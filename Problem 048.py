def samePower(n):
    product = 1
    for i in xrange(1, n + 1):
        if len(str(product * n)) > 10:
            product = int(str(product * n)[-10:])
        else:
            product *= n
    return product

def getTotal(n):
    total = 0
    for i in xrange(1, n + 1):
        if len(str(total + samePower(i))) > 10:
            total = int(str(total + samePower(i))[-10:])
        else:
            total += samePower(i)
    return total

def main():
    print getTotal(1000)

main()
