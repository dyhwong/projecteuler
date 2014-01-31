def buildTri(n):
    return n * (n + 1) / 2

def buildPent(n):
    return n * (3 * n - 1) / 2

def buildHex(n):
    return n * (2 * n - 1)

triangular = []
pentagonal = []
hexagonal = []

def findOverlap():
    overlap = []
    count = 1
    while len(overlap) != 3:
        triangular.append(buildTri(count))
        pentagonal.append(buildPent(count))
        hexagonal.append(buildHex(count))
        if triangular[-1] in pentagonal:
            if triangular[-1] in hexagonal:
                overlap.append(count)
        count += 1
    return overlap

print findOverlap()[2]
