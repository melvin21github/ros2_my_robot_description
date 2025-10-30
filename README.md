# 🦾 My Robot Description (ROS2 Humble)

This project defines a **2-wheeled differential drive robot** for simulation in **Gazebo** and visualization in **RViz**.  
It’s designed as part of my learning and research in **Computer Vision, AI, and Robotics**.

---

## 🚀 Features
- URDF-based robot model with wheel and base links  
- Supports **joint_state_publisher_gui** for interactive joint control  
- Launch files for **RViz2** and **Gazebo simulation**  
- Fully modular file structure for easy extension (e.g., sensors, camera)  
- Compatible with **ROS2 Humble Hawksbill**

---

## 🧠 Requirements
Make sure the following packages are installed:
```bash
sudo apt install ros-humble-joint-state-publisher-gui
sudo apt install ros-humble-xacro
sudo apt install ros-humble-gazebo-ros-pkgs

▶️ How to Run
1️⃣ Build the workspace
bashCopy codecd ~/ros2_ws
colcon build
source install/setup.bash

2️⃣ Launch in RViz
bashCopy coderos2 launch my_robot_description display.launch.py

3️⃣ Launch in Gazebo
bashCopy coderos2 launch my_robot_description gazebo.launch.py
