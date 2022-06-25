n = 100
a = sum(i for i in range(1, n + 1))
b = sum(i**2 for i in range(1, n + 1))
print(str(a**2 - b))