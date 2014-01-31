import math
def numberOfTerms(base, n):
    total = []
    for i in range(1, int(math.log(n, base)) + 1):
        for j in range(1, 100 * i + 1):
            for k in range(i, int(math.log(n, base)) + 1):
                if j % k == 0 and j not in total:
                    total.append(j)
    return len(total)

def removePowers(n):
    newList = [i for i in range(1, n + 1)]
    for i in range(2, int(math.floor(math.sqrt(n))) + 1):
        m = 2
        while i ** m <= n:
            if i ** m in newList:
                newList.remove(i ** m)
            m += 1
    return newList

def findSequenceLength(n):
    total = 0
    for i in removePowers(n)[1:]:
        total += numberOfTerms(i, n)
    return total - len(removePowers(n)[1:])

def main():
    print findSequenceLength(100)

main()

