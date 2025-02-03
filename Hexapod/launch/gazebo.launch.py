import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():
    # Đường dẫn đến gói hexapod
    hexapod_description_dir = get_package_share_directory('hexapod')

    # Đường dẫn đến launch file của gazebo_ros
    gazebo_launch_dir = get_package_share_directory('gazebo_ros')

    # Include Gazebo empty world launch file
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([gazebo_launch_dir, 'launch', 'empty_world.launch.py'])
        )
    )

    # Static Transform Publisher node
    tf_footprint_base_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='tf_footprint_base',
        arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'base_footprint', '40']
    )

    # Spawn model node
    spawn_model_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_model',
        arguments=[
            '-file', PathJoinSubstitution([hexapod_description_dir, 'urdf', 'Hexapod.urdf']),
            '-urdf',
            '-entity', 'Hexapod'
        ],
        output='screen'
    )

    # Fake joint calibration node
    fake_joint_calibration_node = Node(
        package='topic_tools',
        executable='relay',
        name='fake_joint_calibration',
        arguments=['/calibrated', 'std_msgs/msg/Bool', 'true'],
        output='screen'
    )

    return LaunchDescription([
        gazebo_launch,
        tf_footprint_base_node,
        spawn_model_node,
        fake_joint_calibration_node
    ])
