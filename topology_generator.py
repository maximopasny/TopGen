from utils import Point
from constants import *
from grid_builder import GridBuilder
from bitmap_builder import BitmapBuilder
from xml_builder import XmlBuilder
from networkx_graph_builder import NetworkXGraphBuilder

grid = [[Point(i, j) for i in range(X_SIZE)] for j in range(Y_SIZE)]
gridBuilder = GridBuilder(grid)
grid = gridBuilder.produce_grid()

bitmapBuilder = BitmapBuilder(grid)
bitmapBuilder.create_bitmap()

networkxGraphBuilder = NetworkXGraphBuilder(grid)
networkxGraphBuilder.produce_networkx_graph()

xmlBuilder = XmlBuilder(grid)
xmlBuilder.create_xml()





