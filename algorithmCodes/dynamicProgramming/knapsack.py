"""
from cs161 note 22
Knapsack Problem
1. input: collection of n items, each with a size and value.
L: limit on total size of a solution

2. goal: choose some of the items, keeping total size of choosen items <= L that
    maximizing total value of chosen items

3. special case: if size = value, then goal is to find combination of items as close as possible to L
    without going over
"""
from collections import namedtuple

Item = namedtuple('Item', ['name', 'size', 'value'])
L = 8
items = [Item("A", 2, 4),
         Item("B", 3, 5),
         Item("C", 4, 6),
         Item("D", 4, 7),
         Item("E", 6, 8)]

"""
Two important variations:
1. Fractional Knapsack:
can include part of an item (any fraction 0 <= x <= 1)
    => that fraction of both size and value.
        * Fairly easy, using greedy algorithm

"""


def fractionalSol(items: [Item], L: int):
	# sort items by decreasing value/size
	items.sort(key = lambda item: -item.value / item.size)
	output = []
	remainingSpace = L
	for x in items:
		if remainingSpace == 0:
			break
		xAmount = min(x.size, remainingSpace)
		remainingSpace -= xAmount
		output.append(Item(x.name, size = xAmount, value = x.value))
	
	return output


print(fractionalSol(items, L))
"""
0-1 Knapsack:
Each item must either be completely included or excluded
Dynamic programming algorithm
Time = O(nL) not polynomial in # bits of input (uses L, not logL)
	when sizes and size limits are integers
*** "Weakly" NP-complete: NP-complete for huge integer inputs

dynamic programming solution to 0-1 knapsack
1. parameters of inlput: n(#items), L(total size)
2. define subproblem(i,s) = first i items(prefix of input),total size s<=L
3. construct a recurrence for K(i, s)= max value possible for subproblem(i,s)
4. two possibilities:
	1) optimal solution includes ith item, then its value
		is value (ith item) + K(i-1, s-size(ith item)))
	3) otherwise value is K(i-1, s)
5. base case K(0,s) = K(i,0) = 0
6. the recurrence:
K(i,s) = 0 if i == 0 or s < 0
		= max(K(i-1,s), value(ith item)+K(i-1, s-size(ith item))) otherwise
"""


# DP = [[None] * len(items) for _ in range(L + 1)]
def dpKnapsack(items: [Item], L: int):
	n = len(items)
	DP = [[None] * (L + 1) for _ in range(n + 1)]
	for i in range(n + 1):
		DP[i][0] = 0
	for s in range(L + 1):
		# if s < n:
		DP[0][s] = 0
	
	for i in range(1, n + 1):
		for s in range(1, L + 1):
			if s - items[i - 1].size >= 0:
				DP[i][s] = max(DP[i - 1][s], items[i - 1].value + DP[i - 1][s - items[i - 1].size])
			else:
				DP[i][s] = DP[i - 1][s]
	return DP


def dpKnapsackSol(items: [Item], L: int):
	DP = dpKnapsack(items, L)
	i = len(items)
	s = L
	output = []
	while i > 0 and s > 0:
		if s - items[i - 1].size >= 0 and DP[i - 1][s] < (items[i-1].value + DP[i - 1][s - items[i - 1].size]):
			# means take this item
			output.append(items[i - 1])
			s -= items[i - 1].size
		i -= 1

	return output


DP = dpKnapsack(items, L)
for i in range(len(DP)):
	print(DP[i])
print(dpKnapsackSol(items, L))
