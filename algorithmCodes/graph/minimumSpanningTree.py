from collections import defaultdict

from graph.graphRepresentations import UndirectedGraphWithWeights
from helpers.priodict import priorityDictionary

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
"""


def minimumSpanningTree(start, graph: UndirectedGraphWithWeights):
	# initialize a priority queue Q of vertices not yet in tree
	Q = priorityDictionary()
	D = priorityDictionary()
	P = defaultdict()
	D[start] = 0
	for vertex in graph.getVertices():
		if vertex != start:
			D[vertex] = 999999
		Q[vertex] = D[vertex]
		P[vertex] = None
	for vertex in Q:
		for w, k in graph.getNeighbors(vertex).items():
			if w in Q:
				# in Dijkstra: D[v] + k,
				# in P-D-J: k
				if k < D[w]:
					D[w] = k
					P[w] = vertex
					Q[w] = D[w]
	return D, P

g = UndirectedGraphWithWeights()
g.addEdges([("s", "x", 4), ("s", "y", 5), ("x", "y", 3)])
print(minimumSpanningTree("s", g))