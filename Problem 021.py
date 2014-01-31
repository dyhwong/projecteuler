import math
def proper_divisors(n):
    divisors = []
    for i in range(2, int(math.floor(math.sqrt(n)))):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n/i)
    divisors.append(1)
    return divisors

amicable_numbers = []
for j in range(1, 10000):
    if sum(proper_divisors(sum(proper_divisors(j)))) == j and sum(proper_divisors(j)) != j:
        amicable_numbers.append(j)

print sum(amicable_numbers)
