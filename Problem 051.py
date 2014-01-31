from math import sqrt

def isPrime(n):
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def genReplace(string):
    replacements = []
    for i in xrange(1, 10):
        replace = ""
        for number in string:
            if number == '_':
                replace += str(i)
            else:
                replace += number
        replacements.append(int(replace))
    return replacements

def eightPrimeFamily(list1):
    count = 0
    for item in list1:
        if isPrime(item):
            count += 1
    if count >= 8:
        return True
    return False

def sixDigit():
    newList = []
    for i in xrange(101, 1000, 2):
        n = str(i)
        list1 = [n[0] + "___" + n[1],
                 n[0] + "__" + n[1] + "_",
                 n[0] + "_" + n[1] + "__",
                 n[0] + n[1] + "___",
                 "___" + n[0] + n[1],
                 "__" + n[0] + "_"  + n[1],
                 "__" + n[0] + n[1] + "_",
                 "_" + n[0] + n[1] + "__",
                 "_" + n[0] + "__" + n[1],
                 "_" + n[0] + "_" + n[1] + "_"
                 ]
                 
        for item in list1:
            if eightPrimeFamily(genReplace(item + n[-1])):
                newList.append(item + n[-1])
    return newList
            
def getAns():
    newList = []
    for item in sixDigit():
        for number in genReplace(item):
            if isPrime(number) and len(str(number)) == 6:
                newList.append(number)
                break
    print min(newList)

getAns()
