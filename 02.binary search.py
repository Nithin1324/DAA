def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

try:
    user_input = int(input("Enter the target value: "))
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    result = binary_search(sorted_array, user_input)

    if result != -1:
        print(f"Target {user_input} found at index {result}.")
    else:
        print(f"Target {user_input} not found in the array.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
