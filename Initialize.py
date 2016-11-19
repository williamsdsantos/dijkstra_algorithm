# Implements Dijsktra's Algorithm

from Dijkstra import Dijkstra

Origin = input("-> Origin's Node: ")
Destination = input("-> Destination's Node: ")

Route = Dijkstra(Origin, Destination)

print(Route.getRoute())
