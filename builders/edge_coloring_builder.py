from networkx.algorithms import bipartite
import networkx as nx


class EdgeColoringBuilder:
    graph = nx.Graph()
    graph_edge_coloring = []

    def __init__(self, graph):
        self.graph = graph

    def color_edges_and_build_channels(self):

        def max_degree(graph):
            return max(graph.degree().values())

        def best_match(graph):
            b_m = bipartite.hopcroft_karp_matching(graph)
            return [(v, k) for k, v in b_m.items()]

        g = self.graph.copy()
        number_of_colors = max_degree(g)

        for color in range(number_of_colors):
            # print('next color')
            best_matching = best_match(g)
            # print(best_matching)
            self.graph_edge_coloring.append(best_matching)

            mydict = {}
            mydict.update(dict.fromkeys(best_matching, color))
            # print('my dict is', mydict)

            old_colors = nx.get_edge_attributes(self.graph, 'color')
            # print('old: ', old_colors)

            old_colors.update(mydict)
            # print('new: ', old_colors)

            nx.set_edge_attributes(self.graph, 'color', old_colors)
            g.remove_edges_from(best_matching)

        print("Edge coloring: " + str(self.graph_edge_coloring))
        return self.graph_edge_coloring
