import math

def eratosthenes(n):
    sieve = [i for i in range(2, n + 1)]
    for i in sieve:
        for j in sieve:
            if j % i == 0 and j / i >= 2:
                sieve.remove(j)
    return sieve

def isPrime(n):
    if n % 2 == 0 or n < 0:
        return False
    divisor = 3
    while divisor <= math.sqrt(n):
        if n % divisor == 0:
            return False
            break
        else:
            divisor += 2
    return True

def findMaxPrimes(a, b):
    prime = True
    count = 0
    while prime:
        count += 1
        prime = isPrime(count**2 + a*count + b)
    return count

def findCoeff(n):
    maxPrimes = 0
    a, b = 0, 0
    for x in range(-n + 1, n):
        for y in eratosthenes(n):
            if findMaxPrimes(x, y) > maxPrimes:
                maxPrimes = findMaxPrimes(x, y)
                a, b = x, y
    return a * b

def main():
    print findCoeff(1000)

main()
        
        
    

