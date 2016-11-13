# Topologies

class Topology:
    def __init__(self):
        self.Nodes = set()
        self.Links = default(list)
        self.Lengths = {}

    def add_Node(self, NodeID):
        self.Nodes.add(value)

    def add_Link(self, Origin, Destination, Length):
        self.Links[Origin].append(Destination)
        self.Links[Destination].append(Origin)
        self.Lengths[(Origin, Destination)] = Length
