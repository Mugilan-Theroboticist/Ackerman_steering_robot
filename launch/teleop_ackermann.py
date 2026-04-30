#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
import sys
import termios
import tty

class TeleopAckermann(Node):

    def __init__(self):
        super().__init__('teleop_ackermann')

        self.vel_pub = self.create_publisher(
            Float64MultiArray,
            '/forward_velocity_controller/commands',
            10)

        self.steer_pub = self.create_publisher(
            Float64MultiArray,
            '/forward_position_controller/commands',
            10)

        self.speed = 0.0
        self.steer = 0.0

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        return key

    def run(self):
        print("""
Control your Ackermann Robot:
---------------------------
w : increase speed
s : decrease speed
a : steer left
d : steer right
space : stop
q : quit
""")

        while True:
            key = self.get_key()

            if key == 'w':
                self.speed += 1.0
            elif key == 's':
                self.speed -= 1.0
            elif key == 'a':
                self.steer += 0.1
            elif key == 'd':
                self.steer -= 0.1
            elif key == ' ':
                self.speed = 0.0
                self.steer = 0.0
            elif key == 'q':
                break

            vel_msg = Float64MultiArray()
            vel_msg.data = [self.speed, self.speed]

            steer_msg = Float64MultiArray()
            steer_msg.data = [self.steer, self.steer]

            self.vel_pub.publish(vel_msg)
            self.steer_pub.publish(steer_msg)

            print(f"Speed: {self.speed:.2f}, Steering: {self.steer:.2f}")


def main():
    global settings
    settings = termios.tcgetattr(sys.stdin)

    rclpy.init()
    node = TeleopAckermann()

    try:
        node.run()
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()