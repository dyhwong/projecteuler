def eratosthenes(n):
    sieve = [True] * n
    for x in xrange(2, int(n ** 0.5) + 1):
        for i in xrange(2*x, n, x):
            sieve[i] = False
    return sieve

def getPrimes(n):
    sieve = eratosthenes(n)
    array = [i for i in xrange(n) if sieve[i] and i > 1]
    return array

#PRIMES = getPrimes(400)

def factorize(n):
    factors = [1]
    counter = 0
    while True:
        prime = PRIMES[counter]
        if prime ** 2 > n:
            if n != factors[-1]:
                factors.append(n)
            return factors[1:]
        if n % prime == 0:
            n /= prime
            if prime != factors[-1]:
                factors.append(prime)            
        else:
            counter += 1

def totient(n):
    factors = factorize(n)
    for factor in factors:
        n = n * (factor - 1) / factor
    return n

def getHalf(d):
    return d / 2

def getThird(d):
    return d / 3

def gcd(a, b):
    while a:
        a, b = b%a, a
    return b

def main():
    total = []
    for i in xrange(4, 12001):
        for j in xrange(getThird(i) + 1, getHalf(i) + 1):
            if gcd(j, i) == 1:
                total.append([j, i])
    print len(total)

main()
