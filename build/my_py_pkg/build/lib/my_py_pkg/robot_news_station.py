#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node

from example_interfaces.msg import String

class RobotNewsStationNode(Node):

    def __init__(self):
        super().__init__("robot_news_station") #nombre del nodo

        self.publishers_=self.create_publisher(String,"robot_news",10) #crea una salida que publica tipo cadena de caracteres (robot_news es el nombre del topic)
        self.timer_=self.create_timer(0.5, self.publish_news)
        self.get_logger().info("Robot newstation has been started")
        

    def publish_news(self): #crea el mensaje que se va a publicar
        msg=String()
        msg.data="Hello"
        self.publishers_.publish(msg)
   

def main(args=None):

    rclpy.init(args=args)
    node=RobotNewsStationNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
