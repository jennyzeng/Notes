"""
variant of coins-in-a-line game called houses-in-a-row

In this game, two real estate moguls, Alice and Bob, take turns divvying
up n houses that are lined up in a row, with Alice going first. When it is a player’s
turn, he or she must choose one or more of the remaining houses, starting from
either the left end of the row or the right, with the set of houses he or she picks
in this turn being consecutive. For example, in a row of houses numbered 1
to 100, Alice could choose houses numbered 1, 2, and 3 in her first turn, and,
following that, Bob could choose houses numbered 100 and 99 in his first turn,
which could be then followed by Alice choosing house number 98, and so on,
until all the houses are chosen. There is no limit on the number of houses that
Alice or Bob can choose during a turn, but the values of the houses can be either
positive or negative. For instance, a house could have a negative value if it is
contains a hazardous waste site that costs more to clean up than the house is worth.
Describe an efficient algorithm for determining how Alice can maximize
the total net value of all the houses she chooses, assuming Bob plays optimally
as well. What is the running time of your algorithm?
"""


# we can still have i and j to represent the start and the end for the house line.
# but every time the number of houses reduced may be different.
# value (i,j,k) = max(A[i]+...A[i+k-1] - value(i+k, j),
# 						A[j] + ... + A[j-k+1] - value(i, j -k))
# k range is from 1 to num of houses left

def makeTable(A):
	# initialize the value table
	DP = []
	for i in range(len(A)):
		aList = []
		for j in range(len(A)):
			aList.append(None)
		DP.append(aList)
	# i is the the left start point of the line with houses left
	for i in range(len(A)):
		DP[i][i] = A[i]

	for s in range(2, len(A) + 1):
		# s is the num of houses left
		for i in range(0, len(A) - s + 1):
			# j is the right end point of the line with houses left
			j = i + s - 1
			theMax = None
			for k in range(1, s):
				# player1 took k from left,
				# sum of A(i, i+k-1) - player2's max score in DP(i+k,j)
				left = sum(A[i: i + k]) - DP[i + k][j]
				# player2 took k from right,
				# sum of A(j-k+1, j) - player2's max score in DP(i, j-k)
				right = sum(A[j - k + 1: j + 1]) - DP[i][j - k]
				theMax = max(left, right)
			DP[i][j] = theMax
	return DP


def makeMove(i, j, DP, A):
	"""
	it will make move when there is A(i, j)
	return list of indexes of the houses that the player will pick.
	"""
	if i == j:
		return [i]
	theMax = None
	kMark = None
	indexMark = None

	for k in range(1, j - i + 1):
		left = sum(A[i: i + k]) - DP[i + k][j]
		right = sum(A[j - k + 1: j + 1]) - DP[i][j - k]
		if theMax == None or theMax < max(left, right):
			theMax = max(left, right)
			if left > right:
				indexMark = i
				kMark = k
			else:
				indexMark = j
				kMark = k
	if indexMark == i:
		return [indexMark + h for h in range(0, kMark)]
	else:
		return [indexMark - h+1 for h in range(kMark, 0, -1)]
#
# TODO: fix codes of simulation
# player1 = "Alice"
# player2 = "Bob"
# playerdict = {player1: player2, player2: player1}
# scoreDict = {player1: 0, player2: 0}
#
#
# def simulation(i, j, DP, A, player):
# 	"""
# 	It will simulate the whole progress of the game
# 	"""
# 	if i == j:
# 		print("i == j,", player, " take [", j,"]")
# 		scoreDict[player] += A[i]
# 		print(player, " score: ", scoreDict[player])
# 		return DP[i][j]
# 	theMax = None
# 	kMark = None
# 	indexMark = None
# 	for k in range(1, j - i + 1):
# 		left = sum(A[i: i + k]) - DP[i + k][j]
# 		right = sum(A[j - k + 1: j + 1]) - DP[i][j - k]
# 		if theMax == None or theMax < max(left, right):
# 			theMax = max(left, right)
# 			if left > right:
# 				indexMark = i
# 				kMark = k
# 			else:
# 				indexMark = j
# 				kMark = k
# 	if indexMark == i:
# 		print(player, "take: ", [indexMark + h for h in range(0, kMark)])
# 		scoreDict[player] += sum(A[i:i+k])
# 		print(player, " score: ", scoreDict[player])
# 		return simulation(i + kMark, j, DP, A, playerdict[player])
# 	else:
# 		print(player, "take: ", [indexMark-h+1 for h in range(kMark, -1, -1)])
# 		scoreDict[player] += sum(A[j - k + 1: j + 1])
# 		print(player, " score: ", scoreDict[player])
# 		return simulation(i, j - kMark, DP, A, playerdict[player])
# #(i, j -k)
#
A = [-3, 10, 2, -5, 7, -1, -2, -1, -3]
DP = makeTable(A)
for i in range(len(DP)):
	print(DP[i])
print(makeMove(6, len(A)-1, DP, A))
# simulation(0, len(A) - 1, DP, A, player1)

# output

# [-3, 13, 15, 14, 17, 16, 14, 13, 10]
# [None, 10, 8, 17, 0, 15, 15, 12, 13]
# [None, None, 2, 7, 0, 5, 5, 2, 3]
# [None, None, None, -5, 12, 11, 9, 8, 5]
# [None, None, None, None, 7, 8, 8, 5, 6]
# [None, None, None, None, None, -1, 1, -2, -1]
# [None, None, None, None, None, None, -2, 1, 0]
# [None, None, None, None, None, None, None, -1, 2]
# [None, None, None, None, None, None, None, None, -3]