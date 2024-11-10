# from launch import LaunchDescription
# from launch_ros.actions import Node
 
# def generate_launch_description():
#     return LaunchDescription([
#         Node(
#             package='turtlesim',
#             executable='turtlesim_node',
#             name='tortuga1'
#         ),
#     ])
from launch import LaunchDescription
from launch_ros.actions import Node
 
def generate_launch_description():
    ld = LaunchDescription()
    turtlesim_node = Node(
        package="turtlesim",
        executable="turtlesim_node",
        name='sim'
    )
 
    ld.add_action(turtlesim_node)
    return ld