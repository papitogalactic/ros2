from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld=LaunchDescription()

    robot_news_station_node_launch=Node(   #creo un nodo con el nombre que yo elija
        package="my_py_pkg",
        executable="robot_news_station"
    )

    smartphone_node_launch=Node(
        package="my_py_pkg",
        executable="smartphone"
    )


    ld.add_action(smartphone_node_launch) 
    ld.add_action(robot_news_station_node_launch)
    
    return ld
