#!/usr/bin/env python3

import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import Twist

class cmd_vel_publisher(Node):
    def __init__(self):
        super().__init__("cmd_vel_publisher")
        
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10) #topic 

        timer_period = 0.5  # temporizador para publicar mensajes 
        self.timer = self.create_timer(timer_period, self.publish_cmd_vel)

        self.get_logger().info('Nodo cmd_vel_publisher iniciado')

    def publish_cmd_vel(self):
        twist = Twist()

        twist.linear.x = 0.5  # Velocidad lineal en m/s
        vel_degrees=float
        vel_degrees=20.0 # velocidad en grados/s
        vel_radianes=float
        vel_radianes=vel_degrees*(math.pi/180)
        twist.angular.z = vel_radianes  # Velocidad angular en rad/s

        self.publisher_.publish(twist) 
        self.get_logger().info(f'Publicando: linear.x = {twist.linear.x}, angular.z = {twist.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = cmd_vel_publisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
