from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory  # Importa esta función para obtener la ruta del paquete
import os

def generate_launch_description():
    # Ruta del archivo de configuración de RViz
    rviz_config_file = LaunchConfiguration('rviz_config')

    return LaunchDescription([
        # Declarar argumento para el archivo de configuración de RViz
        DeclareLaunchArgument(
            'rviz_config',
            default_value=os.path.join(
                get_package_share_directory('my_robot_bringup'), 
                'rviz', 'demo_depth_camera_ros2.rviz'
            ),
            description='Ruta al archivo de configuración de RViz'
        ),
        
        # Nodo para iniciar RViz con el archivo de configuración especificado
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_file],
            output='screen'
        )
    ])
