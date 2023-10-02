# Depth-First Search (DFS)
# DFS is a strategy that  expands a deepest node first before backtracking. It starts at the root and explores as far as possible along each branch before retreating. DFS is particularly useful for tasks that benefit from visiting nodes far away from the root quickly, such as finding a solution to a maze or a puzzle.
# DFS uses a stack to keep track of the nodes that have been visited but not yet explored. In a tree search, DFS visits each node once, while in a graph search, it may visit nodes multiple times if they can be reached by different paths.
# DFS is complete, meaning that it will find a solution if one exists, but it is not guaranteed to find the optimal solution.

# Breadth-First Search (BFS)
# BFS is a strategy that expands the shallowest node first before moving on to nodes at the next depth level. It starts at the root and inspects all the neighboring nodes. Then for each of those neighbor nodes in turn, it inspects their neighbor nodes which are two steps away from the root, and so on.
# BFS uses a queue to keep track of the nodes that have been visited but not yet explored. In both tree and graph search, BFS visits each node once.
# BFS is complete and optimal, meaning that it will always find the shortest path to the goal node if one exists.

# Uniform Cost Search (UCS)
# UCS is a search algorithm used for traversing a weighted tree or graph. It focuses on finding the path with the lowest total cost ( the node with the least path cost (i.e., the shortest path) is selected for expansion).
# UCS uses a priority queue as its agenda, it always expands the lowest-cost node on the fringe of the search. In both tree and graph search, UCS can handle weighted edges and can find the lowest-cost path to a goal.
# UCS is complete and optimal, meaning that it will always find the shortest path to the goal node if one exists.


# Greedy Search
# Greedy search selects the next node based solely on a heuristic or estimated cost to the goal. The heuristic could be straight-line distance to the goal in a navigation problem, for example.It uses a priority queue and selects the node with the highest value (as determined by a heuristic function) for expansion. This search is 'greedy' because it makes the locally optimal choice at each decision point with the hope that these local decisions lead to a global optimum.
# It does not keep track of the nodes that it has already visited, so it is not guaranteed to find a solution or an optimal solution.



# A* Search
# A* search is a best-first search algorithm that finds the least-cost path from a given initial node to one goal node (out of one or more possible goals). It uses a heuristic to estimate the cost to reach the goal from a given node and also calculates the cost to reach that node from the start. It then gives priority to nodes with the lowest sum of both costs.
# A* uses a priority queue and always selects the node with the lowest f(n) = g(n) + h(n) for expansion, where g(n) is the actual cost from the start to node n, and h(n) is the heuristic estimate of the cost from node n to the goal. A* is complete and optimal, given certain conditions on the heuristic.








from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_nodes_from(["S", "A", "B", "C", "D", "G"])
G.add_edges_from([("S", "A"), ("S", "B"), ("A", "B"), ("A", "C"), ("B", "C"), ("C", "D"), ("C", "G"), ("D", "G")])

print(G)

# Find the shortest path between node `S` and node `G`.
shortest_path = nx.shortest_path(G, "S", "G")

print( shortest_path)

# Visualize the graph.
 

nx.draw(G, with_labels=True)
plt.show()


# Define the graph as a dictionary with nodes and their edge costs
graph = {
    'S': {'A': 3, 'B': 1},
    'A': {'B': 2, 'C': 2},
    'B': {'C': 3},
    'C': {'D': 4, 'G': 4},
    'D': {'G': 1},
    'G': {}
}

# Define heuristic values for each node
heuristics = {
    'S': 7,
    'A': 5,
    'B': 7,
    'C': 4,
    'D': 1,
    'G': 0
}

# Define the start and target nodes
start_node = 'S'
target_node = 'G'

print("-------QN3: search strategies using for tree search----------")

# Depth-First Search

def depth_first_search(graph, start, target):
    stack = [(start, [start])]
    visited = set() 
    while stack:
        (node, path) = stack.pop()
        visited.add(node) 
        if node == target:
            return path
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in path and neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

dfs_path = depth_first_search(graph, start_node, target_node)
print("DFS Path:", dfs_path)

# Breadth-First Search
def breadth_first_search(graph, start, target):
    queue = [(start, [start])]
    visited = set()  
    while queue:
        (node, path) = queue.pop(0)
        visited.add(node) 
        if node == target:
            return path
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in path and neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

bfs_path = breadth_first_search(graph, start_node, target_node)
print("BFS Path:", bfs_path)

# Uniform Cost Search
def uniform_cost_search(graph, start, target):
    priority_queue = [(0, start, [start])]
    visited = set()  
    while priority_queue:
        (cost, node, path) = priority_queue.pop(0)
        visited.add(node) 
        if node == target:
            return path
        neighbors = graph[node]
        for neighbor, neighbor_cost in neighbors.items():
            if neighbor not in path and neighbor not in visited:
                new_cost = cost + neighbor_cost
                priority_queue.append((new_cost, neighbor, path + [neighbor]))
                priority_queue.sort(key=lambda x: x[0])

ucs_path = uniform_cost_search(graph, start_node, target_node)
print("UCS Path:", ucs_path)

# Greedy Search
def greedy_search(graph, start, target, heuristics):
    priority_queue = [(heuristics[start], start, [start])]
    visited = set()  
    while priority_queue:
        (_, node, path) = priority_queue.pop(0)
        visited.add(node)  
        if node == target:
            return path
        neighbors = graph[node]
        for neighbor in sorted(neighbors, key=lambda x: heuristics[x]):
            if neighbor not in path and neighbor not in visited:
                priority_queue.append((heuristics[neighbor], neighbor, path + [neighbor]))
                priority_queue.sort(key=lambda x: x[0])

greedy_path = greedy_search(graph, start_node, target_node, heuristics)
print("Greedy Search Path:", greedy_path)

# A* Search
def a_star_search(graph, start, target, heuristics):
    priority_queue = [(heuristics[start], 0, start, [start])]
    visited = set()  
    while priority_queue:
        (_, cost, node, path) = priority_queue.pop(0)
        visited.add(node)  
        if node == target:
            return path
        neighbors = graph[node]
        for neighbor, neighbor_cost in sorted(neighbors.items(), key=lambda x: heuristics[x[0]]):
            if neighbor not in path and neighbor not in visited:
                new_cost = cost + neighbor_cost
                priority_queue.append((new_cost + heuristics[neighbor], new_cost, neighbor, path + [neighbor]))
                priority_queue.sort(key=lambda x: x[0])

a_star_path = a_star_search(graph, start_node, target_node, heuristics)
print("A* Search Path:", a_star_path)



print("------------------QN4: search strategies using for GRAPH search------------------------")
def depth_first_search(graph, start, target):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        if node == target:
            return path
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))

dfs_path = depth_first_search(graph, start_node, target_node)
print("DFS Path:", dfs_path)


def breadth_first_search(graph, start, target):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        if node == target:
            return path
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

bfs_path = breadth_first_search(graph, start_node, target_node)
print("BFS Path:", bfs_path)



def uniform_cost_search(graph, start, target):
    priority_queue = [(0, start, [start])]
    while priority_queue:
        (cost, node, path) = priority_queue.pop(0)
        if node == target:
            return path
        neighbors = graph[node]
        for neighbor, neighbor_cost in neighbors.items():
            if neighbor not in path:
                new_cost = cost + neighbor_cost
                priority_queue.append((new_cost, neighbor, path + [neighbor]))
                priority_queue.sort(key=lambda x: x[0])

ucs_path = uniform_cost_search(graph, start_node, target_node)
print("UCS Path:", ucs_path)


 



def greedy_search(graph, start, target, heuristics):
    priority_queue = [(heuristics[start], start, [start])]
    while priority_queue:
        (_, node, path) = priority_queue.pop(0)
        if node == target:
            return path
        neighbors = graph[node]
        for neighbor, _ in sorted(neighbors.items(), key=lambda x: heuristics[x[0]]):
            if neighbor not in path:
                priority_queue.append((heuristics[neighbor], neighbor, path + [neighbor]))
                priority_queue.sort(key=lambda x: x[0])
greedy_path = greedy_search(graph, start_node, target_node, heuristics)
print("Greedy Search Path:", greedy_path)



def a_star_search(graph, start, target, heuristics):
    priority_queue = [(heuristics[start], 0, start, [start])]
    while priority_queue:
        (_, cost, node, path) = priority_queue.pop(0)
        if node == target:
            return path
        neighbors = graph[node]
        for neighbor, neighbor_cost in sorted(neighbors.items(), key=lambda x: heuristics[x[0]]):
            if neighbor not in path:
                new_cost = cost + neighbor_cost
                priority_queue.append((new_cost + heuristics[neighbor], new_cost, neighbor, path + [neighbor]))
                priority_queue.sort(key=lambda x: x[0])

a_star_path = a_star_search(graph, start_node, target_node, heuristics)
print("A* Search Path:", a_star_path)


print("------------QN5:print out the order in which states are expanded, the path returned by tree search, as well as the states that are not expanded.------------")

def tree_depth_first_search(graph, start, target):
    stack = [(start, [start])]
    expanded_states = []  # To store the order of expanded states
    while stack:
        (node, path) = stack.pop()
        expanded_states.append(node)  # Add the expanded state to the list
        if node == target:
            return expanded_states, path
        neighbors = graph[node]
        for neighbor in sorted(neighbors, reverse=True):  # Break ties alphabetically by reversing the order
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))


def tree_breadth_first_search(graph, start, target):
    queue = [(start, [start])]
    expanded_states = []  # To store the order of expanded states
    while queue:
        (node, path) = queue.pop(0)
        expanded_states.append(node)  # Add the expanded state to the list
        if node == target:
            return expanded_states, path
        neighbors = graph[node]
        for neighbor in sorted(neighbors):  # Break ties alphabetically
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))


def tree_uniform_cost_search(graph, start, target):
    priority_queue = [(0, start, [start])]
    expanded_states = []  # To store the order of expanded states
    while priority_queue:
        (cost, node, path) = priority_queue.pop(0)
        expanded_states.append(node)  # Add the expanded state to the list
        if node == target:
            return expanded_states, path
        neighbors = graph[node]
        for neighbor, neighbor_cost in sorted(neighbors.items()):  # Break ties alphabetically
            if neighbor not in path:
                new_cost = cost + neighbor_cost
                priority_queue.append((new_cost, neighbor, path + [neighbor]))
                priority_queue.sort(key=lambda x: (x[0], x[1]))  # Sort by cost and then by name

def tree_greedy_search(graph, start, target, heuristics):
    priority_queue = [(heuristics[start], start, [start])]
    expanded_states = []  # To store the order of expanded states
    while priority_queue:
        (_, node, path) = priority_queue.pop(0)
        expanded_states.append(node)  # Add the expanded state to the list
        if node == target:
            return expanded_states, path
        neighbors = graph[node]
        for neighbor in sorted(neighbors, key=lambda x: heuristics[x]):  # Break ties alphabetically based on heuristic value
            if neighbor not in path:
                priority_queue.append((heuristics[neighbor], neighbor, path + [neighbor]))
                priority_queue.sort(key=lambda x: (x[0], x[1]))  # Sort by heuristic and then by name

def tree_a_star_search(graph, start, target, heuristics):
    priority_queue = [(heuristics[start], 0, start, [start])]
    expanded_states = []  # To store the order of expanded states
    while priority_queue:
        (_, cost, node, path) = priority_queue.pop(0)
        expanded_states.append(node)  # Add the expanded state to the list
        if node == target:
            return expanded_states, path
        neighbors = graph[node]
        for neighbor, neighbor_cost in sorted(neighbors.items(), key=lambda x: heuristics[x[0]]):  # Break ties alphabetically based on heuristic value
            if neighbor not in path:
                new_cost = cost + neighbor_cost
                priority_queue.append((heuristics[neighbor], new_cost, neighbor, path + [neighbor]))
                priority_queue.sort(key=lambda x: (x[0], x[1]))  # Sort by heuristic and then by name

# Test the custom search algorithms
start_node = 'S'
target_node = 'G'

# Depth-First Search
expanded_states_dfs, dfs_path =  tree_depth_first_search( graph,  start_node,  target_node)
print("DFS Expanded States:", expanded_states_dfs)
print("DFS Path:", dfs_path)
print("DFS States Not Expanded:", [node for node in  graph if node not in expanded_states_dfs])

# Breadth-First Search
expanded_states_bfs, bfs_path = tree_breadth_first_search( graph,  start_node,  target_node)
print("\nBFS Expanded States:", expanded_states_bfs)
print("BFS Path:", bfs_path)
print("BFS States Not Expanded:", [node for node in  graph if node not in expanded_states_bfs])

# Uniform Cost Search
expanded_states_ucs, ucs_path =  tree_uniform_cost_search( graph,  start_node,  target_node)
print("\nUCS Expanded States:", expanded_states_ucs)
print("UCS Path:", ucs_path)
print("UCS States Not Expanded:", [node for node in  graph if node not in expanded_states_ucs])

# Greedy Search
expanded_states_greedy, greedy_path =  tree_greedy_search( graph,  start_node,  target_node,  heuristics)
print("\nGreedy Search Expanded States:", expanded_states_greedy)
print("Greedy Search Path:", greedy_path)
print("Greedy Search States Not Expanded:", [node for node in  graph if node not in expanded_states_greedy])

# A* Search
expanded_states_a_star, a_star_path =  tree_a_star_search( graph,  start_node,  target_node,  heuristics)
print("\nA* Search Expanded States:", expanded_states_a_star)
print("A* Search Path:", a_star_path)
print("A* Search States Not Expanded:", [node for node in  graph if node not in expanded_states_a_star])


print("----QN 6:print out the order in which states are expanded, the path returned by graph search, as well as the states that are not expanded. -----")

def graph_depth_first_search(graph, start, target):
    stack = [(start, [start])]
    visited_nodes = set()  # To keep track of visited nodes
    expanded_states = []  # To store the order of expanded states
    while stack:
        (node, path) = stack.pop()
        visited_nodes.add(node)  # Mark the current node as visited
        expanded_states.append(node)  # Add the expanded state to the list
        if node == target:
            return expanded_states, path
        neighbors = graph[node]
        for neighbor in sorted(neighbors, reverse=True):  # Break ties alphabetically by reversing the order
            if neighbor not in path and neighbor not in visited_nodes:
                stack.append((neighbor, path + [neighbor]))

def graph_breadth_first_search(graph, start, target):
    queue = [(start, [start])]
    visited_nodes = set()  # To keep track of visited nodes
    expanded_states = []  # To store the order of expanded states
    while queue:
        (node, path) = queue.pop(0)
        visited_nodes.add(node)  # Mark the current node as visited
        expanded_states.append(node)  # Add the expanded state to the list
        if node == target:
            return expanded_states, path
        neighbors = graph[node]
        for neighbor in sorted(neighbors):  # Break ties alphabetically
            if neighbor not in path and neighbor not in visited_nodes:
                queue.append((neighbor, path + [neighbor]))

def graph_uniform_cost_search(graph, start, target):
    priority_queue = [(0, start, [start])]
    visited_nodes = set()  # To keep track of visited nodes
    expanded_states = []  # To store the order of expanded states
    while priority_queue:
        (cost, node, path) = priority_queue.pop(0)
        visited_nodes.add(node)  # Mark the current node as visited
        expanded_states.append(node)  # Add the expanded state to the list
        if node == target:
            return expanded_states, path
        neighbors = graph[node]
        for neighbor, neighbor_cost in sorted(neighbors.items()):  # Break ties alphabetically
            if neighbor not in path and neighbor not in visited_nodes:
                new_cost = cost + neighbor_cost
                priority_queue.append((new_cost, neighbor, path + [neighbor]))
                priority_queue.sort(key=lambda x: (x[0], x[1]))  # Sort by cost and then by name

def graph_greedy_search(graph, start, target, heuristics):
    priority_queue = [(heuristics[start], start, [start])]
    visited_nodes = set()  # To keep track of visited nodes
    expanded_states = []  # To store the order of expanded states
    while priority_queue:
        (_, node, path) = priority_queue.pop(0)
        visited_nodes.add(node)  # Mark the current node as visited
        expanded_states.append(node)  # Add the expanded state to the list
        if node == target:
            return expanded_states, path
        neighbors = graph[node]
        for neighbor in sorted(neighbors, key=lambda x: heuristics[x]):  # Break ties alphabetically based on heuristic value
            if neighbor not in path and neighbor not in visited_nodes:
                priority_queue.append((heuristics[neighbor], neighbor, path + [neighbor]))
                priority_queue.sort(key=lambda x: (x[0], x[1]))  # Sort by heuristic and then by name
 
def graph_a_star_search(graph, start, target, heuristics):
    priority_queue = [(heuristics[start], 0, start, [start])]
    visited_nodes = set()  # To keep track of visited nodes
    expanded_states = []  # To store the order of expanded states
    while priority_queue:
        (_, cost, node, path) = priority_queue.pop(0)
        visited_nodes.add(node)  # Mark the current node as visited
        expanded_states.append(node)  # Add the expanded state to the list
        if node == target:
            return expanded_states, path
        neighbors = graph[node]
        for neighbor, neighbor_cost in sorted(neighbors.items(), key=lambda x: heuristics[x[0]]):  # Break ties alphabetically based on heuristic value
            if neighbor not in path and neighbor not in visited_nodes:
                new_cost = cost + neighbor_cost
                priority_queue.append((heuristics[neighbor], new_cost, neighbor, path + [neighbor]))
                priority_queue.sort(key=lambda x: (x[0], x[1]))  # Sort by heuristic and then by name


# Depth-First Search
expanded_states_dfs, dfs_path = graph_depth_first_search(graph, start_node, target_node)
print("DFS Expanded States:", expanded_states_dfs)
print("DFS Path:", dfs_path)
print("DFS States Not Expanded:", [node for node in graph if node not in expanded_states_dfs])

# Breadth-First Search
expanded_states_bfs, bfs_path = graph_breadth_first_search(graph, start_node, target_node)
print("\nBFS Expanded States:", expanded_states_bfs)
print("BFS Path:", bfs_path)
print("BFS States Not Expanded:", [node for node in graph if node not in expanded_states_bfs])

# Uniform Cost Search
expanded_states_ucs, ucs_path = graph_uniform_cost_search(graph, start_node, target_node)
print("\nUCS Expanded States:", expanded_states_ucs)
print("UCS Path:", ucs_path)
print("UCS States Not Expanded:", [node for node in graph if node not in expanded_states_ucs])

# Greedy Search
expanded_states_greedy, greedy_path = graph_greedy_search(graph, start_node, target_node, heuristics)
print("\nGreedy Search Expanded States:", expanded_states_greedy)
print("Greedy Search Path:", greedy_path)
print("Greedy Search States Not Expanded:", [node for node in graph if node not in expanded_states_greedy])

# A* Search
expanded_states_astar, astar_path = graph_a_star_search(graph, start_node, target_node, heuristics)
print("\nA* Search Expanded States:", expanded_states_astar)
print("A* Search Path:", astar_path)
print("A* Search States Not Expanded:", [node for node in graph if node not in expanded_states_astar])