nums = list(map(int, input("Enter integers(separated by space): ").split()))

def assort_even_and_odd(nums):
    even_list = []
    odd_list = []
    for n in nums:
        if n % 2 == 0:
            even_list.append(n)
        else:
            odd_list.append(n)
    return even_list, odd_list

even_list, odd_list = assort_even_and_odd(nums)
print(f"even: {even_list}")
print(f"odd: {odd_list}")