# Johnson's algorithm and closeness centrality
from graphRepresentations import DirectedGraph,UndirectedGraph
import sys
from priodict import priorityDictionary
from copy import deepcopy

def addNewNode(G, q):
	# add new node q and connected by zero-weight edges to each of the other nodes
	vertices = G.getVertices()
	for v in vertices:
		G.addEdge(q, v, 0)
	return G
def bellmanFordForq(G, q):
	"""
	Second, the Bellman–Ford algorithm is used, starting from the new vertex q,
	 to find for each vertex v the minimum weight h(v)  of a path from q to v.
	If this step detects a negative cycle, the algorithm is terminated.
	"""
	# initialize
	h = dict()  # h[x]: dist from q to x
	h[q] = 0  # correct
	for v in G.getVertices():
		if v != q:
			h[v] = sys.maxsize  # infinity, incorrect

	edges = G.getEdges()
	for _ in range(len(G)):# run n-1 times
		for u, v, w in edges:
			# after i iterations of outer loop, first i levels of shortest path tree become correct
			h[v] = min(h[v], h[u]+w)
	# check negtive cycle
	for u, v, w in edges:
		if h[u] + w < h[v]: # can still relax! --> neg-cycle
			return None
	return h

def reweight(G,h):
	edges = G.getEdges()
	for u, v, w in edges:
		G.updateEdgeWeight(u,v, w+h[u]-h[v])
	return G


def DijkstraShortestPath(start, G):
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
	D = {} # D[x]: dist from s to x
	P = {} # P[x]: predecessor on path(parent in tree)
	Q = priorityDictionary()
	D[start] = 0  # correct
	for v in G.getVertices():
		if v != start:
			D[v] = sys.maxsize # infinity, incorrect
		P[v] = None
		Q[v] = D[v]

	for v in Q:# extract min
		for u, w in G.getNeighbors(v).items():
			if u in Q:
				if D[v] + w < D[u]:
					Q[u] = D[v] + w
					D[u] = Q[u]
					P[u] = v

	return D, P

def JohnsonAPSP(G):
	# "q" should not be in G initially
	q = "q"
	_G = deepcopy(G)
	_G = addNewNode(_G, q)
	h = bellmanFordForq(_G, q)
	G = reweight(G, h)
	D_table = {}
	P_table = {}
	for v in G.getVertices():
		D_table[v], P_table[v] = DijkstraShortestPath(v, G)

	return D_table, P_table



if __name__ == '__main__':

	g = UndirectedGraph()
	g.addEdges([("A", "B", 22), ("A", "C", 9), ("A", "D", 12), ("B", "C", 35), ("B", "F", 36), ("B", "H", 34),
	            ("C", "D", 4), ("C", "E", 65), ("C", "F", 42), ("D", "E", 33), ("D", "I", 30), ("E", "F", 18),
	            ("E", "G", 23), ("F", "G", 39), ("F", "H", 24), ("G", "H", 25), ("G", "I", 21), ("H", "I", 19)])
	D_table, P_table = JohnsonAPSP(g)
	print(D_table)
