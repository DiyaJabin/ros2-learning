#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import ComputeRectangleArea


class ComputeRectangleAreaServer(Node):
    def __init__(self):
        super().__init__("compute_rectangle_area_server")
        self.server_=self.create_service(srv_type=ComputeRectangleArea,
                                     srv_name="compute_rectangle_area",
                                     callback=self.compute_rectangle_area_callback)
        self.get_logger().info("Compute Rectangle Area Server has been started.")

    def compute_rectangle_area_callback(self,request:ComputeRectangleArea.Request, response:ComputeRectangleArea.Response):
        response.area=request.length*request.width
        self.get_logger().info(f"Received request: length={request.length}, width={request.width}.")
        self.get_logger().info(f"Sending response: area={response.area}.")
        return response 

def main(args=None):
    rclpy.init(args=args)
    node=ComputeRectangleAreaServer()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()