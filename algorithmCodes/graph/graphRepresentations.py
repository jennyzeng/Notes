"""
from cs161 note13
ways of representating a graph
1. adjacency list (2 ways)
2. van Rossum(python adjacency list)
3. adjacency matrix

vertex: anything that can be a dicct key (not special vertex object)
neighbors: list(of set) of vertices
graph: dict where keys - vertices, values = neighborhoods
"""
from collections import defaultdict


class UndirectedGraph:
	def __init__(self):
		self.adjList = defaultdict(set)
	
	def createFromDict(self, d):
		self.adjList = defaultdict(set, d)
	
	def addVertex(self, vertex):
		if vertex not in self.adjList:
			self.adjList.update({vertex: set()})
			return True
		else:
			return False
	
	def addVertices(self, vertices):
		for v in vertices:
			self.addVertex(v)
	
	def addEdge(self, edge: tuple):
		self.adjList[edge[0]].add(edge[1])
		self.adjList[edge[1]].add(edge[0])
	
	def addEdges(self, edges):
		for edge in edges:
			self.addEdge(edge)
	
	def getVertices(self):
		return [v for v in self.adjList]
	
	def getNeighbors(self, vertex):
		neighbors = self.adjList.get(vertex)
		if not neighbors:
			return []
		else:
			return neighbors
	
	def edgeExist(self, edge):
		return edge[1] in self.adjList[edge[0]]
	
	def __str__(self):
		return str(self.adjList)
	
	def __len__(self):
		return len(self.adjList)


class UndirectedGraphWithWeights:
	def __init__(self):
		self.adjList = defaultdict(dict)
	def __len__(self):
		return len(self.adjList)
	def __eq__(self, other):
		self.adjList == other.adjList

	def createFromDict(self, d):
		self.adjList = defaultdict(dict, d)
	
	def addVertex(self, vertex):
		if vertex not in self.adjList:
			self.adjList.update({vertex: dict()})
			return True
		else:
			return False
	
	def addVertices(self, vertices):
		for v in vertices:
			self.addVertex(v)
	
	def addEdge(self, u, v, w):
		self.adjList[u].update({v: w})
		self.adjList[v].update({u: w})
	
	def addEdges(self, edges):
		for u,v,w in edges:
			self.addEdge(u,v,w)
	
	def getVertices(self):
		return [v for v in self.adjList]
	
	def getNeighbors(self, vertex):
		neighbors = self.adjList.get(vertex)
		if not neighbors:
			return {}
		else:
			return neighbors

	def getEdgeWeight(self, u, v):
		if u in self.adjList:
			if v in self.adjList[u]:
				return self.adjList[u][v]
		else:
			return None
	def edgeExist(self, u,v):
		return v in self.adjList[u]

	def getAllEdges(self):
		edges = []
		visited=set()
		for v in self.adjList:
			for w in self.adjList[v]:
				if w not in visited:
					edges.append((v, w, self.adjList[v][w]))
			visited.add(v)
		return edges



	def __str__(self):
		return str(self.adjList)
	
	def __len__(self):
		return len(self.adjList)


class DirectedGraph:
	def __init__(self):
		self.adjList = defaultdict(set)
	
	def createFromDict(self, d):
		self.adjList = defaultdict(set, d)
	
	def addVertex(self, vertex):
		if vertex not in self.adjList:
			self.adjList.update({vertex: set()})
			return True
		else:
			return False
	
	def addVertices(self, vertices):
		for v in vertices:
			self.addVertex(v)
	
	def addEdge(self, edge: tuple):
		self.adjList[edge[0]].add(edge[1])
		self.adjList[edge[1]]
	
	def addEdges(self, edges):
		for edge in edges:
			self.addEdge(edge)
	
	def reverse(self):
		reversed = DirectedGraph()
		for v in self.getVertices():
			for w in self.getNeighbors(v):
				reversed.addEdge((w, v))
		return reversed
	
	def getVertices(self):
		return [v for v in self.adjList]
	
	def getNeighbors(self, vertex):
		neighbors = self.adjList.get(vertex)
		if not neighbors:
			return []
		else:
			return neighbors
	
	def edgeExist(self, edge):
		return edge[1] in self.adjList[edge[0]]
	
	def __str__(self):
		return str(self.adjList)
	
	def __len__(self):
		return len(self.adjList)


class DirectedGraphWithWeights:
	# edge of the graph has a value
	def __init__(self):
		self.adjList = defaultdict(dict)

	# def createFromDict(self, d):
	# 	self.adjList = defaultdict(set, d)

	def addVertex(self, vertex):
		if vertex not in self.adjList:
			self.adjList.update({vertex: dict()})
			return True
		else:
			return False

	def addVertices(self, vertices):
		for v in vertices:
			self.addVertex(v)

	def addEdge(self, edge: tuple):
		# edge representation (x,y,v) x->y, edge value = v
		# so it is {x:{y: v}}
		self.adjList[edge[0]].update({edge[1]: edge[2]})
		self.adjList[edge[1]]
	
	def addEdges(self, edges):
		for edge in edges:
			self.addEdge(edge)
	
	def reverse(self):
		reversed = DirectedGraph()
		for v in self.getVertices():
			for w in self.getNeighbors(v):
				reversed.addEdge((w, v, self.adjList[v][w]))
		return reversed
	
	def getVertices(self):
		return [v for v in self.adjList]
	
	def getNeighbors(self, vertex):
		neighbors = self.adjList.get(vertex)
		if not neighbors:
			return {}
		else:
			return neighbors
	
	def getEdge(self, s, e):
		if self.adjList.get(s):
			for v, k in self.adjList[s].items():
				if e == v:
					return k
		else:
			return None
	
	def getEdges(self):
		output = []
		for v in self.adjList:
			for x in self.getNeighbors(v):
				output.append((v, x, self.adjList[v][x]))
		return output
	
	def edgeExist(self, edge):
		return edge[1] in self.adjList[edge[0]] and edge[2] == self.adjList[edge[0]][edge[1]]
	
	def __str__(self):
		return str(self.adjList)
	
	def __len__(self):
		return len(self.adjList)

