from math import sqrt

def isPerfectSquare(x):
    return int(sqrt(x)) ** 2 == x

def getMinSolution(D):
    counter = 1
    while True:
        if counter > 1000000:
            return 0
        if isPerfectSquare(1 + D * counter ** 2):
            return sqrt(1 + D * counter ** 2)
        counter += 1

def main():
    array = []
    for i in xrange(1001):
        if not isPerfectSquare(i):
            array.append(getMinSolution(i))
        else:
            array.append(-1)
        if array[-1] == 0:
            print i
    print array.index(max(array))

main()
    
