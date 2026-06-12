# Lesson 01: ROS 2 Nodes

## Objective

Learn how to create and run ROS 2 nodes using both Python (`rclpy`) and C++ (`rclcpp`).

## Concepts Covered

* ROS 2 Nodes
* Logging with ROS 2
* Timer Callbacks
* Node Execution using `spin()`
* Basic Object-Oriented Structure

## Files

### Python

```text
python/my_first_node.py
```

### C++

```text
cpp/my_first_node.cpp
```

## How It Works

1. A custom node class inherits from the ROS 2 Node class.
2. The node prints a startup message.
3. A timer is created that triggers once every second.
4. The callback function increments a counter and logs the current count.
5. The node remains active using `rclpy.spin()` or `rclcpp::spin()`.

## Example Output

```text
Hello ROS2
Timer callback called 0 times
Timer callback called 1 times
Timer callback called 2 times
...
```

## Key Takeaways

* Nodes are the fundamental building blocks of ROS 2 applications.
* Timers allow periodic execution without using loops.
* Python uses the `rclpy` client library.
* C++ uses the `rclcpp` client library.
