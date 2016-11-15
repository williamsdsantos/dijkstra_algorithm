# Implements Dijsktra's Algorithm

from Dijkstra import Dijkstra
# from Topology import Topology

Origin = input("-> Origin's Node: ")
Destination = input("-> Destination's Node:")

Route = Dijkstra(Origin, Destination)
print(Route)
