from math import sqrt

def pent(n):
    return n * (3 * n - 1) / 2

def isPentagonal(n):
    if (sqrt(1 + 24 * n) + 1) % 6 == 0:
        return True
    return False

def minDif():
    notFound = True
    count = 1
    while notFound:
        count += 1
        for m in range(count - 1, 0, -1):
            if isPentagonal(pent(count) - pent(m)) and isPentagonal(pent(count) + pent(m)):
                notFound = False
                result = pent(count) - pent(m)
                break
    return result
                
print minDif()
                
