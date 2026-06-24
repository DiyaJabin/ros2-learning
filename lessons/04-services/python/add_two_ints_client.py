#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial #To be able to pass extra data to the callback

class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.client_=self.create_client(srv_type=AddTwoInts,#service type
                                        srv_name="add_two_ints")#service name
        
    def call_add_two_ints(self,a:int,b:int):
        while not self.client_.wait_for_service(timeout_sec=1.0):#Wait for server to start for 1sec, if not started, display the following warning
            self.get_logger().warn("Waiting for server.....")

        request=AddTwoInts.Request()
        request.a=a
        request.b=b

        future=self.client_.call_async(request)#using asynchronous call as normal call might cause deadlock
        future.add_done_callback(partial(self.callback_call_add_two_ints,request=request))#callback until response arrives(can't spin inside a spinning node)
    
    def callback_call_add_two_ints(self, future,request):
        response=future.result()
        self.get_logger().info(f"{request.a}+{request.b}={response.sum}")


def main(args=None):
    rclpy.init(args=args)
    node=AddTwoIntsClient()
    node.call_add_two_ints(2,3)
    rclpy.spin(node)
    rclpy.shutdown()