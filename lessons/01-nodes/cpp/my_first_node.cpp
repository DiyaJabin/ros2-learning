#include "rclcpp/rclcpp.hpp"

class MyNode:public rclcpp::Node{ //Inherit from the Node class provided by ROS2
    public:
        MyNode():Node("my_first_cpp_node"),counter_(0) { //Constructor , initialize the Node with the name "my_first_cpp_node" and initialize conter to 0
            RCLCPP_INFO(this->get_logger(),"Hello ROS2");//Log a message to the console
            timer_=this->create_wall_timer(std::chrono::seconds(1),//Creates a timer that calls the function every one second
            std::bind(&MyNode::timer_callback,this));//Binds the timer callback function to the timer
        }
    private:
        int counter_;
        void timer_callback() {//Fuction that is called every time the timer is triggered
            counter_++;
            RCLCPP_INFO(this->get_logger(),"Timer called %d times",counter_);
        }
        rclcpp::TimerBase::SharedPtr timer_;//Shared pointer to the timer object
};

int main(int argc, char **argv) {
    rclcpp::init(argc,argv); //nitialize ROS2
    auto node = std::make_shared<MyNode>(); //auto means we're bascally begging the compiler to figure out the type for  us
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}