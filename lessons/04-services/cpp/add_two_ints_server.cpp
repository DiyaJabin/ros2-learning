#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"
using namespace std::placeholders;//to send extra parameters

class AddTwoIntsServer : public rclcpp::Node
{
    public:
    AddTwoIntsServer(): Node("add_two_ints_server"){
        server_=this->create_service<example_interfaces::srv::AddTwoInts>(//service type
            "add_two_ints",//service name
            std::bind(&AddTwoIntsServer::callbackAddTwoInts,this,_1,_2)//callback function with two extra parameters passed
        );
        RCLCPP_INFO(this->get_logger(),"Add Two Ints service has been started");
    }

    private:
    rclcpp::Service<example_interfaces::srv::AddTwoInts>::SharedPtr server_;//service server is stored as a shared pointer
    void callbackAddTwoInts(const example_interfaces::srv::AddTwoInts::Request::SharedPtr request,
                            const example_interfaces::srv::AddTwoInts::Response::SharedPtr response)//request and response are received as shared pointers
        {
            response->sum=request->a+request->b;//no need to return the response here like in Python,the response object is sent automatically by ROS2 when the callback exits
            RCLCPP_INFO(this->get_logger(),"%d + %d = %d",(int)request->a,(int)request->b,(int)response->sum);
        }

};


int main(int argc, char **argv) {
    rclcpp::init(argc,argv);
    auto node=std::make_shared<AddTwoIntsServer>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}

