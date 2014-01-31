import math

def isPrime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        else:
            i += 2
    return True

def isPandigital(n):
    listedDigits = []
    for i in str(n):
        listedDigits.append(i)
    listedDigits.sort()
    listedDigits = "".join(listedDigits)
    if listedDigits == "1234567":
        return True
    else:
        return False

def buildPandigital7():
    return [ int(str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g)) for a in xrange(7, 0, -1) for b in xrange(7, 0, -1) for c in xrange(7, 0, -1)
             for d in xrange(7, 0, -1) for e in xrange(7, 0, -1) for f in xrange(7, 0, -1) for g in xrange(7, 0, -1) if isPandigital(int(str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g)))]

def filterPrimes(list1):
    for i in list1[:]:
        if not isPrime(i):
            list1.remove(i)
    return list1

def main():
    print max(filterPrimes(buildPandigital7()))

main()
