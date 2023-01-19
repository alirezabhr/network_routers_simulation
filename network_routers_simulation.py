import json
import heapq

import networkx as nx
import matplotlib.pyplot as plt


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

    
    def create_routers_graph(self, predecessors, distances):
        graph = {}

        # Add graph nodes and costs
        for node, predecessor in predecessors.items():
            if node not in graph.keys():
                graph[node] = {}
            
            if predecessor is not None:
                if predecessor not in graph.keys():
                    graph[predecessor] = {node: distances[node] - distances[predecessor]}
                else:
                    graph[predecessor].update({node: distances[node] - distances[predecessor]})
                
        return graph
                

    def display_graph(self, graphs):
        for graph in graphs:
            # Create a new graph
            G = nx.DiGraph()

            # Add nodes to the graph
            for node in graph.keys():
                G.add_node(node)

            # Add edges to the graph along with their costs
            for node, neighbors in graph.items():
                for neighbor, cost in neighbors.items():
                    G.add_edge(node, neighbor, weight=cost)

            # Draw the graph
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True)
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

            plt.figure()

        plt.show()



def main():
    # Get the routers data from a json file
    f = open('routers.json')
    data = json.load(f)

    initial_routers_graph = data.get('routers')
    start_node = data.get('start')


    network = Network()

    predecessors, distances = network.shortest_path(initial_routers_graph, start_node)

    final_routers_graph = network.create_routers_graph(predecessors, distances)

    network.display_graph([initial_routers_graph, final_routers_graph])


main()
