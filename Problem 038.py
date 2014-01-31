def isPandigital(n):
    listedDigits = []
    for i in str(n):
        listedDigits.append(i)
    listedDigits.sort()
    listedDigits = "".join(listedDigits)
    if listedDigits == "123456789":
        return True
    else:
        return False

def onetwotwotwotwo():
    pandigitalMultiples = []
    for i in range(5, 10):
        string = str(i) + str(2 * i) + str(3 * i) + str(4 * i) + str(5 * i)
        if isPandigital(int(string)):
            pandigitalMultiples.append(int(string))
    return pandigitalMultiples

def twotwotwothree():
    pandigitalMultiples = []
    for i in range(25, 100):
        string = str(i) + str(2 * i) + str(3 * i) + str(4 * i)
        if isPandigital(int(string)):
            pandigitalMultiples.append(int(string))
    return pandigitalMultiples

def threethreethree():
    pandigitalMultiples = []
    for i in range(100, 334):
        string = str(i) + str(2 * i) + str(3 * i)
        if isPandigital(int(string)):
            pandigitalMultiples.append(int(string))
    return pandigitalMultiples

def fourfive():
    pandigitalMultiples = []
    for i in range(5000, 10000):
        string = str(i) + str(2 * i)
        if isPandigital(int(string)):
            pandigitalMultiples.append(int(string))
    return pandigitalMultiples

def findMax():
    list1 = onetwotwotwotwo()
    list2 = twotwotwothree()
    list3 = threethreethree()
    list4 = fourfive()
    list1.extend(list2)
    list1.extend(list3)
    list1.extend(list4)
    return max(list1)

print findMax()
