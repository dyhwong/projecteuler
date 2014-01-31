x = 1
y = 1
count = 2
power = 999
while x <= 10**power and y <= 10**power:
    x += y
    count += 1
    if x <= 10**power and y <= 10**power:
        y += x
        count += 1
    else:
        break
print count
    
