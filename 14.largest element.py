def largest(arr, n):
    arr.sort()
    return arr[n - 1]

arr = input("Enter space-separated numbers: ")
arr = arr.split()
n = len(arr)
print("Largest in given array:", largest(arr, n))
