# retrieves the index of a target in an array in O(log n) steps
def binary_search(arr, target):
	i, j = 0, len(arr)-1
	
	while i <= j:
		pos = (i + j) // 2

		if arr[pos] == target:
			return pos
		elif arr[pos] < target:
			i = pos + 1
		else:
			j = pos - 1
	return -1 

# arr = [1,3,5,6]
# print(binary_search(arr, 1))
# print(binary_search(arr, 3))
# print(binary_search(arr, 7))

# arr = [4, 18, 32, 33, 49, 100, 102]
# print(binary_search(arr, 102))
# print(binary_search(arr, 33))
# print(binary_search(arr, 50))