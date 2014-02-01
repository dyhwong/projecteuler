from math import sqrt

def isPrime(n):
    for i in range(3, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
        else:
            i += 2
    return True

def concatenate(a, b):
    return int(str(a) + str(b))

def isconcatPrime(a, b):
    if isPrime(concatenate(a, b)) and isPrime(concatenate(b, a)):
        return True
    return False

def eratosthenes(n):
    sieve = [True] * n
    for x in xrange(2, int(n ** 0.5) + 1):
        for i in xrange(2*x, n, x):
            sieve[i] = False
    return sieve

def getPrimes(sieve):
    primes = []
    for i in xrange(2, len(sieve)):
        if sieve[i]:
            primes.append(i)
    return primes

def addPrime(primeList, primes):
    newList = []
    for i in xrange(primes.index(primeList[-1]) + 1, len(primes)):
        for prime in primeList:
            if not isconcatPrime(prime, primes[i]):
                break
            elif prime == primeList[-1]:
                tempList = primeList + [primes[i]]
                newList.append(tempList)
    return newList

def main():
    primes = getPrimes(eratosthenes(10000))
    newList = []
    for primeList in primes[:50]:
        newList += addPrime([primeList], primes)
    newList2 = []
    for primeList in newList:
        newList2 += addPrime(primeList, primes)
    newList = []
    for primeList in newList2:
        newList += addPrime(primeList, primes)
    newList2 = []
    for primeList in newList:
        newList2 += addPrime(primeList, primes)
    print sum(newList2[0])
    
main()
