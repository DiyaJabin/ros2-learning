#include "rclcpp/rclcpp.hpp"
#include "my_robot_interfaces/msg/hardware_status.hpp"

using namespace std::chrono_literals;

class HardwareStatusPublisher : public rclcpp::Node{
    public:
        HardwareStatusPublisher():Node("hardware_status_publisher")
        {
            pub_=this->create_publisher<my_robot_interfaces::msg::HardwareStatus>("hardware_status",10);
            timer_=this->create_wall_timer(
                1s,
                std::bind(&HardwareStatusPublisher::publish_hardware_status,this)
            );
        RCLCPP_INFO(this->get_logger(),"Hardware Status Publisher has been started");
        }

    private:
    rclcpp::Publisher<my_robot_interfaces::msg::HardwareStatus>::SharedPtr pub_;
    rclcpp::TimerBase::SharedPtr timer_;
    void publish_hardware_status(){
        auto msg=my_robot_interfaces::msg::HardwareStatus();
        msg.temperature=57.6;
        msg.are_motors_ready=false;
        msg.debug_message="Motors are too hot!";
        pub_->publish(msg);
    }

};

int main(int argc, char **argv) {
    rclcpp::init(argc,argv);
    auto node=std::make_shared<HardwareStatusPublisher>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}