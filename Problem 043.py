def isPandigital(n):
    listedDigits = []
    for i in str(n):
        listedDigits.append(i)
    listedDigits.sort()
    listedDigits = "".join(listedDigits)
    if listedDigits == "0123456789":
        return True
    else:
        return False

def main():
    divisors = [17, 13, 11, 7, 5, 3, 2]
    pandigital = [ a + b + c for a in "0123456789" for b in "0123456789" for c in "0123456789"]
    for n in divisors:
        copy = pandigital[:]
        for m in copy:
            if int(m[0:3]) % n == 0:
                for digit in "0123456789":
                    a = digit + m
                    pandigital.append(a)
            pandigital.remove(m)
    total = 0
    for i in pandigital:
        if isPandigital(int(i)) and i[0] != 0:
            total += int(i)
    return total

print main()
                
