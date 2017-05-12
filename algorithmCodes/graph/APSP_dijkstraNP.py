from priodict import priorityDictionary as pq
import sys
from collections import Counter


# for graphs without negative weights
# counting number of paths pass through



# TA Nil's pesudocode using dijkstra to count
# this is for counting the shortest paths with s as the source
def dijkstraNP(G, s):
	dist = dict()
	NP = Counter()  # counter for shortest paths,
	Q = pq()  # priority queue with all the nodes using dist[u] as key for node u
	vertices = G.getVertices()
	for v in vertices:
		dist[v] = sys.maxsize
		NP[v] = 0  # C[v] = number of shortest paths from s to v
		Q[v] = dist[v]
	dist[s] = 0
	NP[s] = 1
	Q[s] = 0

	while Q:
		u = Q.smallest()
		del Q[u]
		for v, w in G.getNeighbors(u).items():
			if dist[v] > dist[u] + w:
				dist[v] = dist[u] + w
				Q[v] = dist[v]
				NP[v] = NP[u]
			elif dist[v] == dist[u] + w:
				NP[v] += NP[u]
	return dist, NP


def APSPdijkstraNP(G):
	dist = {}
	C = {}
	for s in G.getVertices():
		dist[s], C[s] = dijkstraNP(G, s)
	return dist, C
