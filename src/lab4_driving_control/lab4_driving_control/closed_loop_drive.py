import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

class ClosedLoopDrive(Node):
    def __init__(self):
        super().__init__('closed_loop_drive')
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
    
    def drive_forward(self, distance=3.0, speed=0.2, tolerance=0.01):
        """
        Drive forward using odometry feedback
        distance: target distance in meters
        speed: linear velocity in m/s
        tolerance: acceptable error in meters
        """
        # Wait for odometry data
        while not self.odom_received:
            rclpy.spin_once(self, timeout_sec=0.1)
            self.get_logger().info('Waiting for odometry data...')
        
        start_x = self.current_x
        start_y = self.current_y
        
        self.get_logger().info(f'Starting position: ({start_x:.3f}, {start_y:.3f})')
        self.get_logger().info(f'Target distance: {distance}m')
        
        msg = Twist()
        rate = self.create_rate(10)  # 10 Hz
        
        while rclpy.ok():
            # Calculate distance traveled
            dx = self.current_x - start_x
            dy = self.current_y - start_y
            distance_traveled = math.sqrt(dx**2 + dy**2)
            
            remaining = distance - distance_traveled
            
            if remaining <= tolerance:
                self.get_logger().info(f'Target reached! Distance traveled: {distance_traveled:.3f}m')
                break
            
            # Proportional control (slow down as we approach target)
            if remaining < 0.5:
                msg.linear.x = max(0.05, speed * (remaining / 0.5))
            else:
                msg.linear.x = speed
            
            self.publisher.publish(msg)
            rclpy.spin_once(self, timeout_sec=0.1)
        
        # Stop
        msg.linear.x = 0.0
        self.publisher.publish(msg)
        
        final_x = self.current_x
        final_y = self.current_y
        self.get_logger().info(f'Final position: ({final_x:.3f}, {final_y:.3f})')
        self.get_logger().info(f'Error: εx={final_x - start_x - distance:.3f}m, εy={final_y - start_y:.3f}m')

def main(args=None):
    rclpy.init(args=args)
    node = ClosedLoopDrive()
    
    try:
        node.drive_forward(distance=3.0, speed=0.2, tolerance=0.01)
        time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
