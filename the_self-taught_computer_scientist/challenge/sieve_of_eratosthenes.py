import math

n = int(input("Enter an integer(greater than or equal to 2): "))

def create_n_dict(n):
    n_dict = {}
    for i in range(2, n + 1):
        n_dict[i] = True
    return n_dict

def sieve_of_eratosthenes(n_dict, n):
    max_i = int(math.sqrt(n)) + 1
    for k in range(2, max_i):
        if n_dict[k]:
            for l in range(k ** 2, n+1 ,k):
                n_dict[l] = False
    return [prime for prime, is_prime in n_dict.items() if is_prime]

n_dict = create_n_dict(n)
prime_list = sieve_of_eratosthenes(n_dict, n)
print(f"prime_list: {prime_list}")
if n in prime_list:
    print(f"{n} is prime number.")
else:
    print(f"{n} is not prime number.")