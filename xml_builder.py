from utils import Status
import xml.etree.ElementTree as ET
from constants import *


class XmlBuilder:
    grid = []

    def __init__(self, grid):
        self.grid = grid

    def create_xml(self):
        root = ET.Element("grid")
        for i in range(X_SIZE):
            for j in range(Y_SIZE):
                if self.grid[j][i].status == Status.STATION:
                    neighbors_to_set = str(self.grid[j][i].neighbors_note_coloring)
                    id = self.grid[j][i].id()
                    ET.SubElement(root, "point", {"id": str(id),
                                                  "x_coord": str(i),
                                                  "y_coord": str(j),
                                                  "neighbors": neighbors_to_set[1:len(neighbors_to_set) - 1]})
        ET.dump(root)
        tree = ET.ElementTree(root)
        tree.write("grid.xml")