from graphRepresentations import DirectedGraph, UndirectedGraph
import sys
from collections import Counter


# with shortest paths counter
def Floyd_Warshall(G):
	dist = dict()
	C = dict()  # counter for shortest paths
	vertices = G.getVertices()
	# initialize
	for v in vertices:
		dist[v] = {}
		dist[v][v] = 0
		C[v] = Counter()
		C[v][v] = 1
		for u in vertices:
			if u != v:
				dist[v][u] = sys.maxsize
				C[v][u] = 0

	for u, v, w in G.getEdges():
		dist[u][v] = w
		C[u][v] = 1

	# use dynamic programming
	for k in vertices:
		for i in vertices:
			for j in vertices:
				if i != j:
					if dist[i][j] > dist[i][k] + dist[k][j]:
						dist[i][j] = dist[i][k] + dist[k][j]
						C[i][j] = C[i][k] * C[k][j]
					elif dist[i][j] == dist[i][k] + dist[k][j] and k != i and k != j:
						C[i][j] += C[i][k] * C[k][j]
	return dist, C


if __name__ == '__main__':
	g = UndirectedGraph()
	g.addEdges([("A", "B", 22), ("A", "C", 9), ("A", "D", 12), ("B", "C", 35), ("B", "F", 36), ("B", "H", 34),
	            ("C", "D", 4), ("C", "E", 65), ("C", "F", 42), ("D", "E", 33), ("D", "I", 30), ("E", "F", 18),
	            ("E", "G", 23), ("F", "G", 39), ("F", "H", 24), ("G", "H", 25), ("G", "I", 21), ("H", "I", 19)])
	dist, C = Floyd_Warshall(g)
	print(dist)
	print(C)
