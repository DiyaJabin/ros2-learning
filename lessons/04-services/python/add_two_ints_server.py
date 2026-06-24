#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts#import the service (this is an inbuilt service in ROS2)

class AddTwoIntsServer(Node):
    def __init__(self):
        super().__init__("add_two_ints_server")
        self.server_=self.create_service(srv_type=AddTwoInts, #server type
                                         srv_name="add_two_ints",#server name
                                         callback=self.callback_add_two_ints)#calback function
        self.get_logger().info("Add Two Ints Server has been started")

    def callback_add_two_ints(self,request:AddTwoInts.Request,response=AddTwoInts.Response):
        response.sum=request.a+request.b
        self.get_logger().info(f"{request.a}+{request.b}={response.sum}")
        return response 
        



def main(args=None):
    rclpy.init(args=args)
    node=AddTwoIntsServer()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()

