import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from nav_msgs.msg import Odometry
import sys, select, tty, termios


class RobotController(Node):

    def __init__(self):
        super().__init__('key_publisher')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )
        self.service = self.create_service(Empty, 'stop_robot', self.stop_robot_callback)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.settings = termios.tcgetattr(sys.stdin)
        self.current_velocity = Twist()
        self.robot_ready = False

    def timer_callback(self):
        key = self.get_key()
        twist = Twist()
        if key == 'w':
            twist.linear.x = 0.5
        elif key == 's':
            twist.linear.x = -0.5
        elif key == 'a':
            twist.angular.z = 0.5
        elif key == 'd':
            twist.angular.z = -0.5
        elif key == 'x':  # Mata Robôs 2000
            self.stop_robot()
        elif key == '\x03':  # Ctrl+C
            print('debugging aaahh')
            self.destroy_node()
            rclpy.shutdown()

        if self.robot_ready:
            self.publisher_.publish(twist)
            self.get_logger().info(f'Publishing: linear.x={twist.linear.x:.2f}, angular.z={twist.angular.z:.2f}')
            self.get_logger().info(f'Current Velocity: linear.x={self.current_velocity.linear.x:.2f}, angular.z={self.current_velocity.angular.z:.2f}')
        else:
            self.get_logger().warn('Robot not ready. Command not sent.')

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key

    def odom_callback(self, msg):
        self.current_velocity = msg.twist.twist
        self.robot_ready = True 

    def stop_robot_callback(self, request, response):
        self.stop_robot()
        return response

    def stop_robot(self):
        twist = Twist()
        self.publisher_.publish(twist)
        self.get_logger().info('Stopping the robot')
        self.destroy_node()
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
