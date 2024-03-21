def left_triangle_numbers(n):
    triangle = []
    for i in range(1, n + 1):
        row = [str(x) for x in range(1, i + 1)]
        triangle.append(' '.join(row))
    return triangle

# Example usage:
n = int(input())
print('\n'.join(left_triangle_numbers(n)))
