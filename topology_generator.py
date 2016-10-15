from math import sqrt
from random import choice

X_SIZE = 4
Y_SIZE = 4
INNER_RANGE = 1
OUTER_RANGE = 2
NUM_OF_BS = 2

class Statuses:
    FREE = 0
    CORRUPTED = 1
    STATION = 2

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    x = -1
    y = -1
    status = Statuses.FREE

    def equals(self, point2):
        if self.x == point2.x and self.y == point2.y:
            return True
        else:
            return False

points = [[Point(i, j) for i in range(X_SIZE)] for j in range(Y_SIZE)]


def points_distance(point1, point2):
    return sqrt(pow(2, (point1.x - point2.x)) + pow(2, (point1.y - point2.y)))


def linear_to_bin(lin_position):
    return lin_position % X_SIZE, lin_position // X_SIZE


def bin_to_linear(x, y):
    return y * X_SIZE + x


def generate_topology():

    chosen_point = choice(points)
    points[bin_to_linear(chosen_point.x, chosen_point.y)].status = Statuses.STATION
    available_points = []
    for point in points:
        if points_distance(point, chosen_point) <= INNER_RANGE and not chosen_point.equals(point) and not point.status == Statuses.STATION:
            points[bin_to_linear(point.x, point.y)].status = Statuses.CORRUPTED
        if INNER_RANGE < points_distance(point, chosen_point) <= OUTER_RANGE and not point.status == Statuses.STATION:
            available_points.append(point)

    for i in range(0, NUM_OF_BS - 1):
        chosen_point = choice[available_points]
        points[bin_to_linear(chosen_point.x, chosen_point.y)].status = Statuses.STATION
        for point in points:
            if points_distance(point, chosen_point) <= INNER_RANGE and not chosen_point.equals(point) and not point.status == Statuses.STATION:
                points[bin_to_linear(point.x, point.y)].status = Statuses.CORRUPTED
            if INNER_RANGE < points_distance(point, chosen_point) <= OUTER_RANGE and not point.status == Statuses.STATION:
                available_points.append(point)

        for point in available_points:
            if points[bin_to_linear(point.x, point.y)].status == Statuses.CORRUPTED or points[bin_to_linear(point.x, point.y)].status == Statuses.STATION:
                available_points.remove(point)

    for point in points:
        if point.status == Statuses.STATION:
            print(point.x, point.y)

generate_topology()