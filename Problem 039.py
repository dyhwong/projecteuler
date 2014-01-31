def createPythag(maxPerimeter):
    return [[x + y, x + z, x + y + z] for x in xrange(2, maxPerimeter / 3 + 1, 2) for y in xrange(1, maxPerimeter / 2 + 1) for z in xrange(1, maxPerimeter / 2 + 1)
             if y < z and 3 * x + 2 * y + 2 * z <= 1000 and x ** 2 == 2 * y * z]

def getPerimeter(list1):
    for i in range(len(list1)):
        list1[i] = sum(list1[i])
    return list1

def findMaxCount(list1):
    perimeter = None
    maxCount = 0
    for i in range(1001):
        if list1.count(i) > maxCount:
            maxCount = list1.count(i)
            perimeter = i
    return perimeter

def main():
    print findMaxCount(getPerimeter(createPythag(1000)))

main()
             
