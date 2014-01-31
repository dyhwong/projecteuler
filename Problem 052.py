def genMultiples(n):
    newList = []
    for i in xrange(1, 7):
        newList.append(n * i)
    return newList

def isSame(list1):
    list2 = []
    for item in list1:
        newList = []
        for number in str(item):
            newList.append(number)
        newList.sort()
        list2.append("".join(newList))
    if list2.count(list2[0]) == len(list2):
        return True
    return False


def permuted(digits):
    for i in xrange(10 ** (digits - 1), (10 ** digits) / 6 + 1):
        if isSame(genMultiples(i)):
            return i
    return 0

def getAns():
    for i in xrange(1, 8):
        if permuted(i):
            return permuted(i)

print getAns()
