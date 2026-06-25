#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"
using namespace std::chrono_literals;
using namespace std::placeholders;

class AddTwoIntsClient : public rclcpp::Node
{
    public:
    AddTwoIntsClient(): Node("add_two_ints_client") {
        client_=this->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");//create client with service name and service type
    }
    
    void callAddTwoInts(int a, int b) { //function to call the service
        while (!client_->wait_for_service(1s)) {//keep checking every second and display the following warning until the server is available
            RCLCPP_WARN(this->get_logger(),"Waiting for the server");
        }
        auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
        request->a=a;
        request->b=b;

        client_->async_send_request(
            request, std::bind(&AddTwoIntsClient::callbackAddTwoInts, this, _1)//placeholder for SharedFuture object
        );


    }

    private:
    rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedPtr client_;//declare client as a shared pointer
    void callbackAddTwoInts(rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedFuture future) {
        auto response=future.get();
        RCLCPP_INFO(this->get_logger(),"Sum: %d",(int)response->sum);
    }
};

int main(int argc, char **argv){
    rclcpp::init(argc,argv);
    auto node=std::make_shared<AddTwoIntsClient>();
    node->callAddTwoInts(7,6);
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}