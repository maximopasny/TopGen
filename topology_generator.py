from random import choice
from utils import Point
from utils import points_distance
from utils import Status
from PIL import Image
import xml.etree.ElementTree as ET
import time
from constants import *


def place_stations_opt(grid):
    chosen_point = choice(choice(grid))
    chosen_point.status = Status.AVAILABLE
    for i in range(0, NUM_OF_BS):
        available_points = get_available_points(grid)
        chosen_point = choice(available_points)
        update_points_status_opt(chosen_point, grid)


def place_stations(grid):
    chosen_point = choice(choice(grid))
    chosen_point.status = Status.AVAILABLE
    for i in range(0, NUM_OF_BS):
        available_points = get_available_points(grid)
        chosen_point = choice(available_points)
        update_points_status(chosen_point, grid)


def get_available_points(grid):
    available_points = []
    for x_row in grid:
        for point in x_row:
            if point.status == Status.AVAILABLE:
                available_points.append(point)
    return available_points


def update_points_status(chosen_point, grid):
    chosen_point.status = Status.STATION
    for x_row in grid:
        for point in x_row:
            if point.status != Status.BUSY and point.status != Status.STATION:
                distance = points_distance(point, chosen_point)
                if distance <= INNER_RANGE:
                    point.status = Status.BUSY
                if INNER_RANGE < distance <= OUTER_RANGE:
                    point.status = Status.AVAILABLE

            if point.status == Status.STATION:
                distance = points_distance(point, chosen_point)
                if distance <= OUTER_RANGE:
                    point.neighbors.append(chosen_point.id())
                    chosen_point.neighbors.append(chosen_point.id())


def update_points_status_opt(chosen_point, grid):
    chosen_point.status = Status.STATION

    upper_index = chosen_point.y - INNER_RANGE
    bottom_index = chosen_point.y + INNER_RANGE
    left_index = chosen_point.x - INNER_RANGE
    right_index = chosen_point.x + INNER_RANGE

    upper_index = (upper_index if upper_index > 0 else 0)
    bottom_index = (bottom_index if bottom_index < Y_SIZE else Y_SIZE)
    left_index = (left_index if left_index > 0 else 0)
    right_index = (right_index if right_index > X_SIZE else X_SIZE)

    for x_row in grid[upper_index: bottom_index]:
        for point in x_row[left_index: right_index]:
            if point.status != Status.BUSY and point.status != Status.STATION:
                distance = points_distance(point, chosen_point)
                if distance <= INNER_RANGE:
                    point.status = Status.BUSY
                if INNER_RANGE < distance <= OUTER_RANGE:
                    point.status = Status.AVAILABLE

            if point.status == Status.STATION:
                distance = points_distance(point, chosen_point)
                if distance <= OUTER_RANGE:
                    point.neighbors.append(chosen_point.id())
                    chosen_point.neighbors.append(chosen_point.id())


def validator(grid):
    stations = []
    for i in range(X_SIZE):
        for j in range(Y_SIZE):
            if grid[j][i].status == Status.STATION:
                stations.append(grid[j][i])
    distances = []
    for station in stations:
        stations.remove(station)
        for measured_station in stations:
            distances.append(points_distance(station, measured_station))
    distances.sort()
    print(distances)
    if distances[0] < INNER_RANGE:
        print("fail")
    else:
        print("success")


def create_bitmap(grid):
    img = Image.new('RGB', (X_SIZE, Y_SIZE), "black")  # create a new black image
    pixels = img.load()  # create the pixel map

    for i in range(X_SIZE):  # for every pixel:
        for j in range(Y_SIZE):
            if grid[j][i].status == Status.STATION:
                pixels[i, j] = (255, 0, 0)  # red
            elif grid[j][i].status == Status.BUSY:
                pixels[i, j] = (0, 0, 255)  # blue
            elif grid[j][i].status == Status.AVAILABLE:
                pixels[i, j] = (0, 255, 0)  # green
            else:
                pixels[i, j] = (0, 0, 0)    # black

    img.show()


def create_xml(grid):
    root = ET.Element("grid")
    for i in range(X_SIZE):
        for j in range(Y_SIZE):
            if grid[j][i].status == Status.STATION:
                id = grid[j][i].id()
                neighbors_points = grid[j][i].neighbors
                neighbors_to_set = str(neighbors_points)
                ET.SubElement(root, "point", {"id": str(id),
                                              "x_coord": str(i),
                                              "y_coord": str(j),
                                              "neighbors": neighbors_to_set[1:len(neighbors_to_set) - 1]})
    ET.dump(root)
    tree = ET.ElementTree(root)
    tree.write("grid.xml")


grid = [[Point(i, j) for i in range(X_SIZE)] for j in range(Y_SIZE)]
start_time = time.time()
place_stations_opt(grid)
total_time = time.time() - start_time
print(total_time)
create_bitmap(grid)
create_xml(grid)
validator(grid)
