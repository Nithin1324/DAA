def count_digits(num):
    if num == 0:
        return 0
    return 1 + count_digits(num // 10)
def is_armstrong(num, digit_count):
    if num == 0:
        return 0
    return ((num % 10) ** digit_count) + is_armstrong(num // 10, digit_count)
def check_armstrong(num):
    digit_count = count_digits(num)
    return num == is_armstrong(num, digit_count)
number = int(input("Enter a number: "))
print(check_armstrong(number))
