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
  visited = []
  stack = []
  stack.append(start)
  while stack:
    s = stack.pop()
    if s not in visited:
      print(s, end=" ")
      visited.append(s)
    if s == end:
      return
    for neighbour in graph[s]:
      if neighbour not in visited:
        stack.append(neighbour)

print("Đồ thị 1")
dfs(graph1, 'S', 'G')
print()
print("Đồ thị 2")
dfs(graph2, 'S', 'G')
print()
print("Đồ thị 3")
dfs(graph3, 'A', 'G')