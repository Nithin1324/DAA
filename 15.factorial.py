def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)

try:
    num = int(input("Enter a positive integer: "))
    if num < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {num} is {recur_factorial(num)}")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
