#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

using namespace std::chrono_literals;

class NumberPublisher: public rclcpp::Node 
{
    public:
        NumberPublisher(): Node("number_publisher")
        {
            this->declare_parameter("number",2);//initialize parameter with name 'number' and default value 2
            this->declare_parameter("timer_period",1.0);//initialize parameter with name 'time period' and default value 1.0
            number_=this->get_parameter("number").as_int();//get value of the parameter as an integer
            timer_period_=this->get_parameter("timer_period").as_double();//get value of the parameter as a double

            number_publisher_=this->create_publisher<example_interfaces::msg::Int64>("number",10);
            number_timer_=this->create_wall_timer(std::chrono::duration<double>(timer_period_),
                                                    std::bind(&NumberPublisher::publishNumber,this));
            RCLCPP_INFO(this->get_logger(),"Number publisher node has been started");

        }
    private:
        int number_;
        double timer_period_;
        rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr number_publisher_;
        rclcpp::TimerBase::SharedPtr number_timer_;
        void publishNumber() {
            auto msg = example_interfaces::msg::Int64();
            msg.data=number_;
            number_publisher_->publish(msg);

        }

};

int main(int argc,char **argv) {
    rclcpp::init(argc,argv);
    auto node=std::make_shared<NumberPublisher>();
    rclcpp::spin(node);
    RCLCPP_INFO(node->get_logger(),"Shutting down node....");
    rclcpp::shutdown();
    return 0;
}