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

def dfs(graph, start, end):
  stack = []
  visited = []
  stack.append([start])
  while stack:
    path = stack.pop()
    node = path[-1]
    if node not in visited:
      visited.append(node)
    if node == end:
      return path
    for neighbour in graph.get(node, []):
      if neighbour not in visited:
        new_path = list(path)
        new_path.append(neighbour)
        stack.append(new_path)

print("Đồ thị 1")
print(dfs(graph1, 'S', 'G'))
print("Đồ thị 2")
print(dfs(graph2, 'S', 'G'))
print("Đồ thị 3")
print(dfs(graph3, 'A', 'G'))