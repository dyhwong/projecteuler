def getNextIter(x, y):
    return [y, 2*y + x]

def checkNum(x, y):
    if len(str(x + y)) > len(str(y)):
        return True
    return False

def main():
    x = 0
    y = 1
    counter = 0
    count = 0
    while counter < 1000:
        [x, y] = [getNextIter(x, y)[0], getNextIter(x, y)[1]]
        if checkNum(x, y):
            count += 1
        counter += 1
    print count


main()
