def find_min_max(numbers):
    if not numbers:
        print("The list is empty.")
        return

    min_value = max_value = numbers[0]  

    for num in numbers:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num

    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")

try:
    input_numbers = input("Enter a list of numbers (separated by spaces): ")
    number_list = [float(num) for num in input_numbers.split()]
    find_min_max(number_list)
except ValueError:
    print("Invalid input. Please enter valid numeric values.")

 
