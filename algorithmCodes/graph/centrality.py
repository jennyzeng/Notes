from APSP_JohnsonsAlg import *


def closenessCentrality(G, D_table):
	CCtable = {}
	for v in G.getVertices():
		distance = sum(D_table[v].values())
		CCtable[v] = (1,distance)
	return CCtable

if __name__ == '__main__':

	g = UndirectedGraph()
	g.addEdges([("A", "B", 22), ("A", "C", 9), ("A", "D", 12), ("B", "C", 35), ("B", "F", 36), ("B", "H", 34),
	            ("C", "D", 4), ("C", "E", 65), ("C", "F", 42), ("D", "E", 33), ("D", "I", 30), ("E", "F", 18),
	            ("E", "G", 23), ("F", "G", 39), ("F", "H", 24), ("G", "H", 25), ("G", "I", 21), ("H", "I", 19)])
	D_table, P_table = JohnsonAPSP(g)
	print(D_table)
	print(closenessCentrality(g, D_table))