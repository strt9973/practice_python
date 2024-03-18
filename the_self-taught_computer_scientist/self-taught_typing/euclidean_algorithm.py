int_list = list(map(int, input("Enter integers(separated by space and only two integers): ").split()))

def eucidian_algorithm(i1, i2):
    remainder = i1 % i2
    if remainder != 0:
        return eucidian_algorithm(i2, remainder)
    
    return i2

print(eucidian_algorithm(int_list[0], int_list[1]))