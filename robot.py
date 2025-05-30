import numpy as np
from math import cos, sin, radians

class Robot:
    def __init__(self, name, position_x=0, position_y=0, orientation=0):
        self._name = name
        self._position_x = position_x
        self._position_y = position_y
        self._theta = radians(orientation)
        self._initialize_position_matrix()

    def _initialize_position_matrix(self):
        self._position_matrix = np.array([[cos(self._theta), -sin(self._theta), self._position_x],
                                          [sin(self._theta), cos(self._theta), self._position_y],
                                          [0, 0, 1]])

    def move(self, steps):
        d_x = steps
        d_y = 0
        transform_matrix_tr = np.array([[1, 0, d_x],
                                        [0, 1, d_y],
                                        [0, 0, 1]])
        self._position_matrix = self._position_matrix @ transform_matrix_tr

    def turn_left(self, d_theta):
        d_theta = radians(d_theta)
        transform_matrix_rot = np.array([[cos(d_theta), -sin(d_theta), 0],
                                         [sin(d_theta), cos(d_theta), 0],
                                         [0, 0, 1]])
        self._position_matrix = self._position_matrix @ transform_matrix_rot
        self._theta = self._theta + d_theta

    def turn_right(self, d_theta):
        d_theta = -radians(d_theta)
        transform_matrix_rot = np.array([[cos(d_theta), -sin(d_theta), 0],
                                         [sin(d_theta), cos(d_theta), 0],
                                         [0, 0, 1]])
        self._position_matrix = self._position_matrix @ transform_matrix_rot
        self._theta = self._theta+d_theta

    def get_position(self):
        position = [self._position_matrix[0][2], self._position_matrix[1][2], self._theta]

        return position

    def __str__(self):
        return f"Robot {self._name} is at position {self.get_position()}"

class FlyingRobot(Robot):
    def __init__(self, name, position_x=0, position_y=0, orientation=0, altitude=0):
        super().__init__(name, position_x, position_y, orientation)
        self._altitude = altitude

    def ascend(self, d_altitude):
        self._altitude += abs(d_altitude)

    def descend(self, d_altitude):
        self._altitude -= abs(d_altitude)

    def get_position(self):
        position = super().get_position()
        position.append(self._altitude)
        return position

    def __str__(self):
        return f"FlyingRobot {self._name} is at position {self.get_position()}"

class SwimmingRobot(Robot):
    def __init__(self, name, position_x=0, position_y=0, orientation=0, depth=0):
        super().__init__(name, position_x, position_y, orientation)
        self._depth = depth

    def dive(self, d_depth):
        self._depth += abs(d_depth)

    def surface(self, d_depth):
        d_depth = abs(d_depth)
        self._depth = max(0, self._depth - d_depth)

    def get_position(self):
        position = super().get_position()
        position.append(-self._depth)  # Depth is typically represented as negative
        return position

    def __str__(self):
        return f"SwimmingRobot {self._name} is at position {self.get_position()}"

# Testování
robots = [
    Robot("Robot1", 0, 0, 0),
    FlyingRobot("FlyingRobot1", 0, 0, 0, 10),
    SwimmingRobot("SwimmingRobot1", 0, 0, 0, 5)
]

for robot in robots:
    robot.move(10)
    robot.turn_left(30)
    robot.move(20)
    if isinstance(robot, FlyingRobot):
        robot.ascend(5)
    if isinstance(robot, SwimmingRobot):
        robot.dive(3)
    print(robot)

