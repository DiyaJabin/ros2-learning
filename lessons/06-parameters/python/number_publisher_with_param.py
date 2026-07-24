#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32

class NumberPublisher(Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.declare_parameter("number",2) #Declare a parameter named 'number' with default value 2
        self.declare_parameter("timer_period",1.0) #Declare a parameter with name 'timer_period', having default value 1s
        self.number_=self.get_parameter("number").value #Get value passed into parameter
        self.timer_period_=self.get_parameter("timer_period").value
        self.publisher_=self.create_publisher(Int32,"number",10)
        self.timer_=self.create_timer(self.timer_period_,self.publish_number)
        self.get_logger().info("Number Publisher has been started.")


    def publish_number(self):
        msg=Int32()
        msg.data=self.number_
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node=NumberPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print(f"\nShutting down node....")
    finally:
        node.destroy_node()
        if rclpy.ok(): #returns false if ros has already shut down
            rclpy.shutdown()

if __name__=="__main__":
    main()