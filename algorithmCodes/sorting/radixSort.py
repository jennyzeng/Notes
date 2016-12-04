
"""
from cs 161 note 10
radix sort
1. choose a base b
2. represent keys (of values to be sorted in base b)
3. do a loop:
	for i = 0, 1, ...(max # of digits):
		bucket sort input (starting from output of previous iteration by b's digit
		(e.g. in decimal: sort by 1's, then 10's, then 100's digit)
Time analysis:
repeated bucket sorts with b buckets (b is the base)
O(n+b) per bucket sort
repetitions = # of digits of a number in range(0,..., N-1) in base b
	= celling(log_b N)
Total = O((n+b) * celling(log_b N)


base of number system:
	e.g. decimal system - 10 as its radix (radix-10)

Warm up: How to convert a number to base B
1. base b representation of x (assume x >= 0):
	if x >= b:
		output base b representation of x//b
	output x % b
"""


def radixSort(items, radix):
	maxDigits = max(len(i[1]) for i in items)
	for i in range(maxDigits):
		buckets = [[] for _ in range(radix)]
		for item in items:
			if i >= len(item[1]):
				buckets[0].append(item)
			else:
				buckets[int(item[1][len(item[1]) - 1 - i])].append(item)
		items = []
		for bucket in buckets:
			for item in bucket:
				items.append(item)
	return items


items = [("A", "3521"), ("B", "99999"), ("C", "221"), ("D", "389"), ("E", "911"), ("F", "217"),
         ("G", "682"), ("H", "499"), ("I", "3213"), ("J", "604"), ("K", "504"), ("L", "811"),
         ("M", "904")]
print(radixSort(items, 10))


def convertBase(x, base):
	output = ""

	while int(x) >= base:
		output = str(int(x) % base) + output
		x = str(int(x) // base)

	output = str(int(x) % base) + output
	return output

def convertBinToHex(x):
	output = 0
	digit = 0
	while x!= "":
		if x[-1] == "1":
			output += pow(2, digit)
		digit+=1
		x = x[:-1]
	return output

print(convertBase("324", 2))
print(convertBase("100", 16))
print(convertBinToHex("101000100"))