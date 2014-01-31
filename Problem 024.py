def factorial(n):
    product = 1
    for i in range(n):
        product *= (i + 1)
    return product

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
total = 999999

first = digits[total // factorial(9)]
digits.remove(first)
total -= (total // factorial(9) * factorial(9))
second = digits[total // factorial(8)]
digits.remove(second)
total -= (total // factorial(8) * factorial(8))
third = digits[total // factorial(7)]
digits.remove(third)
total -= (total // factorial(7) * factorial(7))
fourth = digits[total // factorial(6)]
digits.remove(fourth)
total -= (total // factorial(6) * factorial(6))
fifth = digits[total // factorial(5)]
digits.remove(fifth)
total -= (total // factorial(5) * factorial(5))
sixth = digits[total // factorial(4)]
digits.remove(sixth)
total -= (total // factorial(4) * factorial(4))
seventh = digits[total // factorial(3)]
digits.remove(seventh)
total -= (total // factorial(3) * factorial(3))
eighth = digits[total // factorial(2)]
digits.remove(eighth)
total -= (total // factorial(2) * factorial(2))
ninth = digits[total // factorial(1)]
digits.remove(ninth)
total -= (total // factorial(1) * factorial(1))
tenth = digits[total // factorial(0)]
digits.remove(tenth)
total -= (total // factorial(0) * factorial(0))

print str(first) + str(second) + str(third) + str(fourth) + str(fifth) + str(sixth) + str(seventh) + str(eighth) + str(ninth) + str(tenth)
