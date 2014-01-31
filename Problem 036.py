def isPalindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] == string[-1]:
        return True and isPalindrome(string[1:-1])
    else:
        return False

def getBinary(n):
    return bin(n)[2:]

def checkPalindrome(n):
    palindromes = []
    for i in xrange(1, n + 1):
        if isPalindrome(getBinary(i)) and isPalindrome(str(i)):
            palindromes.append(i)
    return palindromes

def getSum(list1):
    return sum(list1)

def main():
    print getSum(checkPalindrome(1000000))

main()
