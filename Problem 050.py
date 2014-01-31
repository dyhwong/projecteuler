def sieve(n):
    sieve = [True] * n
    for x in xrange(2, int(n ** 0.5) + 1):
        for i in xrange(2*x, n, x):
            sieve[i] = False
    sieve[0], sieve[1] = False, False
    primes = []
    for i in xrange(len(sieve)):
        if sieve[i]:
            primes.append(i)
    return primes


def findMax():
    primes = sieve(1000000)
    for i in xrange(len(primes) - 1):
        total = primes[i]
        count = 1
        while total + primes[i + count]< 1000000:
            total += primes[i + count]
            count += 1
        if total in primes:
            return total, count

print findMax()
