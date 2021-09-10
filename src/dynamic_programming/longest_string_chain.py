# https://leetcode.com/problems/longest-string-chain/

# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 
# to make it equal to word2. For example, "abc" is a predecessor of "abac".

# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor 
# of word_2, word_2 is a predecessor of word_3, and so on.

def longest_string_chain(words):
	words.sort(key=lambda x: len(x), reverse=True)

	# we add a set containing all words so that we check if a word exists in O(1)
	word_set = set()
	dc = {}
	for w in words:
	    word_set.add(w)
	    dc[w] = 0
	    
	# For each word in order of length, for each word2 which is word with one character removed,
	# length[word2] = max(length[word2], length[word] + 1).
	for w in words:
	    # print(w)
	    for i in range(len(w)):
	        s = w[:i] + w[i+1:]
	        # print(f"\t {s}")
	        if s in word_set:
	            dc[s] = max(dc[s], dc[w] + 1)

	return max(dc.values()) + 1

words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
lsc = longest_string_chain(words)
print(words)
print(f"Longest String Chain: {lsc}")

words = ["a","b","ba","bca","bda","bdca"]
lsc = longest_string_chain(words)
print(words)
print(f"Longest String Chain: {lsc}")