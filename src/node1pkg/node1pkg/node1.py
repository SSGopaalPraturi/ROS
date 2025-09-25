import rclpy # import the client library
from rclpy.node import Node # import the Node class
from geometry_msgs.msg import TwistStamped

class TwistPublisherNode(Node):
    def __init__(self):
        super().__init__('node1')

        self.publisher_ = self.create_publisher(TwistStamped, 'cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.publish_message)

        self.get_logger().info('Node1 pub started')

    def publish_message(self):
        msg = TwistStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'base_link'
        msg.twist.linear.x = 0.2
        msg.twist.angular.z = 0.0
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing stamped twist: {msg.twist.linear.x}')


    def shutdown_node(self):
        self.destroy_node()


def main(args=Node):
    rclpy.init(args=None)
    node = TwistPublisherNode()
    
    try:
        # spin() will block until the node is destroyed
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # This is the final cleanup step.
        rclpy.shutdown()



if __name__ == '__main__':
    main()
