import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped
import math

class TwistPublisherNode(Node):
    def __init__(self):
        super().__init__('node1')
        self.publisher_ = self.create_publisher(TwistStamped, 'cmd_vel', 10)

        # Motion parameters
        self.straight_distance = 0.5   # meters (stem height)
        self.straight_speed = 0.3      # m/s
        self.circle_radius = 0.2       # meters (tight loop)
        self.circle_speed = 0.3        # m/s

        # Derived params
        self.straight_time = self.straight_distance / self.straight_speed
        self.circle_time = (2 * math.pi * self.circle_radius) / self.circle_speed  # full loop

        # Track state
        self.start_time = self.get_clock().now().nanoseconds / 1e9
        self.state = "straight"

        self.timer = self.create_timer(0.1, self.motion_callback)
        self.get_logger().info("P-shape node started")

    def motion_callback(self):
        now = self.get_clock().now().nanoseconds / 1e9
        elapsed = now - self.start_time
        msg = TwistStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "base_link"

        if self.state == "straight":
            if elapsed < self.straight_time:
                msg.twist.linear.x = self.straight_speed
                msg.twist.angular.z = 0.0
            else:
                self.state = "circle"
                self.start_time = now  # reset timer
                self.get_logger().info("Switching to circle motion")
                return

        elif self.state == "circle":
            if elapsed < self.circle_time:  # full loop
                msg.twist.linear.x = self.circle_speed
                msg.twist.angular.z = self.circle_speed / self.circle_radius
            else:
                # stop after P shape is drawn
                msg.twist.linear.x = 0.0
                msg.twist.angular.z = 0.0
                self.get_logger().info("Finished P-shape path")
                self.destroy_node()

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TwistPublisherNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == "__main__":
    main()
