import string

from tools.constants import X_SIZE, Y_SIZE
from tools.utils import Status


class NedBuilder:
    grid = []
    graph = []
    channels = []

    def __init__(self, grid, graph, channels):
        self.grid = grid
        self.graph = graph
        self.channels = channels

    def produce_ned_configuration(self):

        def produce_nodes(self):
            nodes_declarations_strings = ""
            for i in range(X_SIZE):
                for j in range(Y_SIZE):
                    if self.grid[j][i].status == Status.STATION:
                        point_object = self.grid[j][i]
                        id = point_object.id()
                        color = point_object.color
                        name = "coloredNode" + "_" + str(id)
                        x = point_object.x
                        y = point_object.y
                        nodes_declarations_strings += "\t\t" + name + ": ColoredNode {\n" \
                                                      + "\t\t\tparameters:\n" \
                                                      + "\t\t\t\tid = " + str(id) + ";\n" \
                                                      + "\t\t\t\tvertex_color = " + str(color) + ";\n" \
                                                      + "\t\t\t\tx = " + str(x) + ";\n" \
                                                      + "\t\t\t\ty = " + str(y) + ";\n" \
                                                      + "\t\t}\n"
            return nodes_declarations_strings

        def produce_channels(self):
            channels_declarations_strings = ""
            channels_ned_names = list(string.ascii_uppercase)
            i = 0
            for channel in self.channels:
                channels_declarations_strings += ("\t\tchannel " + channels_ned_names[i] + " extends ColoredChannel {\n"
                                                  + "\t\t\tcolor = " + str(i)
                                                  + ";\n\t\t}\n")
                i += 1

            # in order to produce control channel
            channels_declarations_strings += ("\t\tchannel CONTROL_CHANNEL extends ned.IdealChannel {\n"
                                              + "\n\t\t}\n")
            return channels_declarations_strings

        def produce_manager(self):
            numberOfEdgeColors = len(self.channels)
            manager_declaration_string = "\t\t" + "managerNode: Manager {\n" \
                                         + "\t\t\tslotDuration = 1;\n" \
                                         + "\t\t\tnumberOfEdgeColors = " + str(numberOfEdgeColors) + ";\n" \
                                         + "\t\t\tnumberOfStations = " + str(len(self.graph.node)) + ";\n" \
                                         + "\t\t}\n"
            return manager_declaration_string

        def produce_connections(self):
            connections_declarations_strings = ""
            i = 0
            channels_ned_names = list(string.ascii_uppercase)
            for same_colored_channels in self.channels:
                for concrete_connection in same_colored_channels:
                    connections_declarations_strings += ("\t\t\tcoloredNode_" + str(concrete_connection[0])
                                                         + ".out++" + " --> " + channels_ned_names[
                                                             i] + " --> "
                                                         + "coloredNode_" + str(
                        concrete_connection[1]) + ".in++;\n")
                i += 1

            for node in self.graph.node:
                connections_declarations_strings += ("\t\t\tmanagerNode"
                                                     + ".out++" + " --> CONTROL_CHANNEL --> "
                                                     + "coloredNode_" + str(node)
                                                     + ".in++;\n")
            return connections_declarations_strings

        f = open('attempt.ned', 'w')
        header = "package topology_gen_stuff.simulations;\nimport topology_gen_stuff.ColoredNode;\n" + \
            "import topology_gen_stuff.ColoredChannel;\nimport topology_gen_stuff.Manager;\n\n"

        channels_declarations_string = produce_channels(self)
        manager_declaration_string = produce_manager(self)
        nodes_declarations_string = produce_nodes(self)
        connections_declarations_string = produce_connections(self)

        f.write(header +
                'network Network\n' +
                '{\n' +
                '\ttypes:\n' +
                channels_declarations_string +
                '\n\tsubmodules:\n' +
                manager_declaration_string +
                nodes_declarations_string +
                '\n\tconnections:\n' +
                connections_declarations_string +
                '}\n')

# network Network
# {
#     types:
#         channel C extends ned.DatarateChannel {
#             datarate = 100Mbps;
#         }
#     submodules:
#         node1: Node;
#         node2: Node;
#         node3: Node;
#         ...
#     connections:
#         node1.port++ <--> C <--> node2.port++;
#         node2.port++ <--> C <--> node4.port++;
#         node4.port++ <--> C <--> node6.port++;
#         ...
# }
