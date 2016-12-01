"""
given a n*m matrix, there is a path p starts from matrix[0][0] and  ends at matrix[len(matrix)-1][len(matrix[0]-1]
if the min value in p is p_m, find the maximum of all min values of paths in matrix.
e.g. matrix:
[8, 4, 7]
[6, 5, 9]
exist three paths:
8-4-7-9 min: 4
8-4-5-9 min: 4
8-6-5-9 min: 5
return 5
"""

def findMaximumMinimumPath(matrix):
	if len(matrix) == 0:
		return 0

	DP = makeTable(matrix)

def makeTable(matrix):
	DP = [[None] * matrix[0] for _ in range(len(matrix))]
	DP[0][0] = matrix[0][0]
	for i in range(len(matrix)):
		pass
		