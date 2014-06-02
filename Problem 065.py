class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    
    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)

    def add(self, n):
        return Fraction(n * self.denominator + self.numerator, self.denominator)

def getSum(n):
    return sum([int(str(n)[i]) for i in xrange(len(str(n)))])

def getCoefficient(n):
    if n == 1:
        return 2
    if n % 3 == 0:
        return 2 * n / 3
    return 1

def getConvergent(n):
    counter = n
    ans = Fraction(getCoefficient(n), 1)
    while counter > 1:
        counter -= 1
        ans = ans.reciprocal().add(getCoefficient(counter))
    return ans

def main():
    print getSum(getConvergent(100).numerator)

main()

