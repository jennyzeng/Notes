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
		return self.adjList.get(vertex)
	
	def edgeExist(self, edge):
		return edge[1] in self.adjList[edge[0]]
	
	def __str__(self):
		return str(self.adjList)
	
	def __len__(self):
		return len(self.adjList)
#
#
# a = AdjList()
# print(a.addVertex(1))
# a.addEdge((1, 2))
# print(a.addVertex(2))
# print(a)
# print(a.getVertices())
# print(a.getNeighbors(1))
# print(a.edgeExist((2, 1)))
#
# a.createFromDict({1: {3}, 2: {1}})
# print(a)


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
		return self.adjList.get(vertex)
	
	def edgeExist(self, edge):
		return edge[1] in self.adjList[edge[0]]
	
	def __str__(self):
		return str(self.adjList)
	
	def __len__(self):
		return len(self.adjList)