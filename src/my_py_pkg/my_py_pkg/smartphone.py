#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node

from example_interfaces.msg import String

class SmartphoneNode(Node):

    def __init__(self):
        super().__init__("smartphone")  #es el nombre que recibe como nodo 
        self.subscriber_ = self.create_subscription(String, "robot_news",self.callback_robot_news,10) #crea una entrada que se subscribe al topic robot_news con el tipo string
        self.get_logger().info("Smartphone has been started")

    def callback_robot_news(self,msg):
        self.get_logger().info(msg.data)
      

def main(args=None):

    rclpy.init(args=args)
    node=SmartphoneNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()