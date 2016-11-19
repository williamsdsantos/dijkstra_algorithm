# Implements Dijsktra's Algorithm

from Dijkstra import Dijkstra

Origin = input("-> Origin Node: ")
Destination = input("-> Destination Node: ")

Route = Dijkstra(Origin, Destination)

print(Route.getRoute())
