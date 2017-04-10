import networkx as nx
import itertools
import networkx.algorithms.bipartite as bipartite


def remove_zero_degrees(graph):
    for vertex in graph.nodes():
        if graph.degree(vertex) is 0:
            graph.remove_node(vertex)


def generate_bipartite_graphs(mygraph):

    possible_vertex_colors = itertools.combinations([True, False], num_of_vertices)
    vertices = mygraph.nodes()

    for vector in possible_vertex_colors:
        set_one, set_two = [], []
        for i in range(0, num_of_vertices):
            if vector[i] is True:
                set_one.append(vertices[i])
            else:
                set_two.append(vertices[i])

        new_graph = nx.Graph()
        appropriate_edges = []
        inappropriate_edges = []

        for edge in mygraph.edges():
            if (edge[0] in set_one and edge[1] in set_two) or (edge[1] in set_one and edge[0] in set_two):
                appropriate_edges.append(edge)
            else:
                inappropriate_edges.append(edge)

        new_graph.add_nodes_from(set_one, bipartite=0)
        new_graph.add_nodes_from(set_two, bipartite=1)
        new_graph.add_edges_from(appropriate_edges)
        remove_zero_degrees(new_graph)

        assert bipartite.is_bipartite(new_graph)
        graphs.append(new_graph)
        unused_edges.append(inappropriate_edges)


def find_optimal_vertex_coloring(graphs):
    for i in range(0, len(graphs)):
        graph = graphs[i]
        degrees = graph.degree()
        max_degree = max(degrees)
        mean_degree = sum(degrees) / len(degrees)
        metrics = max_degree - mean_degree
        if metrics < optimal_graph_index[1]:
            optimal_graph_index[0] = i
            optimal_graph_index[1] = metrics


graphs = []
unused_edges = []
num_of_vertices = 100
num_of_edges = 10000
optimal_graph_index = [0, num_of_edges]
mygraph = nx.gnm_random_graph(num_of_vertices, num_of_edges)
remove_zero_degrees(mygraph)
generate_bipartite_graphs(mygraph)
num_of_steps = 3