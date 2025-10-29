from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_path = get_package_share_directory('my_robot_description')
    urdf_file = os.path.join(pkg_path, 'urdf', 'my_robot.urdf')

    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    # Publishes transforms from URDF
    robot_state_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_desc}],
        output='screen'
    )

    # GUI sliders for joints
    joint_state_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen'
    )

    # Visualize in RViz
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        output='screen'
    )

    return LaunchDescription([robot_state_pub, joint_state_gui, rviz])
