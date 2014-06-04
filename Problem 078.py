def pentagonalize(n):
    return n * (3 * n - 1) / 2

def sign(n):
    if abs(n) % 2 == 1:
        return 1
    return -1

partition = {0: 1, 1: 1}

def p(n):
    total = 0
    counter = 1
    if n < 0:
        return 0
    while n - pentagonalize(counter) >= 0:
        total += partition[n - pentagonalize(counter)] * sign(counter)
        if n - pentagonalize(-counter) < 0:
            break
        total += partition[n - pentagonalize(-counter)] * sign(-counter)
        
        counter += 1
    partition[n] = total % 1000000
    return partition[n]

def main():
    counter = 2
    while p(counter) % 1000000 != 0:
        counter += 1
    print counter

main()
    
