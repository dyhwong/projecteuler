def factorSum(n):
    total = 0
    for i in xrange(1, n / 2 + 1):
        if n % i == 0:
            total += i
    return total

def isAbundant(n):
    if factorSum(n) > n:
        return True
    else:
        return False

def buildAbundant():
    abundant = []
    for i in xrange(12, 28112):
        if isAbundant(i):
            abundant.append(i)
            print i
    return abundant

def getNonabundant(list):
    nonabundantSum = [True] * 28123
    for x in list:
        for y in list:
            if x + y < len(nonabundantSum):
                nonabundantSum[x + y] = False
    return nonabundantSum

def nonabundantSum(list):
    total = 0
    for i in xrange(0, len(list)):
        if list[i]:
            total += i
    return total

def main():
    print nonabundantSum(getNonabundant(buildAbundant()))

main()

