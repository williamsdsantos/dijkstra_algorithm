# Dijkstra Algorithm for Optical Networks

from Topology import Topology
from operator import itemgetter

class Dijkstra:
    def __init__(self, Origin, Destination):
        T = Topology()
        self.Route = []
        VisitedNodes = []
        CurrentNode = Origin

        while T.Nodes:
            MinorLength = []
            for CurrentLink in T.Links:
                if CurrentLink[0] == CurrentNode:
                    MinorLength.append(CurrentLink)

            MinorLength = sorted(MinorLength, key=itemgetter(2))

            while True:
                if MinorLength[0][1] in VisitedNodes:
                    del MinorLength[0]
                else:
                    VisitedNodes.append(MinorLength[0][0])
                    self.Route.append(MinorLength[0])
                    CurrentNode = self.Route[-1][1]
                    break

            if CurrentNode == Destination:
                break

    def getRoute(self):
        return self.Route
