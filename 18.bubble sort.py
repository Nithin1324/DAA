def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

try:
    user_input = input("Enter space-separated numbers: ")
    lst = list(map(int, user_input.split()))
    bubble_sort(lst)
    print("Sorted array (ascending order):", lst)
except ValueError:
    print("Invalid input. Please enter a list of space-separated numbers.")
