from random import choice
from utils import Point
from utils import points_distance
from utils import Status


X_SIZE = 4
Y_SIZE = 4
INNER_RANGE = 1
OUTER_RANGE = 3
NUM_OF_BS = 2


def generate_topology():
    available_points = []
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
            if points[point.x][point.y].status == Status.AVAILABLE:
                available_points.append(point)

    return available_points


def go_iter(chosen_point):
    chosen_point.status = Status.STATION
    points[chosen_point.x][chosen_point.y].status = Status.STATION
    #print("station ", chosen_point.x, chosen_point.y)
    for x_row in points:
        for point in x_row:
            if points_distance(point, chosen_point) <= INNER_RANGE and not chosen_point.equals(point) and not point.status == Status.STATION:
                point.status = Status.BUSY
                points[point.x][point.y].status = Status.BUSY
                #print("busy", point.x, point.y)
            if INNER_RANGE < points_distance(point, chosen_point) <= OUTER_RANGE and not point.status == Status.STATION:
                point.status = Status.AVAILABLE
                points[point.x][point.y].status = Status.AVAILABLE


points = [[Point(i, j) for i in range(X_SIZE)] for j in range(Y_SIZE)]
generate_topology()
print("result: \n")
for x_row in points:
    for point in x_row:
        if point.status == Status.STATION:
            print("station ", point.x, point.y)

        #if point.status == Status.AVAILABLE:
        #    print("available ", point.x, point.y)

        #if point.status == Status.FREE:
        #    print("free ", point.x, point.y)

        #if point.status == Status.BUSY:
        #    print("busy ", point.x, point.y)