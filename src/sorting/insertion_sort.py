def insertion_sort(arr):

    for i in range(1, len(arr)):
        print(f"Starting at element {i}")
        print(f"List before iteration {arr}")
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
        print(f"List after iteration {arr}")
    
    return arr

arr = [1, 0, 4, 3, -1]
insertion_sort(arr)