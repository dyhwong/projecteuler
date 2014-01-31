import math
x = 600851475143
for n in range(1, int(math.floor(math.sqrt(x)))):
    if x % n == 0 and n != 1:
        x /= n
        print x
