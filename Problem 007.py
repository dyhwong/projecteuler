import math
primes = [2, 3]
x = 5
while len(primes) < 10001:
    for i in primes[1:]:
        if x % i == 0 and i <= int(math.floor(math.sqrt(x))):
            x += 2
            break
    else:
        primes.append(x)
        x += 2
print primes[10000]
        
