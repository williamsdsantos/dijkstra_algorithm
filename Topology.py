# Topologies

class Topology:
    def __init__(self):
        Nodes = []
        Links = {}

        with open('data/topologies/P2P4', 'r') as TopologyData:
            # Reads nodes from topology FileName
            Header1 = TopologyData.readline()
            Header2 = TopologyData.readline()
            Header3 = TopologyData.readline()

            for line in TopologyData:
                Data = line.split()
                try:
                    NodeID = Data[2]
                except:
                    break

            #add_Node(self, NodeID)

            # Reads links from topology FileName
            Header4 = TopologyData.readline()
            Header5 = TopologyData.readline()
            Header6 = TopologyData.readline()

            for line in TopologyData:
                Data = line.split()
                try:
                    Origin = Data[2]
                    Destination = Data[3]
                    Length = Data[4]
                except:
                    break

            #add_Link(self, Origin, Destination, Length)

    def add_Node(self, NodeID):
        pass

    def add_Link(self, Origin, Destination, Length):
        pass
