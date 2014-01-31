def factorial(n):
    product = 1
    for i in range(n):
        product *= (i + 1)
    return product

number = factorial(100)/(10 ** 24)
sum = 0
for i in range(0, len(str(number))):
    sum += int(str(number)[i])
print sum
