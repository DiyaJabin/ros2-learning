#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SmartPhone(Node):
    def __init__(self):
        super().__init__("smartphone")#initialze node with name: smartphone
        #create a subscriber with (topic type, topic name, callback function, queue size)
        self.subscriber_=self.create_subscription(String,
                "robot_news",self.callback_robot_news,10)
        self.get_logger().info("Smartphone has been started")#print startup message to the console
        
    def callback_robot_news(self,msg:String):
        self.get_logger().info(f"Smartphone received: {msg.data}")#Display received message 



def main(args=None):
    rclpy.init(args=args)#initialze ROS2 communication
    node=SmartPhone()#create instance of smartphone node
    rclpy.spin(node)#keep the node alive to process incoming messages
    rclpy.shutdown()#shutdown ROS2 communciation

if __name__=="__main__":
    main()