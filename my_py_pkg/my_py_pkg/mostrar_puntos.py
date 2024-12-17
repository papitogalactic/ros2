#!/usr/bin/env python3

import rclpy
import math
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class mostrar_puntos(Node):
    def __init__(self):
        super().__init__('lidar_subscriber')

        #suscriptor al topic del LiDAR
        self.subscription = self.create_subscription(
            LaserScan,  # Tipo de mensaje
            '/laser1',  # topic del LiDAR 
            self.listener_callback,  # func de callback
            10  # Tamaño de la cola de mensajes
        )
        self.subscription  # evita advertencias sobre el uso no empleado

        self.get_logger().info('Nodo lidar_subscriber iniciado. Escuchando datos del sensor LiDAR...')

    def listener_callback(self, msg):
        # Muestra valores del mensaje de LiDAR
        self.get_logger().info(f'  Rangos: {msg.ranges[:180]}')
        # mas detalles de info del sensor
        # self.get_logger().info(f'  Ángulo mínimo: {msg.angle_min} rad')
        # self.get_logger().info(f'  Ángulo máximo: {msg.angle_max} rad')
        # self.get_logger().info(f'  Incremento angular: {msg.angle_increment} rad')
        # self.get_logger().info(f'  Rango mínimo: {msg.range_min} m')
        # self.get_logger().info(f'  Rango máximo: {msg.range_max} m')

def main(args=None):
    rclpy.init(args=args)
    node = mostrar_puntos()
    rclpy.spin(node)    #se mantiene en bucle
    rclpy.shutdown()   #cierra el nodo correctamente

if __name__ == '__main__':
    main()
