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



# L: list of houses values (can be positive or negative)
L = [-3, 10, 2, -5, 7, -1, -2, -1, -3]  # example input
# T: table where we store already computed subproblems
DP = [[None] * len(L) for _ in range(len(L))]  # init DP empty


# memoiation TODO: time complexity analysis
def makeTable1(i, j):
	# Base case
	if i > j:
		return 0
	if DP[i][j] is None:
		if i == j:
			DP[i][j] = L[i]
		else:
			maxValue = -99999
			# left side
			for k in range(i, j + 1):
				takeLeft = sum(L[i: k + 1]) - makeTable1(k + 1, j)
				maxValue = max(takeLeft, maxValue)
				takeRight = sum(L[k: j + 1]) - makeTable1(i, k - 1)
				maxValue = max(takeRight, maxValue)
			DP[i][j] = maxValue
	return DP[i][j]


# # TODO: non recursive version, not working
#
# def makeTable2(i, j):
# 	for i in range(len(L)):  # only have one slice left.
# 		DP[i][i] = L[i]
#
# 	for s in range(2, len(L) + 1):  # number of slices left
# 		for i in range(0, len(L) - s + 1):  # left start point
# 			j = i + s - 1  # right end point
# 			maxValue = -99999
# 			for k in range(i, j + 1):
# 				takeLeft = sum(L[i:k + 1]) - DP[k + 1][j]
# 				takeRight = sum(L[k: j + 1]) - DP[i][k]
# 				maxValue = max(takeLeft, takeRight, maxValue)
# 			DP[i][j] = maxValue
# 		# return DP[i][j]


def makeMove(i, j, DP, L):
	"""
	it will make move when there is A(i, j)
	return list of indexes of the houses that the player will pick.
	"""
	if i > j:
		return
	if i == j:
		print([i])
		return [i]
	takeLeftMax = -999999
	takeLeftK = 0
	takeRightMax = -999999
	takeRightK = 0
	for k in range(i, j + 1):
		takeLeft = sum(L[i:k + 1]) - (DP[k + 1][j] if k + 1 <= j else 0)
		if takeLeftMax < takeLeft:
			takeLeftMax = takeLeft
			takeLeftK = k
		takeRight = sum(L[k:j + 1]) - (DP[i][k - 1] if k - 1 >= i else 0)
		if takeRightMax < takeRight:
			takeRightMax = takeRight
			takeRightK = k
	if takeLeftMax >= takeRightMax:
		# take left
		print([x for x in range(i, takeLeftK + 1)])
		return makeMove(takeLeftK + 1, j, DP, L)
	else:
		# take right
		print([x for x in range(takeRightK, j + 1)])
		return makeMove(i, takeRightK - 1, DP, L)


makeTable1(0, len(L) - 1)
for i in range(len(DP)):
	print(DP[i])
makeMove(0, len(L) - 1, DP, L)

# output
# [-3, 13, 15, 14, 17, 16, 14, 13, 12]
# [None, 10, 12, 17, 14, 15, 15, 16, 15]
# [None, None, 2, 7, 4, 5, 5, 6, 5]
# [None, None, None, -5, 12, 11, 9, 8, 5]
# [None, None, None, None, 7, 8, 8, 9, 8]
# [None, None, None, None, None, -1, 1, -2, -1]
# [None, None, None, None, None, None, -2, 1, 0]
# [None, None, None, None, None, None, None, -1, 2]
# [None, None, None, None, None, None, None, None, -3]

# [0, 1, 2, 3, 4]
# [5]
# [6, 7]
# [8]
