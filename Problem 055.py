def isPalindrome(n):
    n = str(n)
    if len(n) == 0 or len(n) == 1:
        return True
    else:
        return n[0] == n[-1] and isPalindrome(n[1:-1])

def reverseSum(n):
    def genRev(n):
        n = str(n)
        rev = ''
        for i in xrange(1, len(n) + 1):
            rev += n[-i]
        return int(rev)
    return n + genRev(n)

def isLychrel(n):
    iter = 1
    while iter <= 50:
        n = reverseSum(n)
        if isPalindrome(n):
            return False
        iter += 1
    return True

def main():
    count = 0
    for i in xrange(1, 10000):
        if isLychrel(i):
            count += 1
    print count

main()
