# Topologies

class Topology:
    def __init__(self):
        with open('/data/topologies/P2P4', 'r') as TopologyData:
            # Reads nodes from topology FileName

            add_Node(NodeID)
            # Reads links from topology FileName

            add_Link(Origin, Destination, Length)

    def add_Node(self, NodeID):
        T.Nodes.add(value)

    def add_Link(T, Origin, Destination, Length):
        T.Links[Origin].append(Destination)
        T.Links[Destination].append(Origin)
        T.Lengths[(Origin, Destination)] = Length
