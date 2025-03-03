import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # Đường dẫn đến thư mục mô tả hexapod
    hexapod_description_dir = get_package_share_directory('hexapod')
    urdf_file = os.path.join(hexapod_description_dir, 'urdf', 'Hexapod1.urdf')

    # 🔥 Kiểm tra file có tồn tại không
    if not os.path.exists(urdf_file):
        raise FileNotFoundError(f"⚠️ Không tìm thấy file URDF tại: {urdf_file}")

    # 🔥 Đọc nội dung file URDF
    with open(urdf_file, 'r') as file:
        robot_description_content = file.read()

    # Robot State Publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_content}]
    )

    # Joint State Publisher GUI node
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

    # RViz node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', os.path.join(hexapod_description_dir, 'rviz', 'display.rviz')]
    )

    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz_node
    ])
