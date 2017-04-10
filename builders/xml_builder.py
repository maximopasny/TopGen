import xml.etree.ElementTree as ET
from tools.constants import X_SIZE, Y_SIZE
from tools.utils import Status


class XmlBuilder:
    grid = []
    channels = []

    def __init__(self, grid, channels):
        self.grid = grid
        self.channels = channels


    def create_xml(self):
        topology = ET.Element("topology")
        grid = ET.SubElement(topology, "grid")
        channels = ET.SubElement(topology, "channels")
        for i in range(X_SIZE):
            for j in range(Y_SIZE):
                if self.grid[j][i].status == Status.STATION:
                    point_object = self.grid[j][i]
                    neighbors_to_set = str(point_object.neighbors_note_coloring)
                    id = point_object.id()
                    color = point_object.color
                    ET.SubElement(grid, "point", {"id": str(id),
                                                  "x_coord": str(i),
                                                  "y_coord": str(j),
                                                  "color": str(color),
                                                  "neighbors": neighbors_to_set[1:len(neighbors_to_set) - 1]})
        i = 0
        for channel in self.channels:
            ET.SubElement(channels, "channel", {
                "connetions": str(channel),
                "channel_color": str(i)
            })
            i += 1

        ET.dump(topology)
        tree = ET.ElementTree(topology)
        tree.write("topology.xml")
