
## Lab 3: TurtleBot Action Drive

Action-based drive control system for TurtleBot4 using ROS 2 custom actions.

### Features

- **Custom Action Interface**: `DriveCommand.action` with distance and angle parameters
- **Executive Node** (Action Client): Interactive command-line interface for user input
- **Driving Node** (Action Server): Processes commands and controls robot movement
- **Launch File**: Starts both nodes simultaneously

### Requirements

- ROS 2 Jazzy
- Python 3.12+

### Build Instructions
```bash
cd ~/MyGit/ros2_ws
colcon build --packages-select turtlebot_action_drive
source install/setup.bash

### Option 1: Using Launch File
ros2 launch turtlebot_action_drive turtlebot_action_launch.py
### Option 2: Manual Launch
Terminal 1 - Start the Action Server:
cd ~/MyGit/ros2_ws
source install/setup.bash
ros2 run turtlebot_action_drive driving_node.py
Terminal 2 - Start the Action Client:
cd ~/MyGit/ros2_ws
source install/setup.bash
ros2 run turtlebot_action_drive executive_node.py
