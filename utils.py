from math import sqrt


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
    status = Status.FREE

    def equals(self, point2):
        if self.x == point2.x and self.y == point2.y:
            return True
        else:
            return False


def points_distance(point1, point2):
    return sqrt(pow(2, (point1.x - point2.x)) + pow(2, (point1.y - point2.y)))