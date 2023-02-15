from collections import deque

class Graph:
    def __init__(self, adjacency_list,heuristic):
        self.adjacency_list = adjacency_list
        self.h = heuristic

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def greedy_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        
        g = {}

        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node
        dem = 1

        while len(open_list) > 0:
            n = None

            for v in open_list:
                if n == None or self.h[v] < self.h[n]:
                    n = v;

            if n == None:
                print('Path does not exist!')
                print('Số node được mở rộng: {}'.format(dem))
                return None

            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                print('Số node được mở rộng: {}'.format(dem))
                return reconst_path


            for (m, weight) in self.get_neighbors(n):

                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    dem = dem + 1
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        print('Số node được mở rộng: {}'.format(dem))
        return None

print("Đồ thị 1")
adjacency_list1 = {
    'A': [('C', 2), ('D', 3)],
    'B': [('D', 2), ('E', 4)],
    'C': [('G', 4)],
    'D': [('G', 4)],
    'E': [],
    'F': [('G', 6)],
    'G': [],
    'S': [('A', 2), ('B', 1), ('F', 3)]
}
heuristic1 = {
    'S': 6,
    'A': 4,
    'B': 5,
    'C': 2,
    'D': 2,
    'E': 8,
    'F': 4,
    'G': 0
}

graph1 = Graph(adjacency_list1,heuristic1)
graph1.greedy_algorithm('S', 'G')


print("Đồ thị 2")
adjacency_list2 = {
    'A': [('B', 1), ('C', 1)],
    'B': [('A', 1), ('D', 1)],
    'C': [('A', 1), ('K', 1)],
    'D': [('B', 1), ('E', 1), ('M', 1)],
    'E': [('D', 1), ('N', 1)],
    'F': [('S', 1), ('P', 1)],
    'G': [('T', 1), ('M', 1)],
    'S': [('F', 1), ('H', 1)],
    'H': [('S', 1), ('K', 1)],
    'K': [('H', 1), ('C', 1)],
    'M': [('D', 1), ('G', 1), ('N', 1)],
    'N': [('M', 1), ('E', 1)],
    'P': [('F', 1), ('Q', 1)],
    'Q': [('P', 1), ('R', 1)],
    'R': [('Q', 1), ('T', 1)],
    'T': [('R', 1), ('G', 1)]
}

heuristic2 = {
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 3,
    'F': 5,
    'G': 0,
    'S': 4,
    'H': 3,
    'K': 2,
    'M': 1,
    'N': 2,
    'P': 4,
    'Q': 3,
    'R': 2,
    'T': 1
}

graph1 = Graph(adjacency_list2,heuristic2)
graph1.greedy_algorithm('S', 'G')


print("Đồ thị 3")
adjacency_list3 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 1), ('D', 5)],
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('E', 8), ('F', 3), ('G', 9)],
    'E': [('D', 8), ('G', 2)],
    'F': [('D', 3), ('G', 5)],
    'G': [('E', 2), ('F', 5), ('D', 9)],
}
heuristic3_h1 = {
    'A': 9.5,
    'B': 9,
    'C': 8,
    'D': 7,
    'E': 1.5,
    'F': 4,
    'G': 0
}
heuristic3_h2 = {
    'A': 10,
    'B': 12,
    'C': 10,
    'D': 8,
    'E': 1,
    'F': 4.5,
    'G': 0
}

print("h1")
graph1 = Graph(adjacency_list3,heuristic3_h1)
graph1.greedy_algorithm('A', 'G')
print("h2")
graph1 = Graph(adjacency_list3,heuristic3_h2)
graph1.greedy_algorithm('A', 'G')



print("Đồ thị 4")
adjacency_list4 = {
    'Arad': [('Zerind', 75), ('Timisoara', 118)],
    'Bucharest': [('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Craiova': [('Pitesti', 138), ('Rimnicu Vilcea', 146), ('Dobreta', 120)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Eforie': [('Hirsova', 86)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Giurgiu': [('Bucharest', 90)],
    'Hirsova': [('Eforie', 86), ('Urziceni', 98)],
    'Iasi': [('Neamt', 87), ('Vaslui', 92)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Dobreta', 75), ('Lugoj', 70)],
    'Neamt': [('Iasi', 87)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80), ('Arad', 140), ('Oradea', 151)],
    'Timisoara': [('Lugoj', 111), ('Arad', 118)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Vaslui': [('Iasi', 92), ('Urziceni', 142)],
    'Zerind': [('Arad', 75), ('Oradea', 71)]
}

heuristic4 = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 178,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 98,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

graph1 = Graph(adjacency_list4,heuristic4)
graph1.greedy_algorithm('Arad', 'Bucharest')