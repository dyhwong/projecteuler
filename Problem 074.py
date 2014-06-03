FACTORIALS = {0 : 1}
loop = {1: 1, 2: 1, 145: 1, 169: 3, 871: 2, 872: 2, 1454: 3, 45361: 2, 45362: 2, 363601: 3}
chain = {}

def factorial(n):
    if n in FACTORIALS:
        return FACTORIALS[n]
    else:
        ans = n * factorial(n - 1)
        FACTORIALS[n] = ans
        return ans

def digitFactorial(n):
    def getDigits(n):
        array = []
        while n != 0:
            array.append(n % 10)
            n /= 10
        return array

    return sum([factorial(i) for i in getDigits(n)])

def buildChain(n):
    digFac = digitFactorial(n)
    if n in loop:
        chain[n] = loop[n]
    elif digFac in chain:
        chain[n] = chain[digFac] + 1
    elif digFac == n:
        loop[n] = 1
        chain[n] = 1
    else:
        buildChain(digFac)
        chain[n] = chain[digFac] + 1

def main():
    counter = 0
    for i in xrange(1, 1000001):
        buildChain(i)
        if chain[i] == 60:
            counter += 1
    print counter
        
main()
