from builders.bitmap_builder import BitmapBuilder
from builders.edge_coloring_builder import EdgeColoringBuilder
from builders.grid_builder import GridBuilder
from builders.ned_builder import NedBuilder
from builders.networkx_graph_builder import NetworkXGraphBuilder
from builders.xml_builder import XmlBuilder
from tools.utils import Point, X_SIZE, Y_SIZE

grid = [[Point(i, j) for i in range(X_SIZE)] for j in range(Y_SIZE)]
gridBuilder = GridBuilder(grid)
grid = gridBuilder.produce_grid()

bitmapBuilder = BitmapBuilder(grid)
bitmapBuilder.create_bitmap()

networkxGraphBuilder = NetworkXGraphBuilder(grid)
graph = networkxGraphBuilder.produce_networkx_graph()

edgeColoringBuilder = EdgeColoringBuilder(graph)
channels = edgeColoringBuilder.color_edges_and_build_channels()

xmlBuilder = XmlBuilder(grid, channels)
xmlBuilder.create_xml()

nedBuilder = NedBuilder(grid, graph, channels)
nedBuilder.produce_ned_configuration()





