
def createDP(matrix):
	return [[None] * len(matrix[0]) for _ in range(len(matrix))]


def printMatrix( matrix):
	for i in range(len(matrix)):
		print(matrix[i])