from random import choice
from utils import Point
from utils import points_distance
from utils import Status


X_SIZE = 40
Y_SIZE = 40
INNER_RANGE = 5
OUTER_RANGE = 20
NUM_OF_BS = 30


def generate_topology():
    chosen_point = choice(choice(points))
    go_iter(chosen_point)
    available_points = get_available_points()
    for i in range(0, NUM_OF_BS - 1):
        iteration_step(available_points)


def iteration_step(available_points):
    chosen_point = choice(available_points)
    go_iter(chosen_point)
    available_points = get_available_points()


def get_available_points():
    available_points = []

    for x_row in points:
        for point in x_row:
            if point.status == Status.AVAILABLE:
                available_points.append(point)

    return available_points


def go_iter(chosen_point):
    chosen_point.status = Status.STATION
    for x_row in points:
        for point in x_row:
            if point.status != Status.BUSY and point.status != Status.STATION:
                distance = points_distance(point, chosen_point)
                if distance <= INNER_RANGE:
                    point.status = Status.BUSY
                if INNER_RANGE < distance <= OUTER_RANGE:
                    point.status = Status.AVAILABLE


points = [[Point(i, j) for i in range(X_SIZE)] for j in range(Y_SIZE)]
generate_topology()
print("result: \n")
count = 0
for x_row in points:
    for point in x_row:
        if point.status == Status.STATION:
            print("station: ", point.x, point.y)
            count += 1

        #if point.status == Status.AVAILABLE:
        #    print("available: ", point.x, point.y)

        #if point.status == Status.BUSY:
        #   print("busy: ", point.x, point.y)

#print(count)