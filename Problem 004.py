n = 999999
count = 0
while n > 0:
    for i in range(100, 1000):
        if n % i == 0 and len(str(n/i)) == 3:
            print n
            break
    else:
        count += 1
        if count % 100 == 0:
            n -= 11
        elif count % 10 == 0:
            n -= 110
        else:
            n -= 1100
            

