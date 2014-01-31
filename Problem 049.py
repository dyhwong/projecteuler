from math import sqrt

def isPrime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def sieve(m, n):
    sieve = [True] * n
    for x in xrange(2, int(n ** 0.5) + 1):
        for i in xrange(2*x, n, x):
            sieve[i] = False
    sieve[0], sieve[1] = False, False
    primes = []
    for i in xrange(len(sieve)):
        if sieve[i]:
            primes.append(i)
    for i in xrange(len(primes)):
        if primes[i] > m:
            return primes[i:]

def isPermutation(list1):
    digits = []
    for digit in str(list1[0]):
        digits.append(int(digit))
    digits.sort()
    digits2 = []
    for digit in str(list1[1]):
        digits2.append(int(digit))
    digits2.sort()
    digits3 = []
    for digit in str(list1[2]):
        digits3.append(int(digit))
    digits3.sort()
    if digits == digits2:
        if digits == digits3:
            return True
    return False

def concatenate(list1):
    string = ""
    for i in list1:
        string += str(i)
    return int(string)

def buildList():
    primes = sieve(1000, 10000)
    newList = []
    for i in xrange(len(primes)):
        for j in primes[i + 1:]:
            if 2 * j - primes[i] in primes:
                if isPermutation([primes[i], j, 2 * j - primes[i]]):
                    newList.append([primes[i], j, 2 * j - primes[i]])
    return newList

def main():
    print concatenate(buildList()[1])
    
main()
