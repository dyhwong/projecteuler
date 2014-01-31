import math

def triangular(n):
    return n * (n + 1) / 2

def check_divisors(divisors):
    if len(divisors) > 500:
        return True

n = 0
divisors = []
while check_divisors(divisors) != True:
    n += 1
    divisors = []
    for i in range(1, int(math.floor(math.sqrt(triangular(n)))) + 1):
        if triangular(n) % i == 0:
            divisors.append(i)
            if triangular(n) / i != i:
                divisors.append(triangular(n)/i)
print triangular(n)
