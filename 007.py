
def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if i % i == 0:
            return False
    return True


count = 1
num = 2

while count < 10001:
    num += 1
    if isPrime(num):
        count += 1


print(str(num))