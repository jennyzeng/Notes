# X and Y are two sequences and we want to find the longest
#  common sub-sequence
# (same objects in same order, and gaps are allowed)
X = "skullandbones"
Y = "lullabybabies"

# initiallize a matrix
matrix = []
for i in range(len(X) + 1):
	# matrix.append(list())
	line = []
	for j in range(len(Y) + 1):
		line.append(None)
	matrix.append(line)

# first goal: find alternating sub-sequence of maximum length.
#   L[i][j] = len of LCS(first i char of X, first j char of Y)
# analysis:
#   (a) If last two chars are equal  X[i-1] == Y[j-1],
#   then it's always safe to use that character in the LCS
#   so L[i, j] = L[i-1, j-1] + 1
#   (b) If last two chars are not equal  X[i-1] != Y[j-1],
#   then we have to delete either last char of X or last char of Y
#   so L[i, j] = max( L[i-1, j], L[i, j-1] )

# base case: L[0, j] = l[i, 0] = 0

for i in range(len(X) + 1):
	for j in range(len(Y) + 1):
		if i == 0 or j == 0:
			matrix[i][j] = 0
		elif X[i - 1] == Y[j - 1]:
			matrix[i][j] = matrix[i - 1][j - 1] + 1
		else:
			matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print("result matrix: ")
for i in range(len(matrix)):
	print(matrix[i])

# Final Goal: Find LCS by following arrows backwards from (len(X), len(Y)) to (0, 0)
i = len(X)
j = len(Y)
LCS = []
while i + j > 0 and i > 0 and j > 0:
	if X[i - 1] == Y[j - 1]:  # diag arrow
		LCS.append(X[i - 1])
		i -= 1
		j -= 1
	else:
		if matrix[i - 1][j] > matrix[i][j - 1]:
			i -= 1
		else:
			j -= 1

LCS.reverse()

print("longest common sub-sequence: \n", LCS)

print("Time: O(len(X) + len(Y)")

# recursive version