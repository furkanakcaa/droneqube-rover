import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped
import time

class MissionNode(Node):
    def __init__(self):
        super().__init__('mission_node')
        self._action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

    def go_to(self, x, y, label):
        self.get_logger().info(f'{label} noktasına gidiliyor: x={x}, y={y}')

        goal = NavigateToPose.Goal()
        goal.pose.header.frame_id = 'map'
        goal.pose.header.stamp = self.get_clock().now().to_msg()
        goal.pose.pose.position.x = x
        goal.pose.pose.position.y = y
        goal.pose.pose.orientation.w = 1.0

        self._action_client.wait_for_server()
        future = self._action_client.send_goal_async(goal)
        rclpy.spin_until_future_complete(self, future)

        goal_handle = future.result()
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        
        self.get_logger().info(f'{label} noktasına ulaşıldı!')

def main(args=None):
    rclpy.init(args=args)
    node = MissionNode()

    waypoints = [
        (1.99, -0.71, 'Home'),
        (0.11, -2.57, 'A'),
        (-0.51, -0.73, 'B'),
        (-1.73, 0.14, 'C'),
        (1.99, -0.71, 'Home')
    ]

    for x, y, label in waypoints:
        node.go_to(x, y, label)
        if label != 'Home':
            time.sleep(1)

    node.get_logger().info('Görev tamamlandı!')
    rclpy.shutdown()

if __name__ == '__main__':
    main()