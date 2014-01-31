def buildList(n):
    newList = [ 1 for b in xrange(0, n + 1, 2)
            for c in xrange(0, n + 1, 5) for d in xrange(0, n + 1, 10)
            for e in xrange(0, n + 1, 20) for f in xrange(0, n + 1, 50)
            for g in xrange(0, n + 1, 100) for h in xrange(0, n + 1, 200) if b + c + d + e + f + g + h <= n]
    return newList

def getLength(newList):
    return len(newList)

def main():
    print getLength(buildList(200))

main()
