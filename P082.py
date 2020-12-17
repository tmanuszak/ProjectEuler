import time
import re
from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight


def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path

start_time = time.time()

with open('p082_matrix.txt', 'r') as file:
    data = file.read()
    data = re.split(',|\n', data)
    data = data[:-1]
    file.close()

# d = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956],
#      [805, 732, 524, 37, 331]]
d = []
for i in range(0, 80):
    d.append([int(data[j]) for j in range((i * 80), ((i + 1) * 80))])

graph = Graph()
edges = []
for x in range(0, len(d)):  # create the first column of edges
    edges.append(((x), (x, 0), d[x][0]))
for x in range(0, len(d)):  # create all edges above, below, and to the right
    for y in range(0, len(d[x])):
        if x > 0:  # append edge above
            edges.append(((x, y), (x-1, y), d[x-1][y]))
        if x < len(d) - 1:  # append edge below
            edges.append(((x, y), (x+1, y), d[x+1][y]))
        if y < len(d[x]) - 1:  # append edge to the right
            edges.append(((x, y), (x, y + 1), d[x][y + 1]))
for edge in edges:
    graph.add_edge(*edge)

minsum = 1000000000000000
for start in range(0, len(d)):
    for end in range(0, len(d)):
        path = dijsktra(graph, start, (end, len(d[0]) - 1))
        minsum = min(sum([d[path[i][0]][path[i][1]] for i in range(1, len(path))]), minsum)

print(minsum)


print("--- %s seconds ---" % (time.time() - start_time))
