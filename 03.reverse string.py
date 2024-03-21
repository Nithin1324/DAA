def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])
input_string = "hello"
reversed_string = reverse_string(input_string)
print(f"The reversed string of '{input_string}' is '{reversed_string}'.")
