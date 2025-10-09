#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from turtlebot_action_drive.action import DriveCommand
import math


class ExecutiveNode(Node):
    def __init__(self):
        super().__init__('executive_node')
        
        # Create action client
        self._action_client = ActionClient(
            self,
            DriveCommand,
            'drive_command'
        )
        
        self.get_logger().info('Executive Node started')
        self.get_logger().info('Waiting for action server...')
        
        # Wait for the action server to be available
        self._action_client.wait_for_server()
        self.get_logger().info('Action server available!')
    
    def send_goal(self, distance, angle):
        """Send a goal to the action server"""
        goal_msg = DriveCommand.Goal()
        goal_msg.distance = distance
        goal_msg.angle = angle
        
        self.get_logger().info(f'Sending goal: distance={distance}, angle={angle}')
        
        # Send the goal
        send_goal_future = self._action_client.send_goal_async(goal_msg)
        
        # Wait for the goal to be accepted
        rclpy.spin_until_future_complete(self, send_goal_future)
        goal_handle = send_goal_future.result()
        
        if not goal_handle.accepted:
            self.get_logger().error('Goal was rejected by server')
            return False
        
        self.get_logger().info('Goal accepted by server, waiting for result...')
        
        # Wait for the result
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        
        result = result_future.result()
        
        if result.status == 4:  # SUCCEEDED
            self.get_logger().info('Goal succeeded!')
            return True
        else:
            self.get_logger().error(f'Goal failed with status: {result.status}')
            return False
    
    def run(self):
        """Main loop for user interaction"""
        print("\n" + "="*50)
        print("TurtleBot Action Drive - Executive Node")
        print("="*50)
        
        while True:
            print("\nOptions:")
            print("  1. Move forward (specify distance in meters)")
            print("  2. Turn (specify angle in degrees)")
            print("  3. Quit")
            
            choice = input("\nEnter your choice (1/2/3): ").strip()
            
            if choice == '1':
                try:
                    distance = float(input("Enter distance to move (meters): "))
                    if distance < 0:
                        print("Error: Distance must be non-negative")
                        continue
                    
                    print(f"\nMoving {distance} meters...")
                    success = self.send_goal(distance, 0.0)
                    
                    if success:
                        print(f"✓ Movement complete!")
                    else:
                        print("✗ Movement failed")
                        
                except ValueError:
                    print("Error: Invalid input. Please enter a number.")
            
            elif choice == '2':
                try:
                    degrees = float(input("Enter angle to turn (degrees): "))
                    if degrees < 0:
                        print("Error: Angle must be non-negative")
                        continue
                    
                    turn_direction = input("Enter direction to turn, left (l) or right (r)")
                    if turn_direction == "r":
                        degrees = -degrees

                    elif turn_direction != "l":
                        print("Error: turn direction must be l or r")
                        continue
                    # Convert degrees to radians
                    radians = math.radians(degrees)
                    
                    print(f"\nTurning {degrees} degrees...")
                    success = self.send_goal(0.0, radians)
                    
                    if success:
                        print(f"✓ Turn complete!")
                    else:
                        print("✗ Turn failed")
                        
                except ValueError:
                    print("Error: Invalid input. Please enter a number.")
            
            elif choice == '3':
                print("\nShutting down...")
                break
            
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")


def main(args=None):
    rclpy.init(args=args)
    
    executive_node = ExecutiveNode()
    
    try:
        executive_node.run()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
    
    executive_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()