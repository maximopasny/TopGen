import networkx as nx
from networkx.algorithms import bipartite
from tools.utils import *


class NetworkXGraphBuilder:
    grid = []

    def __init__(self, grid):
        self.grid = grid

    def produce_networkx_graph(self):

        def prepare_sets(self):
            set_zero = []
            set_one = []

            for i in range(X_SIZE):
                for j in range(Y_SIZE):
                    if self.grid[j][i].status == Status.STATION:
                        if self.grid[j][i].color == Color.ZERO:
                            set_zero.append(self.grid[j][i].id())
                        else:
                            set_one.append(self.grid[j][i].id())

            return set_zero, set_one

        def add_edges(self, graph):
            for i in range(X_SIZE):
                for j in range(Y_SIZE):
                    if self.grid[j][i].status == Status.STATION:
                        station = self.grid[j][i]
                        [graph.add_edges_from([(station.id(), neighbor)])
                         for neighbor in self.grid[j][i].neighbors_note_coloring]

        graph = nx.Graph()
        set_zero, set_one = prepare_sets(self)
        graph.add_nodes_from(set_zero, bipartite=0)
        graph.add_nodes_from(set_one, bipartite=1)
        add_edges(self, graph)
        print("NetworkX bipartite validation returns: " + str(bipartite.is_bipartite(graph)))
        return graph



