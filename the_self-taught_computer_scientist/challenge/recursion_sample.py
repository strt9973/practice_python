def count_down(n):
    if n == 1:
        return print(1)
    print(n)
    return count_down(n - 1)

try:
    n = int(input("Enter an integer(greater than or equal to 1): "))
    if n >= 1:
        count_down(n)
    else:
        print("Please, Enter an integer greater than or equal to 1")
except e:
    print(e)