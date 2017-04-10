from math import sqrt
from constants import *


class Status:
    FREE = 0
    AVAILABLE = 1
    BUSY = 2
    STATION = 3


class Color:
    ZERO = 0
    ONE = 1


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    x = -1
    y = -1
    neighbors_ignore_coloring = []
    neighbors_note_coloring = []
    status = Status.FREE
    id = -1
    color = Color.ZERO

    def equals(self, point2):
        if self.x == point2.x and self.y == point2.y:
            return True
        else:
            return False

    def id(self):
        return self.x + self.y * Y_SIZE


def points_distance(point1, point2):
    return sqrt(pow((point1.x - point2.x), 2) + pow((point1.y - point2.y), 2))


def linear_to_dual(linear_coordinate):
    x = linear_coordinate % X_SIZE
    y = linear_coordinate // X_SIZE
    return (x, y)


def get_point_object_by_id(grid, linear_coordinate):
    x = linear_coordinate % X_SIZE
    y = linear_coordinate // X_SIZE
    return grid[y][x]
