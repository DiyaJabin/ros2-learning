#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class Smartphone: public rclcpp::Node {
    public:
        Smartphone():Node("smartphone")
        {
            //create a subscriber with <topic_type>(topic_name,queue_size,callback_function)
            subscriber_=this->create_subscription<example_interfaces::msg::String> (
                "robot_news",10,
                std::bind(&Smartphone::callbackRobotNews,this,std::placeholders::_1));
            RCLCPP_INFO(this->get_logger(),"Smartphone has been started");//print startup message to the console
        }


    private:
        void callbackRobotNews(const example_interfaces::msg::String::SharedPtr msg)
        {
            RCLCPP_INFO(this->get_logger(),"Received news: %s",msg->data.c_str());
        }
        rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;//shared pointe to subscriber object
};


int main(int argc, char **argv) {
    rclcpp::init(argc,argv);//initialize ROS2 communication
    auto node = std::make_shared<Smartphone>();//create an instance of the Smartphone node
    rclcpp::spin(node);//keep the node alive and processing incoming messages
    rclcpp::shutdown();//shutdown ROS2 communication
    return 0;
}