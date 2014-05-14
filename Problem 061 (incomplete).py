triangular = [n * (n + 1) /2 for n in xrange(45, 141)]
square = [n * n for n in xrange(32, 100)]
pentagonal = [n * (3 * n - 1) / 2 for n in xrange(26, 82)]
hexagonal = [n * (2 * n - 1) for n in xrange(23, 71)]
heptagonal = [n * (5 * n - 3) / 2 for n in xrange(21, 64)]
octagonal = [n * (3 * n - 2) for n in xrange(19, 59)]

def remove():
    for num in triangular[:]:
        if str(num)[2] == "0":
            triangular.remove(num)
    for num in square[:]:
        if str(num)[2] == "0":
            square.remove(num)
    for num in pentagonal[:]:
        if str(num)[2] == "0":
            pentagonal.remove(num)
    for num in hexagonal[:]:
        if str(num)[2] == "0":
            hexagonal.remove(num)
    for num in heptagonal[:]:
        if str(num)[2] == "0":
            heptagonal.remove(num)
    for num in octagonal[:]:
        if str(num)[2] == "0":
            octagonal.remove(num)

def isCyclic(a, b):
    if str(a)[2:] == str(b)[:2]:
        return True
    return False

remove()
figurate = [triangular, square, pentagonal, hexagonal, heptagonal, octagonal]
print figurate

print len(triangular) * len(square) * len(pentagonal) * len(hexagonal) * len(heptagonal) * len(octagonal)

print octagonal
