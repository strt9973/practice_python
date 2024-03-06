int_list = list(map(int, input("Enter integers(separated by space): ").split()))

def bubble_sort(int_list):
    loop_size = len(int_list) - 1
    for i in range(loop_size):
        for j in range(loop_size): 
            if int_list[j] > int_list[j + 1]:
                int_list[j], int_list[j + 1] = int_list[j + 1], int_list[j]

    return int_list

sorted_int_list = bubble_sort(int_list)
print(sorted_int_list)
        