#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetBatteryIndicator

class Battery(Node):
    def __init__(self):
        super().__init__("battery")
        self.battery_level=0 #initially battery empty
        self.charging=True #charge up first
        self.client_=self.create_client(srv_type=SetBatteryIndicator,
                                        srv_name="set_battery_indicator")
        self.timer_=self.create_timer(0.2,callback=self.simulate_battery_level)
        self.get_logger().info("Battery node has been started")
        
        
    def simulate_battery_level(self):
        if self.battery_level==100:
            self.charging=False
        elif self.battery_level==0:
            self.charging=True
            self.charging=True
        if self.charging==True:
            self.battery_level+=1
        else:
            self.battery_level-=1
        self.call_set_battery_indicator()

    def call_set_battery_indicator(self):
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("Waiting for set_battery_indicator service....")

        request=SetBatteryIndicator.Request()
        request.battery_level=self.battery_level

        future=self.client_.call_async(request)
        future.add_done_callback(self.callback_call_set_battery_indicator)

    def callback_call_set_battery_indicator(self,future):
        response=future.result()
        self.get_logger().info(f"Success: {response.success} | Message: {response.message}")

                
def main(args=None):
    rclpy.init(args=args)
    node=Battery()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
