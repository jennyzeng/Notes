import sys


def bsinsert(ns, e):
    if len(ns) == 0:
        ns.append(e)
        return
    l, r = 0, len(ns)-1
    m = 0
    while l < r:
        m = (l + r) // 2
        if ns[m] > e:
            r = m - 1
        else:
            l = m + 1
    if ns[l] > e:
        ns.insert(l, e)
    else:
        ns.insert(l+1, e)


def getMed():
    mid = (len(result)) // 2
    if len(result) & 1:  # odd
        return result[mid]
    else:
        return (result[mid-1] + result[mid]) / 2

n = int(input().strip())
result = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    bsinsert(result, a_t)
    print("{0:.1f}".format(getMed()))


"""
6
12
4
5
3
8
7
"""