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

    # Đường dẫn đến launch file chính của gazebo_ros
    gazebo_launch_dir = get_package_share_directory('gazebo_ros')

    # Sử dụng gazebo.launch.py thay vì empty_world.launch.py
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([gazebo_launch_dir, 'launch', 'gazebo.launch.py'])
        )
    )

    # Static Transform Publisher node (sửa lỗi quaternion)
    tf_footprint_base_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='tf_footprint_base',
        arguments=['0', '0', '0', '0', '0', '0', '1', 'base_link', 'base_footprint']
    )

    # Đường dẫn file URDF của Hexapod
    urdf_file = os.path.join(hexapod_description_dir, 'urdf', 'Hexapod1.urdf')
    if not os.path.exists(urdf_file):
        raise FileNotFoundError(f"⚠️ Không tìm thấy file URDF tại: {urdf_file}")

    # Spawn model node (sửa lỗi `-urdf`)
    spawn_model_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        name='spawn_model',
        arguments=[
            '-file', urdf_file,
            '-entity', 'Hexapod'
        ],
        output='screen'
    )

    return LaunchDescription([
        gazebo_launch,
        tf_footprint_base_node,
        spawn_model_node
    ])
