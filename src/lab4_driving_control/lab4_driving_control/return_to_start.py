import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import time

class ReturnToStart(Node):
    def __init__(self):
        super().__init__('return_to_start')
        self.publisher = self.create_publisher(Twist, '/cmd_vel_unstamped', 10)
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )
        
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_yaw = 0.0
        self.odom_received = False
        
    def odom_callback(self, msg):
        """Process odometry data"""
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        
        # Convert quaternion to yaw
        orientation = msg.pose.pose.orientation
        siny_cosp = 2 * (orientation.w * orientation.z + orientation.x * orientation.y)
        cosy_cosp = 1 - 2 * (orientation.y**2 + orientation.z**2)
        self.current_yaw = math.atan2(siny_cosp, cosy_cosp)
        
        self.odom_received = True
    
    def normalize_angle(self, angle):
        """Normalize angle to [-pi, pi]"""
        while angle > math.pi:
            angle -= 2 * math.pi
        while angle < -math.pi:
            angle += 2 * math.pi
        return angle
    
    def turn_in_place(self, target_angle, angular_speed=0.3, tolerance=0.02):
        """
        Turn in place to target angle
        target_angle: target yaw in radians
        angular_speed: angular velocity in rad/s
        tolerance: acceptable error in radians
        """
        while not self.odom_received:
            rclpy.spin_once(self, timeout_sec=0.1)
        
        self.get_logger().info(f'Current yaw: {math.degrees(self.current_yaw):.1f}°')
        self.get_logger().info(f'Target yaw: {math.degrees(target_angle):.1f}°')
        
        msg = Twist()
        
        while rclpy.ok():
            angle_diff = self.normalize_angle(target_angle - self.current_yaw)
            
            if abs(angle_diff) <= tolerance:
                self.get_logger().info(f'Turn complete! Final yaw: {math.degrees(self.current_yaw):.1f}°')
                break
            
            # Proportional control for turning
            if abs(angle_diff) < 0.3:
                msg.angular.z = max(0.1, angular_speed * (abs(angle_diff) / 0.3))
            else:
                msg.angular.z = angular_speed
            
            # Turn direction
            if angle_diff < 0:
                msg.angular.z = -msg.angular.z
            
            self.publisher.publish(msg)
            rclpy.spin_once(self, timeout_sec=0.1)
        
        # Stop
        msg.angular.z = 0.0
        self.publisher.publish(msg)
        time.sleep(0.5)
    
    def drive_forward(self, distance, speed=0.2, tolerance=0.01):
        """Drive forward with odometry feedback"""
        while not self.odom_received:
            rclpy.spin_once(self, timeout_sec=0.1)
        
        start_x = self.current_x
        start_y = self.current_y
        
        msg = Twist()
        
        while rclpy.ok():
            dx = self.current_x - start_x
            dy = self.current_y - start_y
            distance_traveled = math.sqrt(dx**2 + dy**2)
            remaining = distance - distance_traveled
            
            if remaining <= tolerance:
                break
            
            if remaining < 0.5:
                msg.linear.x = max(0.05, speed * (remaining / 0.5))
            else:
                msg.linear.x = speed
            
            self.publisher.publish(msg)
            rclpy.spin_once(self, timeout_sec=0.1)
        
        msg.linear.x = 0.0
        self.publisher.publish(msg)
        time.sleep(0.5)
    
    def execute_return_sequence(self):
        """Execute: forward 3m -> turn 180° -> forward 3m -> turn 180°"""
        # Wait for odom
        while not self.odom_received:
            rclpy.spin_once(self, timeout_sec=0.1)
        
        # Record starting pose
        start_x = self.current_x
        start_y = self.current_y
        start_yaw = self.current_yaw
        
        self.get_logger().info(f'Starting pose: ({start_x:.3f}, {start_y:.3f}, {math.degrees(start_yaw):.1f}°)')
        
        # Step 1: Drive forward 3m
        self.get_logger().info('Step 1: Driving forward 3m...')
        self.drive_forward(3.0)
        
        # Step 2: Turn 180°
        self.get_logger().info('Step 2: Turning 180°...')
        target_yaw = self.normalize_angle(self.current_yaw + math.pi)
        self.turn_in_place(target_yaw)
        
        # Step 3: Drive forward 3m
        self.get_logger().info('Step 3: Driving forward 3m...')
        self.drive_forward(3.0)
        
        # Step 4: Turn 180° back to starting orientation
        self.get_logger().info('Step 4: Turning 180° to starting orientation...')
        self.turn_in_place(start_yaw)
        
        # Calculate final error
        final_x = self.current_x
        final_y = self.current_y
        final_yaw = self.current_yaw
        
        error_x = final_x - start_x
        error_y = final_y - start_y
        error_yaw = self.normalize_angle(final_yaw - start_yaw)
        
        self.get_logger().info('='*50)
        self.get_logger().info(f'Final pose: ({final_x:.3f}, {final_y:.3f}, {math.degrees(final_yaw):.1f}°)')
        self.get_logger().info(f'Position error: εx={error_x:.3f}m, εy={error_y:.3f}m')
        self.get_logger().info(f'Orientation error: {math.degrees(error_yaw):.2f}°')
        self.get_logger().info(f'Total position error: {math.sqrt(error_x**2 + error_y**2):.3f}m')
        self.get_logger().info('='*50)

def main(args=None):
    rclpy.init(args=args)
    node = ReturnToStart()
    
    try:
        node.execute_return_sequence()
    except KeyboardInterrupt:
        pass
    finally:
        # Emergency stop
        msg = Twist()
        node.publisher.publish(msg)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
