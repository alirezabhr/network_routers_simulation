import json
import heapq

class Network:

    def shortest_path(self, routers_graph, start):
        # Create a priority queue to store the nodes to be visited
        queue = [(0, start)]

        # Create a dictionaries to store the distance from the start node and the predecessor node in the shortest path
        distances = {start: 0}
        predecessors = {start: None}

        # Create a set to store the visited nodes
        visited = set()

        while queue:
            # Extract the node with the smallest distance from the queue
            (cost, node) = heapq.heappop(queue)
            
            if node in visited:
                continue
            
            visited.add(node)

            # Update the distance of each neighboring node
            for neighbor, cost in routers_graph[node].items():
                if neighbor not in distances or distances[node] + cost < distances[neighbor]:
                    distances[neighbor] = distances[node] + cost
                    predecessors[neighbor] = node
                    heapq.heappush(queue, (distances[neighbor], neighbor))
                    
        return predecessors, distances
