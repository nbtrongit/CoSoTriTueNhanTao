# đồ thị 1
graph1 = {
  'A': [],
  'B': ['A'],
  'C': ['A'],
  'D': ['B', 'C', 'E'],
  'E': ['H', 'R'],
  'F': ['C', 'G'],
  'G': [],
  'H': ['P', 'Q'],
  'P': ['Q'],
  'Q': [],
  'R': ['F'],
  'S': ['D', 'E', 'P']
}

# đồ thị 2
graph2 = {
  'A': ['B', 'C'],
  'B': ['A', 'D'],
  'C': ['A', 'K'],
  'D': ['B', 'E', 'M'],
  'E': ['D', 'N'],
  'F': ['P', 'S'],
  'G': ['M', 'T'],
  'H': ['K', 'S'],
  'K': ['C', 'H'],
  'M': ['D', 'G', 'N'],
  'N': ['E', 'M'],
  'P': ['F', 'Q'],
  'Q': ['P', 'R'],
  'R': ['Q', 'T'],
  'S': ['F', 'H'],
  'T': ['G', 'R']
}

# đồ thị 3
graph3 = {
  'A': ['B', 'C'],
  'B': ['A', 'C', 'D'],
  'C': ['A', 'B', 'D'],
  'D': ['B', 'C', 'E', 'F', 'G'],
  'E': ['D', 'G'],
  'F': ['D', 'G'],
  'G': ['D', 'E', 'F']
}

# graph is in adjacent list representation

def bfs(graph, start, end):
  # maintain a queue of paths
  queue = []
  visited = []
  # push the first path into the queue
  queue.append([start])
  while queue:
    # get the first path from the queue
    path = queue.pop(0)
    # get the last node from the path
    node = path[-1]
    # path found
    if node == end:
      return path
  # enumerate all adjacent nodes, construct a new path and push it into the queue
    for neighbour in graph.get(node, []):
      if neighbour not in visited:
        visited.append(neighbour)
        new_path = list(path)
        new_path.append(neighbour)
        queue.append(new_path)

print("Đồ thị 1")
print(bfs(graph1, 'S', 'G'))
print("Đồ thị 2")
print(bfs(graph2, 'S', 'G'))
print("Đồ thị 3")
print(bfs(graph3, 'A', 'G'))