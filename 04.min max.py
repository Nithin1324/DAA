def find_min_max_sort(numbers):
    
    if len(numbers) <= 1:
        return numbers
    else:
        
        mid = len(numbers) // 2
        left_sorted = find_min_max_sort(numbers[:mid])
        right_sorted = find_min_max_sort(numbers[mid:])
        
        
        return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_list = []
    left_index, right_index = 0, 0
    

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    
    
    while left_index < len(left):
        sorted_list.append(left[left_index])
        left_index += 1
    
    
    while right_index < len(right):
        sorted_list.append(right[right_index])
        right_index += 1
    
    return sorted_list


numbers_list = [-2,3,4,5,6,7,8,9,18,25,1]
sorted_numbers = find_min_max_sort(numbers_list)
print("Sorted array:", sorted_numbers)
