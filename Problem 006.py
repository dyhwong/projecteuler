count = 0
for i in range(1, 101):
    count += (i ** 2) * (i - 1)
print count

n = 100
def difference(x):
    total = (x*(x+1)/2)**2 - (x*(x+1)*(2*x+1)/6)
    return total
print difference(100)
