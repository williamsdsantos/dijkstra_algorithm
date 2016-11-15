# Topologies

class Topology:
    def __init__(self):
        with open('data/topologies/P2P4', 'r') as TopologyData:
            # Reads nodes from topology FileName
            Header1 = TopologyData.readline()
            Header2 = TopologyData.readline()
            Header3 = TopologyData.readline()

            for line in TopologyData:
                Data = line.split()
                try:
                    NodeID = Data[2]
                    print(NodeID)
                except:
                    break

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
                    print(Origin, Destination, Length)
                except:
                    break
