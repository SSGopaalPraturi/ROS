#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # Launch the Driving Node (Action Server)
        Node(
            package='turtlebot_action_drive',
            executable='driving_node.py',
            name='driving_node',
            output='screen',
        ),
        
        # Launch the Executive Node (Action Client) in separate xterm window
        Node(
            package='turtlebot_action_drive',
            executable='executive_node.py',
            name='executive_node',
            output='screen',
            prefix='xterm -hold -e',
        ),
    ])