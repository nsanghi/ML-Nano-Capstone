from robot import Robot
import sys

if __name__ == '__main__':
    testrobot = Robot(8)
    testrobot.print_grid(testrobot.maze)
    print
    testrobot.print_grid(testrobot.dist)
