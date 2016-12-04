"""
from cs161 note14
depth first search and strong connectivity
"""

from graph.graphRepresentations import DirectedGraph


def dfs(vertex, visited, graph):
	visited.append(vertex)
	for w in graph.getNeighbors(vertex):
		if w not in visited:
			dfs(w, visited, graph)

"""
time analysis:
for a graph with n vertices and m edges, then we make <= n calls to visit, and <= m iterations of loop
total time = O(n+m)
"""

graph = DirectedGraph()
graph.addVertices(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "s"])
graph.addEdges(
	[("s", "a"), ("s", "b"), ("a", "b"), ("a", "d"), ("b", "c"), ("c", "a"), ("c", "d"), ("c", "f"), ("c", "h"),
	 ("d", "e"), ("e", "d"), ("f", "g"), ("g", "c"), ("h", "i"), ("i", "j"), ("j", "h"), ("k", "b"), ("k", "h"),
	 ("l", "k"), ("l", "h")])

visited = []
dfs("s", visited, graph)
print(visited)

"""
directed graph G is strongly connected if:
	for every two vertices s and t in G:
		s can reach t (and vice versa)
"""


def strongConnectivity(graph):
	# choose any one vertex to be s
	s = graph.getVertices()[0]
	visited = []
	# use DFS to find vertices reachable from s
	dfs(s, visited, graph)
	if len(visited) != len(graph):
		return False
	
	reversedGraph = graph.reverse()
	reversedVisited = []
	# use DFS on reversed graph (same vertices, opposite direction edges)
	# to find vertices that can reach s
	dfs(s, reversedVisited, reversedGraph)
	# check that both sets have size n (n = # of vertices in graph)
	return len(reversedVisited) == len(visited)


print(graph)
print(graph.reverse())
print(strongConnectivity(graph))  # False
graph2 = DirectedGraph()
graph2.createFromDict({1: {2, 3}, 2: {1, 3}, 3: {1, 2}})
print(strongConnectivity(graph2))  # True
# time analysis:
# reverse takes O(n+m)
# 2 dfs: O(2*(n+m))
# total time: O(n+m)