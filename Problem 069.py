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

PRIMES = getPrimes(4000)

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

def getRatio(n):
    return float(n) / totient(n)

def main():
    maximum = 1
    ans = 0
    for i in xrange(2, 1000001):
        ratio = getRatio(i)
        if ratio > maximum:
            ans = i
            maximum = ratio
    print ans
main()
