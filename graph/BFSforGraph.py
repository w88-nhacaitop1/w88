# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * len(self.graph)

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# Driver Code
if __name__ == "__main__":
    # g = Graph()
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 3)
    # g.addEdge(3, 3)

    g = Graph()
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 1)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 1)
    g.addEdge(3, 5)
    g.addEdge(4, 2)
    g.addEdge(4, 5)
    g.addEdge(4, 6)
    g.addEdge(5, 2)
    g.addEdge(5, 3)
    g.addEdge(5, 4)
    g.addEdge(5, 6)
    g.addEdge(6, 4)
    g.addEdge(6, 5)

    vertex = 1
    print("Following is Breath First Traversal"
                    f" (starting from vertex {vertex})")
    g.BFS(vertex)



