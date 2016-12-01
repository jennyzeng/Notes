# game strategy for coins-in-a-line or a pizza game
# coins in a line, value of coins


def makeTable(A):
	# initialize the value table
	DP = [[None]*len(A) for _ in range(len(A))]  # value table


	# calculate values for table
	for i in range(len(A)):
		DP[i][i] = A[i]
	for s in range(2, len(A) + 1):
		for i in range(0, len(A) - s + 1):
			j = i + s - 1
			DP[i][j] = max(A[i] - DP[i + 1][j],
			               A[j] - DP[i][j - 1])
	# print the result value table
	# j horizontal, i vertical
	for i in range(len(A)):
		print(DP[i])

	print("\nTime: O(n^2)")
	return DP

def makeMove(i, j, DP, A):
	"""
	it will make move when there is A[i:j+1] left
	"""
	if i == j:
		print("i == j, take A[i] ", A[i])
		return A[i]
	takeLeft = DP[i + 1][j]
	takeRight = DP[i][j - 1]
	if takeLeft < takeRight:
		# pick left
		return A[i]

	else:
		# pick right
		return A[j]


player1 = "Alice"
player2 = "Bob"
playerdict = {player1:player2, player2: player1}
scoreDict = {player1:0, player2:0}

def simulation(i, j, DP, A, player):
	"""
	It will simulate the whole progress of the game
	"""
	if i == j:
		print("i == j,", player, " take A[i]", A[i])
		scoreDict[player] += A[i]
		print(player, " score: ", scoreDict[player])
		return DP[i][j]
	takeLeft = A[i] - DP[i + 1][j]
	takeRight = A[j] - DP[i][j - 1]
	if takeLeft > takeRight:
		print(player, " take left, ", A[i])
		scoreDict[player] += A[i]
		print(player, " score: ", scoreDict[player])
		print("result string: ", A[i + 1: j+1])

		# call to make move for the next player
		return simulation(i + 1, j, DP, A, playerdict[player])

	else:
		print(player, " take right, ", A[j])
		scoreDict[player] += A[j]
		print(player, " score: ", scoreDict[player])
		print("result string: ", A[i: j])
		# call to make move for the next player
		return simulation(i, j - 1, DP, A, playerdict[player])



A = [ 9, 1, 7, 3, 2, 8, 9, 3]
DP = makeTable(A)
simulation(0, len(A) - 1, DP, A, "Alice")
# output:
# Time: O(n^2)
# [9, 8, 3, 12, 4, 6, 3, 12]
# [None, 1, 6, -3, 5, 3, 6, -3]
# [None, None, 7, 4, 6, 2, 7, 4]
# [None, None, None, 3, 1, 7, 2, 3]
# [None, None, None, None, 2, 6, 3, 0]
# [None, None, None, None, None, 8, 1, 2]
# [None, None, None, None, None, None, 9, 6]
# [None, None, None, None, None, None, None, 3]
#
# Time: O(n^2)
# Alice  take left,  9
# Alice  score:  9
# result string:  [1, 7, 3, 2, 8, 9, 3]
# Bob  take right,  3
# Bob  score:  3
# result string:  [1, 7, 3, 2, 8, 9]
# Alice  take right,  9
# Alice  score:  18
# result string:  [1, 7, 3, 2, 8]
# Bob  take right,  8
# Bob  score:  11
# result string:  [1, 7, 3, 2]
# Alice  take right,  2
# Alice  score:  20
# result string:  [1, 7, 3]
# Bob  take right,  3
# Bob  score:  14
# result string:  [1, 7]
# Alice  take right,  7
# Alice  score:  27
# result string:  [1]
# i == j, Bob  take A[i] 1
# Bob  score:  15
