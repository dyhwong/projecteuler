def getDigitalSum(n):
    total = 0
    for number in str(n):
        total += int(number)
    return total

def getPower(a, b):
    if b == 0:
        return 1
    return a * getPower(a, b - 1)

def main():
    digital = []
    for x in xrange(2, 100):
        for y in xrange(2, 100):
            digital.append(getDigitalSum(getPower(x, y)))
    print max(digital)

main()
        
