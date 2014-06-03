class Polynomial:
    ## Intialize a polynomial with a list of coefficients.
    ## The coefficient list starts with the highest order term.
    def __init__(self, coeffs):
        self.coeffs = coeffs
        self.order = len(coeffs) - 1

    ## Return the coefficient of the x**i term
    def coeff(self,i):
        return self.coeffs[-i - 1]

    ## Return the value of this Polynomial evaluated at x=v
    def val(self, v):
        return sum([self.coeff(i) * (v ** i) for i in xrange(len(self.coeffs))])

    ## Return the roots of this Polynomial
    def roots(self):
        if self.order == 1:
            return [-1.0 * self.coeff(0) / self.coeff(1)]
        elif self.order == 2:
            a = self.coeff(2)
            b = self.coeff(1)
            c = self.coeff(0)
            if b ** 2 - 4 * a * c > 0:
                return [-b / (2.0*a) + (b**2 - 4*a*c)**0.5/(2.0*a), -b / (2.0*a) - (b**2 - 4*a*c)**0.5/(2.0*a)]
            elif b ** 2 - 4 * a * c < 0:
                return [complex(-b / (2.0*a), (4*a*c - b**2)**0.5/(2.0*a)), complex(-b / (2.0*a), -(4*a*c - b**2)**0.5/(2.0*a))]
            else:
                return [-b / (2.0*a)]
        else:
            return "Error: roots not handled"

    ## Add two polynomials, return a new Polynomial
    def add (self, other):
        def safeAdd(obj1, obj2):
            sumList = []
            for i in xrange(len(obj1.coeffs)):
                sumList = [obj1.coeff(i) + obj2.coeff(i)] + sumList
            for j in xrange(len(obj1.coeffs), len(obj2.coeffs)):
                sumList = [obj2.coeff(j)] + sumList
            return sumList
        if len(self.coeffs) < len(other.coeffs):
            newCoeffs = safeAdd(self, other)
        else:
            newCoeffs = safeAdd(other, self)
        return Polynomial(newCoeffs)

    ## Multiply two polynomials, return a new Polynomial
    def mul(self, other):
        polyList = []
        for i in xrange(other.order + 1):
            newCoeffs = []
            for j in xrange(self.order + 1):
                newCoeffs.append(other.coeff(i) * self.coeff(len(self.coeffs) - j - 1))
            newCoeffs.extend([0]*i)
            polyList.append(Polynomial(newCoeffs))
        newPoly = Polynomial([0])
        for polynomial in polyList:
            newPoly += polynomial
        return newPoly

    def concatenate(self, value):
        self.coeffs = self.coeffs[self.order - value:]
        self.order = len(self.coeffs) - 1

    def __add__(self, other):
        #override the + operator so we can do things like p1+p2
        return self.add(other)

    def __mul__(self, other):
        #override the * operator so we can do things like p1*p2
        return self.mul(other)

    def __str__(self):
        coeffs = [self.coeff(i) for i in xrange(self.order,-1,-1)]
        return 'Polynomial(%r)' % coeffs

def buildPolynomial(n, k):
    coeffs = [0 for i in xrange(k + 1)]
    for i in xrange(k / n + 1):
        coeffs[-i * n - 1] = 1
    return Polynomial(coeffs)
        
def main():
    k = 100
    poly = buildPolynomial(1, k)
    for i in xrange(2,k):
        poly *= buildPolynomial(i, k)
        poly.concatenate(k)
    print poly.coeff(k)

main()
