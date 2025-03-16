class DFS_Goal_Based_Agent:
    def __init__(self, graph):
        self.graph = graph
    
    def dfs(self, start, goal):
        stack = [(start, [start])]  # Stack stores (current_node, path)
        visited = set()
        
        while stack:
            node, path = stack.pop()
            
            if node == goal:
                return path  # Goal reached, return the path
            
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph.get(node, []):
                    stack.append((neighbor, path + [neighbor]))
        
        return None  # Goal not found

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['I'],
    'H': [],
    'I': []
}

agent = DFS_Goal_Based_Agent(graph)
start_node = 'A'
goal_node = 'I'

path = agent.dfs(start_node, goal_node)
print("Path to goal:", path)
