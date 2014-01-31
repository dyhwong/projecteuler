from math import sqrt

def isPrime(n):
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def factor(n):
    factors = []
    if n % 2 == 0:
        factors.append(2)
        n /= 2
    counter = 3
    while counter <= n:
        if n % counter == 0:
            if isPrime(counter):
                n /= counter
                if counter not in factors:
                    factors.append(counter)
                    if len(factors) >= 5:
                        return []
        else:
            counter += 2
    return factors

def hasFour(list1):
    if len(list1) == 4:
        return True
    return False

def main():
    notFound = True
    check = 2 * 3 * 5 * 13
    while notFound:
        check += 1
        if hasFour(factor(check)):
            if hasFour(factor(check + 1)):
                if hasFour(factor(check + 2)):
                    if hasFour(factor(check + 3)):
                        notFound = False
    return check
    
