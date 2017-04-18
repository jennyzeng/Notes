from collections import defaultdict

from graphRepresentations import UndirectedGraphWithWeights
from priodict import priorityDictionary
from collections import deque

"""
from cs161 note18
Maximum Spanning Tree = minimum Spanning Tree for negated edge lengths
# Cut property
1. if you're given a weighted graph G(with no two weights equal), and a partition of
the vertices into two sets X, Y = vertices not in X
Then min-weight edge that crosses from one side to the other must be in the Minimum Spanning Tree
2. Why is cut property true?
Suppose you have a graph G, a cut(x,y) and a tree T that does not use minimum weight edge
then path in T from s to t must cross from X to Y at some other edge e
=> T-e+st (st:edge s-t)
is a better tree (T is not Minimum Spanning Tree)

Prim-Dijkstra-Jaruik algorithm
O(m log n) algorithm

intuition: build a tree one vertex at a time
at each step: find minimum edge from tree to rest of graph, add that edge to tree


Update for CS163
Kruskal's algorithm

Baruvkas algorithm
"""


def Prim_Dijkstra_Jarnik(start, graph):
	# initialize a priority queue Q of vertices not yet in tree
	Q = priorityDictionary()
	D = dict()
	P = dict()
	D[start] = 0
	T = UndirectedGraphWithWeights()
	for vertex in graph.getVertices():
		if vertex != start:
			D[vertex] = 999999
		Q[vertex] = D[vertex]
		P[vertex] = None
	for vertex in Q:  # extract min
		if P[vertex]:
			T.addEdge(vertex, P[vertex], graph.getEdgeWeight(vertex, P[vertex]))
		# print("add edge: ", vertex, P[vertex], graph.getEdgeWeight(vertex,P[vertex] ))
		else:
			T.addVertex(vertex)
		# print("add vertex: ", vertex)
		for w, k in graph.getNeighbors(vertex).items():
			if w in Q:
				# in Dijkstra: D[v] + k,
				# in P-D-J: k
				if k < D[w]:
					D[w] = k
					P[w] = vertex
					Q[w] = D[w]
	return T


"""
Kruskal's Approach maintain a partition of the vertices into clusters.
	Initially, we have single-vertex clusters
	We view each cluster as an MST
	Then we merge the closest clusters and their MSTs

Use a pq to store the edges outside clusters
	key: weight
	element: edge

And the end of the algorithm, we get only one cluster and one MST

Running time O((n+m) log n)
	- pq operations: O(m log n)
	- Union-Find operations: O(n log n)
"""


# TODO: a better implementation can be done using linked list
def Kruskals(graph):
	T = UndirectedGraphWithWeights()
	C = []  # clusters
	Q = priorityDictionary()
	eleIndices = {}
	for v in graph.getVertices():
		eleIndices[v] = len(C)  # mark cluster index for element, useful for referring later.
		C.append(set(v))  # init clusters

	for u, v, w in graph.getAllEdges():
		Q[(u, v)] = w  # storing edges in G
	numEdges = 0
	while numEdges < len(graph) - 1:
		u, v = Q.smallest()
		w = Q[(u, v)]
		del Q[(u, v)]
		# find cv, the cluster containing v, and find cu, the cluster containing u
		cu = eleIndices[u]
		cv = eleIndices[v]
		if cv != cu:
			T.addEdge(u, v, w)
			numEdges += 1
			# print(numEdges)
			# print("add edge ", u,v,w)
			C[cv] = C[cv].union(C[cu])  # union cv and cu
			for ele in C[cu]:
				eleIndices[ele] = cv
			# we can del cv here, but it require us to update
			#  references of elements in other sets after cv
	return T


"""
Like Kruskal's algorithm, Baruvka's algorithm grows many clusters at once and
maintains a forest T
Each iteration of the while loop halves the number of connected components in forest T
The running time is O(m log n) (master theorem)
"""


def Baruvkas(graph):
	vertices = graph.getVertices()
	T = UndirectedGraphWithWeights()
	T.addVertices(vertices)
	numEdges = 0
	Q = deque()  # use queue to store clusters
	for v in vertices:
		Q.append({v})  # init all clusters
	while numEdges < len(graph) - 1:
		cluster = Q.popleft()  # do this for each cluster in T

		# find the smallest-weight edge from this cluster to another cluster in T
		minEdge = None
		for u in cluster:
			for v in graph.getNeighbors(u):
				w = graph.getEdgeWeight(u, v)
				if v not in cluster and (not minEdge or w < minEdge[2]):
					minEdge = (u, v, w)
		# if minEdge is not already in T
		#   we add minEdge to T
		if minEdge and not T.edgeExist(minEdge[0], minEdge[1]):
			T.addEdge(minEdge[0], minEdge[1], minEdge[2])
			numEdges += 1
			for targetCluster in Q:
				if minEdge[1] in targetCluster:
					cluster = cluster.union(targetCluster)  # union two clusters
					Q.remove(targetCluster)
					Q.append(cluster)  # add it to queue as a cluster in T
					break
	return T


if __name__ == '__main__':
	g = UndirectedGraphWithWeights()
	g.addEdges([("A", "B", 22), ("A", "C", 9), ("A", "D", 12), ("B", "C", 35), ("B", "F", 36), ("B", "H", 34),
	            ("C", "D", 4), ("C", "E", 65), ("C", "F", 42), ("D", "E", 33), ("D", "I", 30), ("E", "F", 18),
	            ("E", "G", 23), ("F", "G", 39), ("F", "H", 24), ("G", "H", 25), ("G", "I", 21), ("H", "I", 19)])

	print("Prim Jarnik alg: \n", Prim_Dijkstra_Jarnik("A", g))
	print("Kruskal's: \n", Kruskals(g))
	print("Baruvka's \n", Baruvkas(g))
