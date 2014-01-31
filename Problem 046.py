from math import sqrt

def isPrime(n):
    for i in range(3, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
        else:
            i += 2
    return True

def checkGoldbach(n):
    for i in xrange(1, int(sqrt(n / 2.0)) + 1):
        if isPrime(n - 2 * i ** 2):
            return True
    return False
    
def goldbach():
    goldbach = []
    for x in xrange(1, 250):
        print x
        for y in xrange(1, 250):
            if not checkGoldbach((2*x + 1)*(2*y + 1)):
                goldbach.append((2*x + 1)*(2*y + 1))
    return min(goldbach)

print goldbach()
