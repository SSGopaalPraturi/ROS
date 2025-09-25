import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped

class PathDriverNode(Node):
    """
    A node to drive a TurtleBot in predefined paths.
    """
    def __init__(self):
        super().__init__('path_driver_node')

        # Create publisher for cmd_vel
        self.publisher_ = self.create_publisher(TwistStamped, 'cmd_vel', 10)

        # --- Constants and Configuration ---
        self.TIMER_PERIOD = 0.1  # seconds (10 Hz callback)
        self.LINEAR_SPEED = 0.2  # meters/second
        self.ANGULAR_SPEED = 0.4 # radians/second

        # --- State Machine Variables ---
        self.state = 'STOPPED'
        self.task = 'DRIVE_P_SHAPE' # <-- CHANGE THIS TO RUN DIFFERENT TASKS
        # Available tasks: 'DRIVE_STRAIGHT', 'DRIVE_CIRCLE', 'DRIVE_90_DEG_ARC', 'DRIVE_P_SHAPE'

        self.state_start_time = self.get_clock().now()
        self.target_duration = 0.0

        # Create a timer that fires every TIMER_PERIOD seconds
        self.timer = self.create_timer(self.TIMER_PERIOD, self.timer_callback)
        self.get_logger().info(f"Path Driver node started. Executing task: {self.task}")
        self.start_task()

    def create_linear_twist(self, x_velocity):
        """Creates a TwistStamped message for linear motion."""
        msg = TwistStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'base_link'
        msg.twist.linear.x = float(x_velocity)
        msg.twist.angular.z = 0.0
        return msg

    def create_angular_twist(self, z_velocity, x_velocity=0.0):
        """Creates a TwistStamped message for angular motion (turning)."""
        msg = TwistStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'base_link'
        msg.twist.linear.x = float(x_velocity)
        msg.twist.angular.z = float(z_velocity)
        return msg

    def start_task(self):
        """Initializes the state machine based on the selected task."""
        if self.task == 'DRIVE_STRAIGHT':
            # Time = Distance / Speed
            self.target_duration = 0.50 / self.LINEAR_SPEED
            self.state = 'DRIVING_STRAIGHT'
        elif self.task == 'DRIVE_CIRCLE':
            # Time = Angle / Angular Speed (2*PI for a full circle)
            self.target_duration = (2 * math.pi) / self.ANGULAR_SPEED
            self.state = 'TURNING'
        elif self.task == 'DRIVE_90_DEG_ARC':
            # Time = Angle / Angular Speed (PI/2 for 90 degrees)
            self.target_duration = (math.pi / 2) / self.ANGULAR_SPEED
            self.state = 'TURNING'
        elif self.task == 'DRIVE_P_SHAPE':
            # First part of the 'P': drive straight
            self.target_duration = 0.50 / self.LINEAR_SPEED
            self.state = 'DRIVING_STRAIGHT'
        
        self.state_start_time = self.get_clock().now()
        self.get_logger().info(f"Starting state '{self.state}' for {self.target_duration:.2f} seconds.")

    def timer_callback(self):
        """Main callback for the state machine."""
        elapsed_time = (self.get_clock().now() - self.state_start_time).nanoseconds / 1e9

        if self.state == 'STOPPED':
            self.publisher_.publish(self.create_linear_twist(0.0))
            return

        # Check if the current action's duration has been reached
        if elapsed_time > self.target_duration:
            # --- State Transition Logic ---
            if self.task == 'DRIVE_P_SHAPE' and self.state == 'DRIVING_STRAIGHT':
                self.get_logger().info("Finished straight part. Starting circle part.")
                # Time for a full circle with 0.5m radius
                # v = w * r  => w = v / r
                angular_speed_for_p = self.LINEAR_SPEED / 0.50
                self.target_duration = (2 * math.pi) / angular_speed_for_p
                self.state = 'TURNING'
                self.state_start_time = self.get_clock().now()
            else:
                self.get_logger().info("Task complete. Stopping.")
                self.state = 'STOPPED'
                self.publisher_.publish(self.create_linear_twist(0.0))
                self.destroy_node() # Stop the node
                return
        
        # --- Action Publishing Logic ---
        if self.state == 'DRIVING_STRAIGHT':
            twist_msg = self.create_linear_twist(self.LINEAR_SPEED)
            self.publisher_.publish(twist_msg)
        elif self.state == 'TURNING':
            linear_speed = 0.0
            angular_speed = self.ANGULAR_SPEED
            
            if self.task == 'DRIVE_CIRCLE' or self.task == 'DRIVE_90_DEG_ARC':
                # To drive in a circle of 1m radius: v = w * r => v = w * 1.0
                linear_speed = self.ANGULAR_SPEED * 1.0
            elif self.task == 'DRIVE_P_SHAPE':
                 # For the 'P', radius is 0.5m: v = w * 0.5
                angular_speed_for_p = self.LINEAR_SPEED / 0.50
                linear_speed = self.LINEAR_SPEED
                angular_speed = angular_speed_for_p

            twist_msg = self.create_angular_twist(angular_speed, linear_speed)
            self.publisher_.publish(twist_msg)

def main(args=None):
    rclpy.init(args=None)
    node = PathDriverNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
