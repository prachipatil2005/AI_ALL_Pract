#Bfs for romania problem
from collections import deque
def bfs(graph, start,goal):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex,'\t',end='')
# Explore neighbors
        neighbors = graph[vertex]
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
        if neighbor == goal:
            print(neighbor)
            return
# Example usage
graph = {'A': ['Z', 'S', 'T'],
         'B': ['U','P', 'G','F'],
         'C': ['D', 'R', 'P'],
         'D': ['M'],
         'E': ['H'],
         'I': ['V','N'],
         'L': ['T','M'],
         'O': ['Z','S'],
         'P': ['R'],
         'U': ['V'],
         'G':['B'],
         'N':['I'],
         'V': ['I','U'],
         'Z': ['O','A'],
         'S': ['O','A','R','F'],
         'T': ['A','L'],
         'M': ['L','D'],
         'R': ['S','P','C'],
         'F': ['S','B']}
start_vertex = 'A'
goal='B'
bfs(graph, start_vertex,goal)
