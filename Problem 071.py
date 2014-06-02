def getClosest(d):
    return 3 * d / 7

def gcd(a, b):
    while a:
        a, b = b%a, a
    return b

def main():
    maximum = [0, 0, 0]
    for i in xrange(1000001):
        if gcd(getClosest(i), i) == 1:
            if i != 7:
                if getClosest(i) / float(i) > maximum[2]:
                    maximum = [getClosest(i), i, getClosest(i) / float(i)]
    print maximum

main()
