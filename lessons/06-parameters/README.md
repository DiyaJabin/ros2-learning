# Lesson 06: ROS 2 Parameters

## Objective

Learn how to declare, retrieve, and use ROS 2 parameters to configure node behavior without modifying the source code.

---

## Concepts Covered

- Declaring parameters
- Default parameter values
- Reading parameter values
- Configuring nodes at runtime
- Python (`rclpy`)
- C++ (`rclcpp`)
- Passing parameters using ROS 2 CLI

---

## Parameters Used

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `number` | Integer | `2` | Number published on the topic |
| `timer_period` | Double | `1.0` | Time interval between published messages (seconds) |

---

## Project Structure

```text
python/
└── number_publisher.py

cpp/
└── number_publisher.cpp
```

---

## Running the Node

### Default Parameters

```bash
ros2 run <package_name> number_publisher
```

### Custom Parameters

```bash
ros2 run <package_name> number_publisher \
--ros-args \
-p number:=10 \
-p timer_period:=0.5
```

---

## Demonstration

### Python Implementation

📹 `screenshots_videos/python_demo.mp4`

---

### C++ Implementation

📹 `screenshots/cpp_demo.mp4`

---

## Key Takeaways

- Parameters allow node behavior to be customized without editing code.
- Default values are declared when the node starts.
- Parameter values can be overridden from the command line.
- The same parameter mechanism works in both Python and C++.
- Parameters improve code reusability and flexibility.