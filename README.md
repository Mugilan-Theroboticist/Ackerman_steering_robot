# 🚗 Gazebo Ackermann Steering Vehicle (ROS 2)

This repository contains a **ROS 2-based Ackermann steering vehicle simulation** using Gazebo.

The vehicle supports **steering angle and velocity control**, and includes a **front camera sensor** for vision-based applications. This setup is ideal for developing and testing **autonomous driving algorithms** in simulation.

---
<img width="800" height="450" alt="435512541-1726cb9f-d4c0-4b1a-90e4-4b3c395b9268" src="https://github.com/user-attachments/assets/16f142f0-2dd9-48c9-a813-37848b5b7935" />

## 🚀 Features

* ✅ Ackermann steering kinematics
* ✅ Velocity and steering control
* ✅ Gazebo simulation
* ✅ Front camera (image streaming)
* ✅ Teleoperation support
* ✅ Configurable parameters

---

## ▶️ Quick Start

```bash
cd ~/test_ws
source install/setup.bash

ros2 launch ackerman_steering_vehicle vehicle.launch.py
```

---



## 🎮 Control the Vehicle

### 🔹 Steering Control

```bash
ros2 topic pub /steering_angle std_msgs/msg/Float64 "data: 0.3"
```

---

### 🔹 Teleoperation

```bash
python3 ~/test_ws/src/ackerman_steering_vehicle/launch/teleop_ackermann.py
```

---

## 📸 Simulation

![Vehicle Simulation](images/vehicle.png)

---

## ⚙️ Requirements

* Ubuntu 22.04 / 24.04
* ROS 2 (Jazzy recommended)
* Gazebo (Harmonic or compatible)

Install required packages:

```bash
sudo apt install -y \
     ros-jazzy-ros2-controllers \
     ros-jazzy-gz-ros2-control \
     ros-jazzy-ros-gz \
     ros-jazzy-ros-gz-bridge \
     ros-jazzy-joint-state-publisher \
     ros-jazzy-robot-state-publisher \
     ros-jazzy-xacro \
     ros-jazzy-joy
```

---

## 🔧 Build

```bash
source /opt/ros/jazzy/setup.bash

cd ~/test_ws
colcon build
```

---

## 🚀 Usage

### 🔹 Launch Vehicle

```bash
ros2 launch ackerman_steering_vehicle vehicle.launch.py
```

---

### 🔹 Launch with Custom World & Pose

```bash
ros2 launch ackerman_steering_vehicle vehicle.launch.py \
world:=/path_to_world/world.sdf \
x:=1.0 y:=2.0 z:=0.5 R:=0.0 P:=0.0 Y:=1.57
```

---

## 🎮 Control Interfaces

### 🔹 Topics

Publish:

```bash
/steering_angle
/velocity
```

Subscribe:

```bash
/camera/image_raw
/camera/info
```

---

### 🕹️ Joystick Control

```bash
ros2 launch ackerman_steering_vehicle joystick.launch.py
```

---

## ⚙️ Parameters

Config file:

```bash
config/parameters.yaml
```

### Key Parameters:

```yaml
# Steering & motion
max_steering_angle: 0.6108652
max_velocity: 2.0

# Vehicle dimensions
body_length: 0.3
body_width: 0.18
body_height: 0.05

# Camera
camera_height: 0.2
camera_fov: 1.3962634
image_width: 640
image_height: 480
```

---

## 🔮 Future Improvements

* Autonomous navigation (Nav2)
* SLAM integration
* Object detection using camera
* Real robot deployment

---

## 👨‍💻 Author

**Mugilan**
Robotics & Automation Engineer

---

## 📌 Notes

This project demonstrates a complete **Ackermann steering vehicle simulation pipeline** using ROS 2 and Gazebo, including control, sensing, and visualization.
