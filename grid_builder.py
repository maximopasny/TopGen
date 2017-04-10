from random import choice, random
from utils import points_distance, Color, linear_to_dual
from utils import Status
from constants import *


class GridBuilder:

    grid = []

    def __init__(self, grid):
        self.grid = grid

    def produce_grid(self):
        self.place_stations_opt()
        self.choose_random_vertex_color()
        self.manage_neighbors_with_coloring()
        self.validator()
        return self.grid

    def place_stations_opt(self):
        chosen_point = choice(choice(self.grid))
        chosen_point.status = Status.AVAILABLE
        for i in range(0, NUM_OF_BS):
            available_points = self.get_available_points()
            chosen_point = choice(available_points)
            self.update_points_status_opt(chosen_point)

    def get_available_points(self):
        available_points = []
        for x_row in self.grid:
            for point in x_row:
                if point.status == Status.AVAILABLE:
                    available_points.append(point)
        return available_points

    def update_points_status_opt(self, chosen_point):
        chosen_point.status = Status.STATION

        upper_index = chosen_point.y - INNER_RANGE
        bottom_index = chosen_point.y + INNER_RANGE
        left_index = chosen_point.x - INNER_RANGE
        right_index = chosen_point.x + INNER_RANGE

        upper_index = (upper_index if upper_index > 0 else 0)
        bottom_index = (bottom_index if bottom_index < Y_SIZE else Y_SIZE)
        left_index = (left_index if left_index > 0 else 0)
        right_index = (right_index if right_index > X_SIZE else X_SIZE)

        for x_row in self.grid[upper_index: bottom_index]:
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
                        point.neighbors_ignore_coloring.append(chosen_point.id())
                        chosen_point.neighbors_ignore_coloring.append(chosen_point.id())

    def validator(self):
        stations = []
        for i in range(X_SIZE):
            for j in range(Y_SIZE):
                if self.grid[j][i].status == Status.STATION:
                    stations.append(self.grid[j][i])
        distances = []
        for station in stations:
            stations.remove(station)
            for measured_station in stations:
                distances.append(points_distance(station, measured_station))
        distances.sort()
        #print(distances)
        if distances[0] < INNER_RANGE:
            print("Grid builder failed to generate.")
        else:
            print("Grid was successfully generated.")

    def manage_neighbors_with_coloring(self):

        def process_coloring(self, iterpoint_coordinate, station_color):
            (x, y) = linear_to_dual(iterpoint_coordinate)
            iterpoint_object = self.grid[x][y]
            return station_color != iterpoint_object.color

        for i in range(X_SIZE):
            for j in range(Y_SIZE):
                if self.grid[j][i].status == Status.STATION:
                    station = self.grid[j][i]
                    id = station.id()
                    neighbors_points = station.neighbors_ignore_coloring
                    neighbors_points.remove(id)
                    neighbors_points = list(set(neighbors_points))
                    station.neighbors_ignore_coloring = neighbors_points
                    neighbors_can_have_edges = [iterpoint_coordinate for iterpoint_coordinate in neighbors_points
                                                if process_coloring(self, iterpoint_coordinate, station.color)]
                    station.neighbors_note_coloring = neighbors_can_have_edges

    def choose_random_vertex_color(self):
        for i in range(X_SIZE):
            for j in range(Y_SIZE):
                if self.grid[j][i].status == Status.STATION:
                    self.grid[j][i].color = choice([Color.ZERO, Color.ONE])
