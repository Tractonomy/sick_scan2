import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    ld = LaunchDescription()
    config = os.path.join(
        get_package_share_directory('sick_scan2'),
        'config',
        'sick_lms_1xx.yaml'
        )

    node=Node(
        package='sick_scan2',
        name = 'sick_scan2_lms_1xx',
        executable='sick_generic_caller',
        parameters = [config]
    )
    ld.add_action(node)
    return ld
