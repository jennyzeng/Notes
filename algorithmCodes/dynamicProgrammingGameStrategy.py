# game strategy for coins-in-a-line or a pizza game
# coins in a line, value of coins


def makeTable(line):
    value = []  # value table
    # initialize the value table
    for i in range(len(line)):
        aList = []
        for j in range(len(line)):
            aList.append(None)
        value.append(aList)

    # calculate values for table
    for i in range(len(line)):
        value[i][i] = line[i]
    for s in range(2, len(line) + 1):
        for i in range(0, len(line) - s + 1):
            j = i + s - 1
            value[i][j] = max(line[i] - value[i + 1][j],
                              line[j] - value[i][j - 1])

    # print the result value table
    # j horizontal, i vertical
    for i in range(len(line)):
        print(value[i])

    print("\nTime: O(n^2)")
    return value


def makeMove(i, j, value, line):
    if i == j:
        print("i == j, ", line[i])
        return line[i]
    takeLeft = line[i] - value[i + 1][j]
    takeRight = line[j] - value[i][j - 1]
    if takeLeft > takeRight:
        print("take left, ", takeLeft)
        print("result string: ", line[i + 1: j])
        makeMove(i + 1, j, value, line)

    else:
        print("take right, ", takeRight)
        print("result string: ", line[i: j - 1])
        makeMove(i, j - 1, value, line)


line = [9, 1, 7, 3, 2, 8, 9, 3]
# line = [3, 5, 4, 1]
value = makeTable(line)
makeMove(0, len(line) - 1, value, line)
# output:
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
# take left,  12
# result string:  [1, 7, 3, 2, 8, 9]
# take right,  -3
# result string:  [1, 7, 3, 2, 8]
# take right,  6
# result string:  [1, 7, 3, 2]
# take right,  3
# result string:  [1, 7, 3]
# take right,  5
# result string:  [1, 7]
# take right,  -3
# result string:  [1]
# take right,  6
# result string:  []
# i == j,  1


# [3, 2, 2, 1]
# [None, 5, 1, 2]
# [None, None, 4, 3]
# [None, None, None, 1]
#
# Time: O(n^2)
# take left,  1
# result string:  [5, 4]
# take left,  2
# result string:  [4]
# take left,  3
# result string:  []
# i == j,  1
