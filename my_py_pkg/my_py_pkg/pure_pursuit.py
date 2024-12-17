#!/usr/bin/env python3

import rclpy
import math
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class pure_pursuit(Node):
    def __init__(self):
        super().__init__('lidar_subscriber')

        # Suscriptor al topic del LiDAR
        self.subscription = self.create_subscription(
            LaserScan, 
            '/laser1', 
            self.listener_callback, 
            10
        )
        
        # Publicador para el topic cmd_vel
        self.cmd_vel_publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        self.get_logger().info('Nodo lidar_subscriber iniciado. Escuchando datos del sensor LiDAR...')

    def listener_callback(self, msg):
        
        max_range = max(msg.ranges)  #selecciona el valor maximo
        posiciones = [i for i, r in enumerate(msg.ranges) if r == max_range]#crea un vector con los puntos mas alejados
        puntobuscado=min(posiciones)+((max(posiciones)-min(posiciones))/2) #toma el punto medio de la pista
        #depende para donde gire selecconamos el signo 
        if puntobuscado > 90:
            valorx=math.cos(puntobuscado*math.pi/180)
            valory=math.sin(puntobuscado*math.pi/180)

            if valorx == 0.0:
                valorx=0.001

            velocidadangular=-0.5/(((valorx*valorx)+(valory*valory))/(2*valorx)) #pure pursuit
        else :
            valorx=-math.cos(puntobuscado*math.pi/180)
            valory=math.sin(puntobuscado*math.pi/180)

            if valorx == 0.0:
                valorx=0.001

            velocidadangular=0.5/(((valorx*valorx)+(valory*valory))/(2*valorx))  #pure pursuit

         
        self.get_logger().info(f'Rayo láser con mayor rango: índice={posiciones}, rango={max_range}, puntobuscado={puntobuscado}')
        # Publica el comando de velocidad angular
        self.publicar_cmd_vel(velocidadangular)
        
        

    def publicar_cmd_vel(self, velocidadangular):
        cmd = Twist()
        cmd.linear.x = 0.5                    # Velocidad lineal 
        cmd.angular.z = velocidadangular      # valocidad angular ajustada con pure pursuit

        # Publica el mensaje en cmd_vel
        self.cmd_vel_publisher.publish(cmd)
        self.get_logger().info(f'Publicando en /cmd_vel: linear.x={cmd.linear.x}, angular.z={cmd.angular.z}')

def main(args=None):
    rclpy.init(args=args)
    node = pure_pursuit()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
