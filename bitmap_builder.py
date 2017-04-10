from utils import Status
from PIL import Image
from constants import *


class BitmapBuilder:
    grid = []

    def __init__(self, grid):
        self.grid = grid

    def create_bitmap(self):
        img = Image.new('RGB', (X_SIZE, Y_SIZE), "black")  # create a new black image
        pixels = img.load()  # create the pixel map

        for i in range(X_SIZE):  # for every pixel:
            for j in range(Y_SIZE):
                if self.grid[j][i].status == Status.STATION:
                    pixels[i, j] = (255, 0, 0)  # red
                elif self.grid[j][i].status == Status.BUSY:
                    pixels[i, j] = (0, 0, 255)  # blue
                elif self.grid[j][i].status == Status.AVAILABLE:
                    pixels[i, j] = (0, 255, 0)  # green
                else:
                    pixels[i, j] = (0, 0, 0)  # black
        print("BitmapBuilder is ready to produce image.")
        img.show()
