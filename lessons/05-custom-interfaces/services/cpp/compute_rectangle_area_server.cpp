#include "rclcpp/rclcpp.hpp"
#include "my_robot_interfaces/srv/compute_rectangle_area.hpp"


using namespace std::placeholders; 

class ComputeRectangleArea:public rclcpp::Node{
    public:
        ComputeRectangleArea():Node("compute_rectangle_area_server") {
            server_=this->create_service<my_robot_interfaces::srv::ComputeRectangleArea>(
                "compute_rectangle_area",
                std::bind(&ComputeRectangleArea::callbackComputeArea,this,_1,_2)
            );
            RCLCPP_INFO(this->get_logger(),"Compute Rectangle Area service has been started");
        }

    private:
        rclcpp::Service<my_robot_interfaces::srv::ComputeRectangleArea>::SharedPtr server_;
        void callbackComputeArea(const my_robot_interfaces::srv::ComputeRectangleArea::Request::SharedPtr request,
                                const my_robot_interfaces::srv::ComputeRectangleArea::Response::SharedPtr response)
                                {
                                    response->area=request->length*request->width;
                                    RCLCPP_INFO(this->get_logger(),"Area of the rectangle is: %d",(int)response->area);
                                }
};

int main(int argc, char **argv) {
    rclcpp::init(argc,argv);
    auto node=std::make_shared<ComputeRectangleArea>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}