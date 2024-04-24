#  List Prime Numbers in a Range: Implement a program to list all the prime numbers within a given range.

def is_prime(n, i=2):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

def list_primes(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
print("Prime numbers between", start, "and", end, "are:")
list_primes(start, end)