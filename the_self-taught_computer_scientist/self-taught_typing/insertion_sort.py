int_list = list(map(int, input("Enter integers(separated by space): ").split()))

def sort(int_list, i):
    for j in reversed(range(i)):
        if j == 0:
            return int_list
        if int_list[j-1] > int_list[j]:
            int_list[j-1], int_list[j] = int_list[j], int_list[j-1]
        else:
            return int_list

def insertion_sort(int_list):
    for i in range(1, len(int_list) + 1):
        sort(int_list, i)
    
    return int_list

print(insertion_sort(int_list))
