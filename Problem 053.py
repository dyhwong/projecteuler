def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def permutation(n, r):
    if n == r:
        return 1
    else:
        return n * permutation(n - 1, r)

def comb(n, r):
    return permutation(n, r) / factorial(n - r)

combinatorials = []
for n in xrange(1, 101):
    for r in xrange(1, n + 1):
        if comb(n, r) > 1000000:
            combinatorials.append(comb(n, r))
print len(combinatorials)
        


