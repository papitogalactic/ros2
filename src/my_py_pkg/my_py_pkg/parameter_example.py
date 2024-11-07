#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node

class ParameterExampleNode(Node):

    def __init__(self):
        super().__init__("parameter_example_node")  #es el nombre que recibe como nodo 
        self.declare_parameter("number_inicio",0.0)
        self.declare_parameter("frecuencia_contador",1.0)
        self.counter_=self.get_parameter("number_inicio").value
        self.frecuencia_contador_=self.get_parameter("frecuencia_contador").value

        self.get_logger().info("Hello Ros2")
        self.create_timer(1/self.frecuencia_contador_,self.timer_callback) # funcion que llama a timer_callback con un f de 0.5 es decir 2 veces por segundo

    def timer_callback(self):
        self.counter_ +=1
        self.get_logger().info("HELLO " + str(self.counter_))

def main(args=None):

    rclpy.init(args=args)
    node=ParameterExampleNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()

