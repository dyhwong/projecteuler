def isPandigital(a, b, c):
    digits = "".join([str(a), str(b), str(c)])
    listedDigits = []
    for i in digits:
        listedDigits.append(i)
    listedDigits.sort()
    listedDigits = "".join(listedDigits)
    if listedDigits == "123456789":
        return True
    else:
        return False
    
def onefourDigits():
    pandigital = []
    test = [[x, y] for x in range(2, 10) for y in range(1234, 9877)]
    for i in range(0, len(test)):
        if isPandigital(test[i][0], test[i][1], test[i][0]*test[i][1]):
            pandigital.append(test[i][0]*test[i][1])
    return pandigital

def twothreeDigits():
    pandigital = []
    test = [[x, y] for x in range(12, 99) for y in range(123, 988)]
    for i in range(0, len(test)):
        if isPandigital(test[i][0], test[i][1], test[i][0]*test[i][1]):
            pandigital.append(test[i][0]*test[i][1])
    return pandigital

def concatenate(list1, list2):
    combined = []
    list1.extend(list2)
    for i in range(0, len(list1)):
        if list1[i] not in combined:
            combined.append(list1[i])
    return combined

def getSum(pandigitalList):
    return sum(pandigitalList)

def main():
    print getSum(concatenate(onefourDigits(), twothreeDigits()))

main()

