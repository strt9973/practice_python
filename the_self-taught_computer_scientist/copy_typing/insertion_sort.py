int_list = list(map(int, input("Enter integers(separated by space): ").split()))

def insertion_sort(int_list):
    for i in range(1, len(int_list)):
        value = int_list[i]
        while i > 0 and int_list[i-1] > value:
            int_list[i] = int_list[i-1]
            i = i - 1
        int_list[i] = value
    return int_list

print(insertion_sort(int_list))
