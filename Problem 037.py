import math

def isPrime(n):
    if n == 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        else:
            i += 2
    return True

def isTruncatablePrime(n):
    for i in range(0, len(str(n))):
        if not isPrime(int(str(n)[i:])):
            return False
    for i in range(1, len(str(n))):
        if not isPrime(int(str(n)[:i])):
            return False
    return True

def findTrunc():
    truncatablePrimes = []
    test = 11
    while len(truncatablePrimes) != 11:
        if str(test)[0] not in "14689" and str(test)[1] not in "245680" and str(test)[-1] not in "159" and str(test)[-2] not in "4680":
            if isTruncatablePrime(test):
                truncatablePrimes.append(test)
        test += 2
    return truncatablePrimes

def getSum(list1):
   return sum(list1)

def main():
    print getSum(findTrunc())

main()
