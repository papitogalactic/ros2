"""
#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node=Node("py_test")
    node.get_logger().info("Hello Ros2")
    rclpy.spin(node)

    rclpy.shutdown()

if __name__=="__main__":
    main()

"""
#crear un node oriendo a objetos
#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")  #es el nombre que recibe como nodo 
        self.counter_=0
        self.get_logger().info("Hello Ros2")
        self.create_timer(0.5,self.timer_callback) # funcion que llama a timer_callback con un f de 0.5 es decir 

    def timer_callback(self):
        self.counter_ +=1
        self.get_logger().info("HELLO " + str(self.counter_))

def main(args=None):

    rclpy.init(args=args)
    node=MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()

