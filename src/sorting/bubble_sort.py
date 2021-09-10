def bubble_sort(arr):
    for i in range(len(arr)-1):
        print(f"Starting at element {i}")
        print(f"List before iteration {arr}")
        for j in range(len(arr) -i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(f"List after iteration {arr}")

arr = [1, 0, 4, 3, -1]
bubble_sort(arr)