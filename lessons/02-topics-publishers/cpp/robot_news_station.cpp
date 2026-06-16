#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp" //get String message type

class RobotNewsStation:public rclcpp::Node{
    public:
        RobotNewsStation():Node("robot_news_station"){
            //Create a publisher with <MessageType>(topic_name, queue_size)
            publisher_=this->create_publisher<example_interfaces::msg::String>("robot_news",10);
            //create a timer that calls publishNews every second
            timer_=this->create_wall_timer(std::chrono::seconds(1),
            std::bind(&RobotNewsStation::publishNews,this));
            RCLCPP_INFO(this->get_logger(),"RObot News Station has started");//print startup messge onto the console
        }
    private:
        void publishNews() {
            auto msg = example_interfaces::msg::String();//create a string message object
            msg.data="Breaking News: Robot News Station is live!";//fill data field of the message 
            publisher_->publish(msg);//publish the message on the topic
        }
        rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;//Shared pointer to a publisher object that can publish String 
        rclcpp::TimerBase::SharedPtr timer_;//Shared pointer to a timer object
};      

int main(int argc, char **argv) {
    rclcpp::init(argc,argv);//start ROS2 communication
    auto node = std::make_shared<RobotNewsStation>();//create an instance of the node
    rclcpp::spin(node);//keep the node alive and processing callbacks
    rclcpp::shutdown();//shutdown ROS2 comunication
    return 0;

}