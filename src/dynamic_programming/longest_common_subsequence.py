# given two words, find the lenth of their longest common subsequence

# leetcode problem reference
# https://leetcode.com/problems/delete-operation-for-two-strings/
# https://leetcode.com/problems/longest-common-subsequence/
def print_table(t):
    for row in t:
        print(row)

def lcs(word1, word2):

    m = len(word1) 
    n = len(word2)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]: 
                c[i][j] = c[i-1][j-1] + 1
                # print_table(c)
            else: 
                c[i][j] = max(c[i-1][j], c[i][j-1])
            
    lcs = c[-1][-1]
    return c, lcs

def backtrack_word(c, word1, word2):
    m = len(word1) 
    n = len(word2)
    i = m
    j = n
    s = ''
    while i > 0 and j > 0:
        # print(i,j)
        if word1[i-1] == word2[j-1]:
            s = word1[i-1] + s
            i = i - 1
            j = j -1
        else:
            if c[i][j] == c[i-1][j]: i = i - 1
            else: j = j - 1

    print(s)
    return s


word1, word2 = "leetcode", "etco"
c, length = lcs(word1, word2)
print_table(c)
common_word = backtrack_word(c, word1, word2)
print(f"Word1: {word1}, Word2: {word2} Longest common subsequence: {length}, common subsequence: {common_word}")

word1, word2 = "ijustwantsometea", "teaiswhatyouneed"
c, length = lcs(word1, word2)
print_table(c)
common_word = backtrack_word(c, word1, word2)
print(f"Word1: {word1}, Word2: {word2} Longest common subsequence: {length}, common subsequence: {common_word}")