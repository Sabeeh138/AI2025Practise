class AStar_Goal_Based_Agent:
    def __init__(self, graph, heuristic):
        self.graph = graph
        self.heuristic = heuristic
    
    def a_star(self, start, goal):
        frontier = [(start, 0 + self.heuristic[start])]  # List-based priority queue (sorted manually)
        visited = set()  # Set to keep track of visited nodes
        g_costs = {start: 0}  # Cost to reach each node from start
        came_from = {start: None}  # Path reconstruction
        
        while frontier:
            frontier.sort(key=lambda x: x[1])  # Sort by f(n) = g(n) + h(n)
            current_node, current_f = frontier.pop(0)  # Get node with lowest f(n)
            
            if current_node in visited:
                continue
            
            print(current_node, end=" ")  # Print visited node
            visited.add(current_node)
            
            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                print(f"\nGoal found with A*. Path: {path}")
                return path
            
            for neighbor, cost in self.graph.get(current_node, {}).items():
                new_g_cost = g_costs[current_node] + cost  # Path cost from start to neighbor
                f_cost = new_g_cost + self.heuristic[neighbor]  # f(n) = g(n) + h(n)
                if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = new_g_cost
                    came_from[neighbor] = current_node
                    frontier.append((neighbor, f_cost))
        
        print("\nGoal not found")
        return None

# Example graph as an adjacency list with costs
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

# Example heuristic function (estimated cost to goal 'I')
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 7,
    'F': 3,
    'G': 6,
    'H': 2,
    'I': 0  # Goal node
}

agent = AStar_Goal_Based_Agent(graph, heuristic)
start_node = 'A'
goal_node = 'I'

print("\nFollowing is the A* Search:")
agent.a_star(start_node, goal_node)
