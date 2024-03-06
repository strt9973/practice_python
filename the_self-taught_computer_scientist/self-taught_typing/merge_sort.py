int_list = list(map(int, input("Enter integers(separated by space): ").split()))

def sort(left, right):
    sorted_list = []
    left_value = left.pop(0)
    right_value = right.pop(0)
    while left_value or right_value:
        if left_value and right_value:
            if left_value > right_value:
                sorted_list.append(right_value)
                right_value = right.pop(0) if len(right) else None
            elif left_value < right_value:
                sorted_list.append(left_value)
                left_value = left.pop(0) if len(left) else None
        elif left_value:
            sorted_list.append(left_value)
            left_value = None
        elif right_value:
            sorted_list.append(right_value)
            right_value = None

    if len(left) > 0:
        sorted_list += left
    if len(right) > 0:
        sorted_list += right
    return sorted_list 

def merge_sort(splited_int_list):
    length = len(splited_int_list)
    median = length // 2
    left = splited_int_list[:median]
    right = splited_int_list [median:]
    
    if len(left) == 1 and len(right) == 1:
        return sort(left, right)
    
    if len(left) == 1:
        right = merge_sort(right)
        return sort(left, right)
    
    if len(right) == 1:
        left = merge_sort(left)
        return sort(left, right)
    
    left = merge_sort(left)
    right = merge_sort(right)
    return sort(left, right)

print(merge_sort(int_list))
