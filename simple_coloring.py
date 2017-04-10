import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt


possible_colors = []
global_colors_counter = 0


def remove_zero_degrees(graph):
    for vertex in graph.nodes():
        if graph.degree(vertex) != 0:
            graph.remove_node(vertex)


def coloring_test(graph):
    return no_equal_colors(graph) and no_uncolored_edges(graph)


def no_equal_colors(graph):
    colors = nx.get_edge_attributes(graph, 'color')
    for vertex in graph.nodes():
        for edge1 in graph.edges(vertex):
            for edge2 in graph.edges(vertex):
                if (edge1 != edge2) and (edge1[0] != edge2[1] and edge1[1] != edge2[0]):
                    edge_to_use1 = edge1 if edge1 in colors else (edge1[1], edge1[0])
                    edge_to_use2 = edge2 if edge2 in colors else (edge2[1], edge2[0])
                    color1 = colors[edge_to_use1]
                    color2 = colors[edge_to_use2]
                    if color1 != color2:
                        return False
    return True


def no_uncolored_edges(graph):
    colors = nx.get_edge_attributes(graph, 'color')
    for edge in graph.edges():
        if edge not in colors and (edge[1], edge[0]) not in colors:
            return False
    return True


def max_degree(graph):
    return max(graph.degree().values())


def best_match(graph):
    b_m = bipartite.hopcroft_karp_matching(graph)
    return [(v, k) for k, v in b_m.items()]


def edge_coloring(graph):
    g = graph.copy()
    number_of_colors = max_degree(g)

    for color in range(number_of_colors):
        #print('next color')
        best_matching = best_match(g)
        #print(best_matching)
        possible_colors.append(best_matching)

        mydict = {}
        mydict.update(dict.fromkeys(best_matching, color))
        #print('my dict is', mydict)

        old_colors = nx.get_edge_attributes(graph, 'color')
        #print('old: ', old_colors)

        old_colors.update(mydict)
        #print('new: ', old_colors)

        nx.set_edge_attributes(graph, 'color', old_colors)
        g.remove_edges_from(best_matching)


def run(graph):
    edge_coloring(graph)

# mygraph = nx.Graph()
# mygraph = bipartite.random_graph(50, 10, 0.1)
# remove_zero_degrees(mygraph)
# set_one1, set_two2 = bipartite.sets(mygraph)
# pos1 = dict()
# pos1.update((n, (0, i*10)) for i, n in enumerate(set_one1))
# pos1.update((n, (0.5, i*10)) for i, n in enumerate(set_two2))
# nx.draw(mygraph, pos=pos1, with_labels=True)
#plt.show()

# requirements

#
# edge_coloring(mygraph)
# print('array of edges/colors', possible_colors)
# print('max degree is', max(mygraph.degree().values()))
# print('len of resulting colors', len(possible_colors))
# print(coloring_test(mygraph))
