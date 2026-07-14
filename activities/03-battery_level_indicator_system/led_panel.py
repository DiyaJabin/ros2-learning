#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedPanelState
from my_robot_interfaces.srv import SetBatteryIndicator

class LedPanel(Node):
    def __init__(self):
        super().__init__("led_panel")
        self.led_status=[0,0,0,0] #initially battery empty
        self.publisher_=self.create_publisher(LedPanelState,"led_panel_state",10)
        self.service_=self.create_service(SetBatteryIndicator,"set_battery_indicator",self.callback_set_battery_indicator)
        self.timer_=self.create_timer(1,self.publish_led_status)
        self.get_logger().info("LED Panel has been started")

    def callback_set_battery_indicator(self,request:SetBatteryIndicator.Request, response:SetBatteryIndicator.Response):
        battery_level=request.battery_level
        if battery_level >=0 and battery_level<25:
            self.led_status=[1,0,0,0]
        elif battery_level>=25 and battery_level<50:
            self.led_status=[1,1,0,0]
        elif battery_level>=50 and battery_level<75:
            self.led_status=[1,1,1,0]
        elif battery_level>=75 and battery_level<=100:
            self.led_status=[1,1,1,1]
        else:
            response.success=False
            response.message="Invalid battery level received; should be between 0 and 100"
            return
        response.success=True
        response.message="Battery level set successfully"
        return response


    def publish_led_status(self):
        msg=LedPanelState()
        msg.led_status=self.led_status
        self.publisher_.publish(msg)


    
def main(args=None):
    rclpy.init(args=args)
    node=LedPanel()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
