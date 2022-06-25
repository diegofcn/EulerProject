
sum = 0
x = 1
y = 2
while y < 4000000:
        x, y = y, x + y
        if x % 2 == 0:
            sum += x


print(str(sum))