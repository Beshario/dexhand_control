
# dexhand_control ROS2 Package

## Overview

`dexhand_control` is a ROS2 package designed for controlling the DexHand robotic system. It provides functionalities for managing the robotic hand's movements and interactions.

## Dependencies

Ensure the following dependencies are installed in your ROS2 environment:

- `ros2_control`: ROS2 control framework for managing controllers.
- `ros2_controllers`: ROS2 package providing various controllers for robot joints.
- `dexhand_description`: Package containing the DexHand robot description files.

```
sudo apt install ros-humble-moveit 
```

```
sudo apt install ros-humble-ros2-control 
```

```
sudo apt install ros-humble-ros2-controllers
```

## Installation

1. Clone this repository into your ROS2 workspace, src folder

```
cd ..
```

```
colcon build
```

```
source install/setup.bash   
```
to launch the demo package

```
ros2 launch dexhand_control demo.launch.py
```
