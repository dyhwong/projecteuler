from math import ceil

def getMinPower(n):
    return ceil(10**(float((n - 1))/n))

def main():
    total = 0
    counter = 1
    difference = 10
    while difference > 0:
        difference = 10 - getMinPower(counter)
        total += difference
        counter += 1
    print int(total)

main()
