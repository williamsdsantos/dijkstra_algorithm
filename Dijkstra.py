# Dijkstra Algorithm for Optical Networks

import Topology

def Dijkstra(topology, initial):
    visited = {initial: 0}
    Route = {}

    nodes = set(topology.Nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node is visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distance[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

        print("It works")
        return visited, path
