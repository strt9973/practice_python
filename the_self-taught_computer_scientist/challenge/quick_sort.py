int_list = list(map(int, input("Enter integers(separated by space): ").split()))

def partition(int_list, min, max):
    pivot = int_list[min]
    left = min - 1
    right = max + 1

    while True:
        while True:
            left += 1
            if int_list[left] >= pivot:
                break
        while True:
            right -= 1
            if int_list[right] <= pivot:
                break
        if left >= right:
            print(int_list)
            return right
        
        int_list[left], int_list[right] = int_list[right], int_list[left]


def quick_sort(int_list, min, max):
    if min < max:
        part = partition(int_list, min, max)
        quick_sort(int_list, min, part)
        quick_sort(int_list, part + 1, max)


quick_sort(int_list, 0 ,len(int_list) - 1)
print(int_list)

