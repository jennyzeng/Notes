from APSP_JohnsonsAlg import JohnsonAPSP
from graphRepresentations import DirectedGraph, UndirectedGraph
from collections import Counter
from APSP_FloydWarshall import Floyd_Warshall
from APSP_dijkstraNP import APSPdijkstraNP


def closenessCentrality(G):
	D_table, _ = JohnsonAPSP(G)
	CCtable = {}
	for v in G.getVertices():
		distance = sum(D_table[v].values())
		CCtable[v] = (1, distance)
	return CCtable

##### two ways to calculate the betweeness centrality
##### use FloydWarshall or djkstra to calcuate the number of paths!

def numpathsthrough(s, t, v, dist, C):
	if dist[s][t] == dist[s][v] + dist[v][t]:
		return C[s][v] * C[v][t]
	else:
		return 0

def betweennessCentralityForV(G,v,dist,C):
	score = 0
	for s in G.getVertices():
		if s!= v:
			for t in G.getVertices():
				if t!=v and t!=s:
					score += numpathsthrough(s,t,v, dist, C)/C[s][t]
	return score
def betweennessCentrality(G, dist, C):
	score = Counter()
	vertices = G.getVertices()
	for v in vertices:
		score[v] = betweennessCentralityForV(G, v, dist, C)
	return score


if __name__ == '__main__':
	g = UndirectedGraph()
	g.addEdges([("A", "B", 22), ("A", "C", 9), ("A", "D", 12), ("B", "C", 35), ("B", "F", 36), ("B", "H", 34),
	            ("C", "D", 4), ("C", "E", 65), ("C", "F", 42), ("D", "E", 33), ("D", "I", 30), ("E", "F", 18),
	            ("E", "G", 23), ("F", "G", 39), ("F", "H", 24), ("G", "H", 25), ("G", "I", 21), ("H", "I", 19)])
	print("closeness Centrality using Johnson's algorithm:")
	print(closenessCentrality(g))
	print()
	print("betweenness Centrality using dijkstra:")
	dist, C = APSPdijkstraNP(g)
	print(betweennessCentrality(g, dist, C))
	print()
	print("betweenness Centrality using Floyd-Warshall:")
	dist, C = Floyd_Warshall(g)
	print(betweennessCentrality(g, dist, C))
