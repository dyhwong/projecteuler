def gcd(a, b):
    while a:
        a, b = b%a, a
    return b

def getLength(m, n):
    return 2 * m * (m + n)

def main():
    lengths = {}
    for m in xrange(750000):
        n = 1
        while n < m:
            if getLength(m, n) > 1500000:
                break
            if gcd(m, n) == 1:
                try:
                    lengths[getLength(m, n)] += 1
                except:
                    lengths[getLength(m, n)] = 1
                for i in xrange(1500000 / getLength(m, n) + 1):
                    try:
                        lengths[i * getLength(m, n)] += 1
                    except:
                        lengths[i * getLength(m, n)] = 1
            n += 1

    counter = 0
    for L in lengths.keys():
        if lengths[L] == 1:
            counter += 1
    print counter
        
    
