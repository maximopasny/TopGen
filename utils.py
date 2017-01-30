from math import sqrt
from constants import *


class Status:
    FREE = 0
    AVAILABLE = 1
    BUSY = 2
    STATION = 3


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    x = -1
    y = -1
    neighbors = []
    status = Status.FREE
    id = -1

    def equals(self, point2):
        if self.x == point2.x and self.y == point2.y:
            return True
        else:
            return False

    def id(self):
        return self.x + self.y * Y_SIZE


def points_distance(point1, point2):
    return sqrt(pow((point1.x - point2.x), 2) + pow((point1.y - point2.y), 2))
