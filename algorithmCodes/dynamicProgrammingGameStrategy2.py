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
            for k in range(1, j-i+1):
                # player1 took k from left,
                # sum of left - player2's max score in DP(i+k,j)
                left = sum(A[i: i+k+1]) - DP[i+k][j]
                # player2 took k from right,
                # sum of right - player2's max score in DP(i, j-k)
                right = sum(A[i+k+1: j])-DP[i][j-k]
                theMax = max(left, right)
            DP[i][j] = theMax

    return DP



# output
# [3, 3, 8, 12, 13, 11, 17, 19, 23]
# [None, 5, 5, 9, 10, 8, 14, 16, 20]
# [None, None, 4, 4, 5, 3, 9, 11, 15]
# [None, None, None, 1, 1, -1, 5, 7, 11]
# [None, None, None, None, -2, 2, 4, 6, 10]
# [None, None, None, None, None, 6, 6, 8, 12]
# [None, None, None, None, None, None, 2, 2, 6]
# [None, None, None, None, None, None, None, 4, 4]
# [None, None, None, None, None, None, None, None, 8]
