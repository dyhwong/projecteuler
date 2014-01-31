import math

def isPrime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        else:
            i += 2
    return True     

def buildCircular(n):
    string = str(n)
    circular = []
    temp = None
    for i in range(0, len(string)):
        temp = string[i:] + string[:i]
        circular.append(int(temp))
    return circular
 
def buildPrimes():
    list1 = [ int(str(a) + str(b)) for a in [1, 3, 7, 9] for b in [1, 3, 7, 9]]
    list2 = [ int(str(a) + str(b)) for a in list1 for b in [1, 3, 7, 9]]
    list3 = [ int(str(a) + str(b)) for a in list2 for b in [1, 3, 7, 9]]
    list4 = [ int(str(a) + str(b)) for a in list3 for b in [1, 3, 7, 9]]
    list5 = [ int(str(a) + str(b)) for a in list4 for b in [1, 3, 7, 9]]
    list1.extend(list2)
    list1.extend(list3)
    list1.extend(list4)
    list1.extend(list5)
    return list1

def buildPrimeList(list1):
    copyList = list1[:]
    for i in copyList:
        if not isPrime(i):
            list1.remove(i)
    return list1

def checkList(list1, list2):
    for i in list1:
        if i not in list2:
            return False
    return True

def checkCircular(list1):
    circular = []
    for i in list1:
        if checkList(buildCircular(i), list1):
            circular.append(i)
    return circular

def getLength(list1):
    return len(list1)

def main():
    print getLength(checkCircular(buildPrimeList(buildPrimes()))) + 4

main()
