integers = [1]
product = 1
x = 2
while x <= 20:
    n = x
    for i in integers:
        if n % i == 0:
            n /= i
    integers.append(n)
    x += 1

for i in integers:
    product *= i
print product
