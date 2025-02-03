import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    # Đường dẫn đến gói Hexapod
    hexapod_description_dir = get_package_share_directory('hexapod')

    # Declare the `model` argument
    model_arg = DeclareLaunchArgument(
        name='model',
        default_value=PathJoinSubstitution([hexapod_description_dir, 'urdf', 'Hexapod.urdf']),
        description='Absolute path to the robot URDF file'
    )

    # Load robot description (URDF)
    robot_description_param = {
        'robot_description': LaunchConfiguration('model')
    }

    # Joint State Publisher GUI node
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    # Robot State Publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[robot_description_param]
    )

    # RViz node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', PathJoinSubstitution([hexapod_description_dir, 'urdf.rviz'])]
    )

    # Return the launch description
    return LaunchDescription([
        model_arg,
        joint_state_publisher_gui_node,
        robot_state_publisher_node,
        rviz_node
    ])
