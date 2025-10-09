#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from geometry_msgs.msg import Twist
from turtlebot_action_drive.action import DriveCommand
import math
import time


class DrivingNode(Node):
    def __init__(self):
        super().__init__('driving_node')
        
        # Create publisher for cmd_vel
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel_unstamped', 10)
        
        # Create action server
        self._action_server = ActionServer(
            self,
            DriveCommand,
            'drive_command',
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback
        )
        
        self.get_logger().info('Driving Node started and ready to receive commands')
    
    def goal_callback(self, goal_request):
        """Accept or reject a client request to begin an action"""
        self.get_logger().info('Received goal request')
        return GoalResponse.ACCEPT
    
    def cancel_callback(self, goal_handle):
        """Accept or reject a client request to cancel an action"""
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT
    
    def execute_callback(self, goal_handle):
        """Execute the action"""
        self.get_logger().info('Executing goal...')
        
        request = goal_handle.request
        distance = request.distance
        angle = request.angle
        
        # Validate the request
        if distance < 0 or angle < 0:
            self.get_logger().error('Negative values not allowed')
            goal_handle.abort()
            return DriveCommand.Result()
        
        if distance != 0.0 and angle != 0.0:
            self.get_logger().error('Both distance and angle are non-zero. Only one can be non-zero.')
            goal_handle.abort()
            return DriveCommand.Result()
        
        if distance == 0.0 and angle == 0.0:
            self.get_logger().warn('Both distance and angle are zero, nothing to do')
            goal_handle.succeed()
            return DriveCommand.Result()
        
        # Execute the appropriate command
        if distance > 0:
            self.move_distance(distance)
        elif angle > 0:
            self.turn_angle(angle)
        
        # Mark goal as succeeded
        goal_handle.succeed()
        
        # Return empty result
        result = DriveCommand.Result()
        return result
    
    def move_distance(self, distance):
        """Move forward by the specified distance"""
        self.get_logger().info(f'Moving forward {distance} meters')
        
        # Set linear velocity (m/s)
        linear_speed = 0.2
        
        # Calculate duration
        duration = distance / linear_speed
        
        # Create twist message
        twist = Twist()
        twist.linear.x = linear_speed
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        
        # Publish at 10 Hz for the calculated duration
        start_time = self.get_clock().now()
        rate_hz = 10.0
        sleep_time = 1.0 / rate_hz
        
        while (self.get_clock().now() - start_time).nanoseconds / 1e9 < duration:
            self.cmd_vel_pub.publish(twist)
            time.sleep(sleep_time)
        
        # Stop the robot
        self.stop_robot()
        self.get_logger().info('Movement complete')
    
    def turn_angle(self, angle):
        """Turn by the specified angle in radians"""
        self.get_logger().info(f'Turning {math.degrees(angle):.2f} degrees')
        
        # Set angular velocity (rad/s)
        angular_speed = 0.5
        
        # Calculate duration
        duration = angle / angular_speed
        
        # Create twist message
        twist = Twist()
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = angular_speed
        
        # Publish at 10 Hz for the calculated duration
        start_time = self.get_clock().now()
        rate_hz = 10.0
        sleep_time = 1.0 / rate_hz
        
        while (self.get_clock().now() - start_time).nanoseconds / 1e9 < duration:
            self.cmd_vel_pub.publish(twist)
            time.sleep(sleep_time)
        
        # Stop the robot
        self.stop_robot()
        self.get_logger().info('Turn complete')
    
    def stop_robot(self):
        """Send a stop command to the robot"""
        twist = Twist()
        twist.linear.x = 0.0
        twist.linear.y = 0.0
        twist.linear.z = 0.0
        twist.angular.x = 0.0
        twist.angular.y = 0.0
        twist.angular.z = 0.0
        
        # Publish stop command multiple times to ensure it's received
        for _ in range(10):
            self.cmd_vel_pub.publish(twist)
            time.sleep(0.01)


def main(args=None):
    rclpy.init(args=args)
    
    driving_node = DrivingNode()
    
    try:
        rclpy.spin(driving_node)
    except KeyboardInterrupt:
        pass
    
    driving_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()