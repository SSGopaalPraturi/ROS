cd ~/ros2_ws

colcon build --packages-select lab4_driving_control

source install/setup.bash

ros2 run lab4_driving_control open_loop

ros2 run lab4_driving_control closed_loop

ros2 run lab4_driving_control return_to_start
