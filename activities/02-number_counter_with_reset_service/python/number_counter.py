#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32
from example_interfaces.srv import SetBool

class NumberCounter(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.counter_=0
        self.subscriber_=self.create_subscription(Int32,
                                                   "number",
                                                   self.callback_number,10)
        self.publisher_=self.create_publisher(Int32,"number_count",10)
        self.reset_counter_service=self.create_service(SetBool,
                                        "reset_counter",
                                        callback=self.callback_reset_counter)
        self.get_logger().info("Number Counter has been started")

    def callback_number(self,msg:Int32):
        self.counter_+=msg.data
        msg=Int32()
        msg.data=self.counter_
        self.publisher_.publish(msg)

    def callback_reset_counter(self,request:SetBool.Request,response:SetBool.Response):
        if request.data:
            self.counter_=0
            response.success=True
            response.message="Counter reset successfully"
        else:
            response.success=False
            response.message="Counter reset failed"
        return response

def main(args=None):
    rclpy.init(args=args)
    node=NumberCounter()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()