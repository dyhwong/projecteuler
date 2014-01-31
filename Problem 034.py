def factorial(n):
    if int(n) == 0:
        return 1
    elif int(n) < 0:
        print "That's not a valid input!"
        return 0
    else:
        return factorial(n - 1) * int(n)

def factorialSum(n):
    digits = []
    for i in str(n):
        digits.append(i)

    total = 0
    for j in digits:
        total += factorial(int(j))
    return total

def findDigitFactorials():
    digitFactorials = []
    for i in range(21, 999999):
        if factorialSum(i) == i:
            digitFactorials.append(i)
    return digitFactorials

def getSum(list1):
    return sum(list1)

def main():
    print getSum(findDigitFactorials())

main()

