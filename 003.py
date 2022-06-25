import math

def isPrime(num):
    for i in range(2, int (math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def largest_prime(num):
    for i in range(int(num ** 0.5)+1, 0, -1):
        if num % i == 0 and isPrime(i):
            return i

print(largest_prime(600851475143))