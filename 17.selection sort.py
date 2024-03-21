def quick_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

try:
    user_input = input("Enter space-separated numbers: ")
    arr = list(map(int, user_input.split()))
    quick_sort(arr)
    print("Sorted array (ascending order):", arr)
except ValueError:
    print("Invalid input. Please enter a list of space-separated numbers.")
