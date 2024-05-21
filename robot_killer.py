import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node('stop_robot_client')
    client = node.create_client(Empty, 'stop_robot')

    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')

    request = Empty.Request()
    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        node.get_logger().info('Robot stopped successfully')
    else:
        node.get_logger().error('Failed to stop the robot')

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
