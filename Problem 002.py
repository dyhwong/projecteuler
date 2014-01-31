x = 1
y = 2
count = 0
while x <= 4000000 and y <= 4000000:
    if x % 2 == 0:
        count += x
    x += y
    if y % 2 == 0:
        count += y
    y += x
print count
    
