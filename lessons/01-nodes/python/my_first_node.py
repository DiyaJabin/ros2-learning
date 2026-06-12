#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self): #Constructor of the MyNode class
        super().__init__("my_first_node") #Initialize the Node with the name "my_first_node"
        self.get_logger().info("Hello ROS2") #Log a message to the console
        self.create_timer(1.0,self.timer_callback) #Creates a timer that calls the function every 1 second
        self.counter_=0

    def timer_callback(self):
        self.get_logger().info(f"Timer callback called {self.counter_} times")
        self.counter_+=1

def main(args=None):
    rclpy.init(args=args) #Initialize the ROS2 system
    node=MyNode() #Create an instance of the MyNode class
    rclpy.spin(node) #Keep the node alive until Ctrl+C is pressed
    rclpy.shutdown() #Properly shutdown the ROS2 system

if __name__=="__main__":
    main()
