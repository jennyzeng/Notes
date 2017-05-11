from collections import defaultdict

from graphRepresentations import DirectedGraph, DirectedGraphWithWeights

"""
from cs161 note15
Directed Acyclic Graphs (DAG)
1. graphs with a topological ordering (every directed graph has either a cycle or a topological ordering, but not both.)
2. Topological order = sequence of all vertices so that for every edge x->y, x is before y in the sequence.
example of topological order:
"""


"""
Proof of Directed Acyclic Graph
1. proof of "topological order = sequence of all vertices so that for every edge x->y, x is before y in the sequence"
if graph G has a cycle, then G has no topological order.
because: which ever vertex of the cycle we place first in an ordering would have an incoming edge from a later vertex

2. Quick sketch: DFS-based topological ordering
	- idea: postorder traverse of DFS tree, then reverse that order
	
!!it does not return a correct result when there is a cycle in the graph.
"""


def DFS_based_topological_ordering(graph: DirectedGraph):
	visited = set()
	postorder = []
	
	def visit(v):
		visited.add(v)
		for w in graph.getNeighbors(v):
			if w not in visited:
				visit(w)
		postorder.append(v)
	
	for v in graph.getVertices():
		if v not in visited:
			visit(v)
	postorder.reverse()
	return postorder



"""
another topological ordering algorithm (from textbook)
1. have to start at a vertex with no incoming edges
e.g. in previous example, the only vertex with no incoming edges is a
2. once you choose the starting vertex, you keep looking for the vertex in remaining vertices with no incoming edges,
and so on.

3. total time = O(n + m)

4. when this algorithm succeeds- it finds a topological ordering
when this algorithm fails -
	get a subset of the graph(its remaining non-output vertices)
	in which every vertex has an incoming edge from another vertex in the same subset
	(else it whould have gone into C and then output)

find a cycle by
- start at any vertex
- backtrack along incoming edges until repetition
"""


def another_topological_ordering(graph: DirectedGraph):
	C = []  # collection of vertices with no incoming edges
	# D is dictionary mapping each vertex to a number, # of incoming edges that come from vertices that have not yet
	# been output. Initially D[v] = total # of incoming edges to v
	D = defaultdict(int)
	for v in graph.getVertices():
		D[v]
		for w in graph.getNeighbors(v):
			D[w] += 1
	for v in graph.getVertices():
		if D[v] == 0:
			C.append(v)
	
	output = []
	while C:  # happen <= n times because n vertices
		vertex = C[0]
		C = C[1:]
		output.append(vertex)
		for w in graph.getNeighbors(vertex):  # happen <= m times
			D[w] -= 1
			if D[w] == 0:
				C.append(w)
	if len(output) == len(graph):
		return output
	else:
		# print(output)
		return False  # not acyclic


def another_topological_ordering_edge_with_value(graph: DirectedGraphWithWeights):
	C = []  # collection of vertices with no incoming edges
	# D is dictionary mapping each vertex to a number, # of incoming edges that come from vertices that have not yet
	# been output. Initially D[v] = total # of incoming edges to v
	D = defaultdict(int)
	for v in graph.getVertices():
		D[v]
		for w in graph.getNeighbors(v):
			D[w] += 1
	for v in graph.getVertices():
		if D[v] == 0:
			C.append(v)
	
	output = []
	while C:  # happen <= n times because n vertices
		vertex = C[0]
		C = C[1:]
		output.append(vertex)
		for w in graph.getNeighbors(vertex):  # happen <= m times
			D[w] -= 1
			if D[w[0]] == 0:
				C.append(w[0])
	if len(output) == len(graph):
		return output
	else:
		# print(output)
		return False  # not acyclic




if __name__ == "__main__":
	graph = DirectedGraph()
	graph.addEdges(
		[("a", "b"), ("a", "e"), ("a", "c"), ("b", "c"), ("c", "d"), ("c", "e"), ("c", "f"), ("d", "f"), ("e", "f"),
		 ("e", "g")])
	print(DFS_based_topological_ordering(graph))  # ['a', 'b', 'c', 'e', 'g', 'd', 'f']
	graph2 = DirectedGraph()
	graph2.addEdges(
		[("a", "b"), ("a", "e"), ("a", "c"), ("b", "c"), ("c", "d"), ("c", "e"), ("c", "f"), ("d", "f"), ("e", "f"),
		 ("e", "g"), ("c", "b")])
	print(DFS_based_topological_ordering(graph2))
	print(another_topological_ordering(graph))
	print(another_topological_ordering(graph2))
	
	g = DirectedGraphWithWeights()
	g.addEdges(
		[("S", "A", 3), ("S", "C", 2), ("A", "B", 5), ("C", "B", 9), ("C", "D", 4), ("B", "T", 2), ("D", "T", 3)])
	print(another_topological_ordering_edge_with_value(g))  # ['S', 'C', 'A', 'D', 'B', 'T']