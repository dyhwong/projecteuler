from math import sqrt

def isPrime(n):
    for i in range(3, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
        else:
            i += 2
    return True

def upperRight(n):
    return 4 * (n ** 2) - 2 * n + 1

def upperLeft(n):
    return 4 * (n ** 2) + 1

def bottomLeft(n):
    return 4 * (n ** 2) + 2 * n + 1

def getDiagonals(n):
    return 4 * n + 1

def getSideLength(n):
    return 2 * n + 1

def main():
    primes = 3
    count = 1
    while primes * 100.0 / getDiagonals(count) > 10.0:
        count += 1
        if isPrime(upperRight(count)):
            primes += 1
        if isPrime(upperLeft(count)):
            primes += 1
        if isPrime(bottomLeft(count)):
            primes += 1
    print getSideLength(count)

main()
