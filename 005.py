import math
r = 1
for i in range(2, 21):
    r = r * i // math.gcd(r, i)

print(r)