# Dijkstra Algorithm for Optical Networks

from Topology import Topology

class Dijkstra:
    def __init__(self, Origin, Destination):
        T = Topology()
        Route = []
        TotalWeight = 0

        for CurrentNode in T.Nodes:
            MinorWeight = []
            for CurrentLink in T.Links:
                if CurrentLink[0] == CurrentNode:
                    MinorWeight.append(CurrentLink[2])
            MinorWeight.sort()
            TotalWeight += MinorWeight[0]
