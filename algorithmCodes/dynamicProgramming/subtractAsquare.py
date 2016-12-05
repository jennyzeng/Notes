"""
from cs161 note20
subtract a square
Game position: pile of counters
move: take away a square number of counters (any square)
goal: win by moving to zero left (take all remaining counters)

value = +1 if player who is about to move wins
		-1 if player who is about to move is losing
value(n) = max (- value(n-s)) for s = 1,4,9...
positions with value -1( the ones you want to move to): 0,2,5,7,10,12,..
"""
import math
import random


def value(n):
	DP = [None for _ in range(n + 1)]
	DP[0] = -1  # base case. when nothing left, lose
	for i in range(1, n + 1):
		DP[i] = max(-DP[i - s ** 2] for s in range(1, math.floor(math.sqrt(i)) + 1))
	return DP
# time: O(n*n^(1/2)) = O(n^(3/2))

def simulation(n):
	if n == 0:
		print("n=0, win")
		return
	DP = value(n)
	print("- current DP: ", DP)
	for s in range(math.floor(math.sqrt(n)), 0, -1):    # we want to win fast, so pick as many as possible
		if DP[n - s ** 2] == -1:    # we want to go to positions with value -1, so opponent will lose
			print("have win positions, pick ", s ** 2, "left: ", n - s ** 2)
			simulation(n - s ** 2)
			return
	s = random.randint(1, math.floor(math.sqrt(n)))
	print("loosing, pick random: ", s ** 2)
	simulation(n - s ** 2)


simulation(18)
