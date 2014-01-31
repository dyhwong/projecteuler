def factorial(n):
    product = 1
    for i in range(n):
        product *= (i + 1)
    return product

def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

rows = 20
cols = 20
n = rows + cols
k = rows

print choose(n, k)
