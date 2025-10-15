import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class OpenLoopDrive(Node):
    def __init__(self):
        super().__init__('open_loop_drive')
        self.publisher = self.create_publisher(Twist, '/cmd_vel_unstamped', 10)
        
    def drive_forward(self, distance=3.0, speed=0.2):
        """
        Drive forward using time-based open loop control
        distance: target distance in meters
        speed: linear velocity in m/s
        """
        msg = Twist()
        msg.linear.x = speed
        
        # Calculate time needed (open loop - no feedback)
        duration = distance / speed
        
        self.get_logger().info(f'Driving {distance}m at {speed}m/s for {duration}s')
        
        start_time = time.time()
        while time.time() - start_time < duration:
            self.publisher.publish(msg)
            time.sleep(0.1)
        
        # Stop
        msg.linear.x = 0.0
        self.publisher.publish(msg)
        self.get_logger().info('Stopped')

def main(args=None):
    rclpy.init(args=args)
    node = OpenLoopDrive()
    
    try:
        node.drive_forward(distance=3.0, speed=0.2)
        time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
