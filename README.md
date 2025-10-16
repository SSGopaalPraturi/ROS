# ROS
## Group C github

### project 3 commands
navigate to your ros2 workspace in terminal
```bash
colcon build --packages-select turtlebot_action_drive
source install/setup.bash
```

#### Option 1: Using Launch File
ros2 launch turtlebot_action_drive turtlebot_action_launch.py

#### Option 2: Manual Launch
Terminal 1 - Start the Action Server:

navigate to your ros2 workspace in terminal
```bash
source install/setup.bash
ros2 run turtlebot_action_drive driving_node.py
```
Terminal 2 - Start the Action Client:

navigate to your ros2 workspace in terminal
```bash
source install/setup.bash
ros2 run turtlebot_action_drive executive_node.py
```

### project 4 commands

navigate to your ros2 workspace in terminal
```bash
colcon build --packages-select lab4_driving_control
source install/setup.bash
ros2 run lab4_driving_control open_loop
ros2 run lab4_driving_control closed_loop
ros2 run lab4_driving_control return_to_start
```