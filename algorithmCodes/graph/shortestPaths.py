from collections import defaultdict

from graph.graphRepresentations import DirectedGraphWithWeights
from graph.topologicalOrder import another_topological_ordering_edge_with_value
from helpers.priodict import priorityDictionary

"""
from cs161 note16
shortest paths algorithm

to convert shortest path to longest path:
	replace each edge length L by -L
If there are negative length cycle, then a shortest path might not exist

Can represent paths from s tart to all other vertices using O(n) pieces of information:
for each other vertex x,
	store D[x]: distance from s to t
	P[x]: predecessor on path (parent in tree)
	1. if we already have correct distance D[x] from start to some vertex x,
	and if x is the parent of y in the shortest path three,
	then we can compute D[y] as D[x] + length(x->y)
	2. if we dont know these things, use "relaxation":
		maintain a tentative (possibly incorrect)D[x] and P[x] for each vertex x,
		then call relax(edgex->y)
		
BellmanFord works for graphs that will have a shortest path, it is allowed to have negative edges,
but not negative cycles
"""


def relax(D, P, x, y, dis):
	if D[x] + dis < D[y]:
		P[y] = x
		D[y] = D[x] + dis


def DAGshortestPath(start, graph: DirectedGraphWithWeights):
	"""
	DAG shortest path only works when there is no cycle in the graph (has a topological order)
	"""
	# initialize
	D = defaultdict(int)  # D[x]: dist from s to x
	P = defaultdict()  # P[x]: predecessor on path(parent in tree)
	D[start] = 0
	for v in graph.getVertices():
		if v != start:
			D[v] = 9999999  # infinity
		P[v] = None
	
	topologicalOrder = another_topological_ordering_edge_with_value(graph)  # O(n+m)
	if not topologicalOrder: return D, P
	for v in topologicalOrder:
		for w, k in graph.getNeighbors(v).items():
			relax(D, P, v, w, k)
	return D, P


# time: O(n+m) + O(n+m) = O(n+m)

def BellmanFordShortestPath(start, graph: DirectedGraphWithWeights):
	"""
	BellmanFord works for graphs that will have a shortest path, it is allowed to have negative edges,
	but not negative cycles
	"""
	# initialize
	D = defaultdict(int)  # D[x]: dist from s to x
	P = defaultdict()  # P[x]: predecessor on path(parent in tree)
	D[start] = 0  # correct
	for v in graph.getVertices():
		if v != start:
			D[v] = 9999999  # infinity, incorrect
		P[v] = None
	
	edges = graph.getEdges()
	for _ in range(len(graph)):
		for edge in edges:
			# after i iterations of outer loop, first i levels of shortest path tree become correct
			relax(D, P, edge[0], edge[1], edge[2])
	return D, P


# O(mn)


def DijkstraShortestPath(start, graph: DirectedGraphWithWeights):
	"""
	Dijkstra works for graphs that might have cycles(not DAGs), but requires all edge weights > 0
	 other wise, may produce incorrect distances)
	 it don't need to topologically order the whole graph (not possible - not a DAG)
	 good enough to topological order the shortest path tree
	 (but we dont know the tree until we find the shortest paths)
	 time analysis:
		use binary heap + pointer from each vertex into heap -> O(mlog n)
	"""
	# initialize
	D = defaultdict(int)  # D[x]: dist from s to x
	P = defaultdict()  # P[x]: predecessor on path(parent in tree)
	Q = priorityDictionary()
	D[start] = 0  # correct
	for v in graph.getVertices():
		if v != start:
			D[v] = 9999999  # infinity, incorrect
		P[v] = None
		Q[v] = D[v]
	
	for v in Q:
		for w, k in graph.getNeighbors(v).items():
			relax(D, P, v, w, k)
			Q[w] = D[w]
	return D, P


def getShortestPath(D, P, terminal):
	output = []
	distance = D[terminal]
	vertex = terminal
	while True:
		output.append(vertex)
		vertex = P[vertex]
		if not P[vertex]:
			break
	output.reverse()
	return output, distance


g = DirectedGraphWithWeights()
g.addEdges(
	[("S", "A", 3), ("S", "C", 2), ("A", "B", 5), ("C", "B", 9), ("C", "D", 4), ("B", "T", 2), ("D", "T", 3)])

D, P = DAGshortestPath("S", g)
print("DAG result: ", getShortestPath(D, P, "T"))  # (['C', 'D', 'T'], 9)
D, P = BellmanFordShortestPath("S", g)
print("bellman-ford result: ", getShortestPath(D, P, "T"))
D, P = DijkstraShortestPath("S", g)
print("Dijkstra result: ", getShortestPath(D, P, "T"))
