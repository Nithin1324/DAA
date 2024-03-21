def copy_string(input_string):
    if len(input_string) == 0:
        return ''
    else:
        return input_string[0] + copy_string(input_string[1:])

user_input = input("Enter a string: ")
copied_str = copy_string(user_input)
print("Original String:", user_input)
print("Copied String:", copied_str)
