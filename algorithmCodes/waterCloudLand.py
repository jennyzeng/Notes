"""
depth first search

find the min number of possible lands in matrix.
matrix has:
- (w) water
- (l) land
- (c) cloud (can be either water or land)
matrix = [
	["c", "w", "l", "c", "c"],
	["c", "w", "l", "w", "c"],
	["c", "l", "l", "c", "c"],
	["c", "w", "w", "w", "c"],
	["c", "w", "l", "w", "c"]
]
"""

def transform(matrix):
	newMatrix = [[None] * len(matrix[0]) for _ in range(len(matrix))]
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			val = matrix[i][j]
			if val == "l":
				newMatrix[i][j] = 1
			elif val == "w":
				newMatrix[i][j] = 0
			else:
				if hasLandAround(newMatrix, matrix, i, j):
					newMatrix[i][j] = 1
				else:
					newMatrix[i][j] = 0
	return newMatrix


def hasLandAround(tranmatrix, matrix, x, y):
	myBool = False
	if x - 1 >= 0:
		myBool |= tranmatrix[x - 1][y] == 1 or matrix[x - 1][y] == "l"
	if y - 1 >= 0:
		myBool |= tranmatrix[x][y - 1] == 1 or matrix[x][y - 1] == "l"
	if x + 1 < len(matrix):
		myBool |= matrix[x + 1][y] == "l"
	if y + 1 < len(matrix[0]):
		myBool |= matrix[x][y + 1] == "l"
	return myBool


def dfs(i, j, transformedMatrix):
	if transformedMatrix[i][j] == 1 and (i, j) not in visited:
		visited.add((i, j))
		if i - 1 >= 0: dfs(i - 1, j, transformedMatrix)
		if j - 1 >= 0: dfs(i, j - 1, transformedMatrix)
		if j + 1 < len(transformedMatrix[0]): dfs(i, j + 1, transformedMatrix)
		if i + 1 < len(transformedMatrix): dfs(i + 1, j, transformedMatrix)
	else:
		return


def findMinLand(matrix):
	if len(matrix) == 0:
		return 0
	count = 0
	tranMatrix = transform(matrix)
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if (i, j) not in visited and tranMatrix[i][j] == 1:
				dfs(i, j, tranMatrix)
				count += 1
	return count

## test
matrix = [
	["c", "w", "l", "c", "c"],
	["c", "w", "l", "w", "c"],
	["c", "l", "l", "c", "c"],
	["c", "w", "w", "w", "c"],
	["c", "w", "l", "w", "c"]
]

visited = set()
print(findMinLand(matrix))

visited = set()
matrix = [
	["c", "w", "l", "c", "c"],
	["c", "w", "l", "w", "c"],
	["c", "l", "l", "c", "w"],
	["c", "w", "w", "w", "c"],
	["c", "w", "l", "w", "c"]
]
print(findMinLand(matrix))
