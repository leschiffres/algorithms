def is_palindrome_slow(s):
	return s == s[::-1]

def is_palindrome(s):
	# if len(s) == 1:
	# 	return True
	for i in range(len(s)//2):
		print(i, len(s)-i-1)
		if s[i] != s[len(s)-i-1]:
			return False
	return True

strs = ['a', 'ab', 'aba', 'abba', 'abcba', 'abcd', 'abcbb']
for s in strs:
	print(s, is_palindrome(s))
