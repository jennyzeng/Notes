"""
Given document, return pairs of (word, # occurrences)
Hash Table
"""
words = ["hello", "world", "hello", "human", "we", "are", "human", "world"]

def pairsOfWords(input):
	counter = {}
	for word in input:
		if word in counter:
			counter[word] += 1
		else:
			counter.update({word: 1})
	return counter

print(pairsOfWords(words))
# Time complexity: O(n)