#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String #importing the String message type from example_interfaces package

class RobotNewsStation(Node):
    def __init__(self):
        super().__init__("robot_news_station")
        self.publisher_=self.create_publisher(String,"robot_news",10) #datatype, topic name and queue size for buffer
        self.timer_=self.create_timer(0.5,self.publish_news) #timer to call the publish_news function every 0.5 seconds
        self.get_logger().info("Robot News Station has been started.")#Print startup message onto the console

    def publish_news(self):
        msg=String()#Create string message object
        msg.data="Hello, this is the latest news from the robot news station!"#Fill message data field
        self.publisher_.publish(msg)#Publish message on topic

def main(args=None):
    rclpy.init(args=args)#Initialize ROS2 communication
    node=RobotNewsStation()#Create node object
    rclpy.spin(node)#Keep node alive and process callbacks
    rclpy.shutdown()#Shutdown ROS2 communication when done 

if __name__=="__main__":
    main()