def findMaxCycle(n):
    reciprocalList = [i for i in range(1, n) if i % 2 != 0 and i % 5 != 0]
    exponent = 1
    while len(reciprocalList) != 1:
        for i in reciprocalList:
            if (10 ** exponent - 1) % i == 0:
                reciprocalList.remove(i)
        exponent += 1
    return reciprocalList[0]

def main():
    print findMaxCycle(1001)
    
main()
