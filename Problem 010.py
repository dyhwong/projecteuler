def eratosthenes(n):
    sieve = [True] * n
    for x in xrange(2, int(n ** 0.5) + 1):
        for i in xrange(2*x, n, x):
            sieve[i] = False
    return sieve

def getSum(list):
    total = 0
    for i in xrange(2, len(list)):
        if list[i]:
            total += i
    return total

def main():
    print getSum(eratosthenes(2000000))

print eratosthenes(1000000)
main()
            
    


