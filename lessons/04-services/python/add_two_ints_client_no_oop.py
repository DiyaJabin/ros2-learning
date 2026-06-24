#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


def main(args=None):
    rclpy.init(args=args)
    node=Node("add_two_ints_client_no_oop")

    client=node.create_client(srv_type=AddTwoInts,
                              srv_name="add_two_ints",
                              )
    while not client.wait_for_service(timeout_sec=1.0): #Wait for server to start, if not started in 1 sec, display the following warning
        node.get_logger().warn("Waiting for Add Two Ints server.....")

    request=AddTwoInts.Request()
    request.a=3
    request.b=5

    future=client.call_async(request)#using asynchronous call instead of normall call as it may cause deadlock
    rclpy.spin_until_future_complete(node,future)#keep the node running until a response is received

    response=future.result()
    node.get_logger().info(f"{request.a}+{request.b}={response.sum}")

    rclpy.shutdown()

if __name__=="__main__":
    main()