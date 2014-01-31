fifth_power = []
for i in range(11, 101):
    if int(str(i)[0])**5 + int(str(i)[1])**5 == i:
        fifth_power.append(i)
for i in range(101, 1001):
    if int(str(i)[0])**5 + int(str(i)[1])**5 + int(str(i)[2])**5 == i:
        fifth_power.append(i)
for i in range(1001, 10001):
    if int(str(i)[0])**5 + int(str(i)[1])**5 + int(str(i)[2])**5 + int(str(i)[3])**5 == i:
        fifth_power.append(i)
for i in range(10001, 100001):
    if int(str(i)[0])**5 + int(str(i)[1])**5 + int(str(i)[2])**5 + int(str(i)[3])**5 + int(str(i)[4])**5 == i:
        fifth_power.append(i)
for i in range(100001, 300000):
    if int(str(i)[0])**5 + int(str(i)[1])**5 + int(str(i)[2])**5 + int(str(i)[3])**5 + int(str(i)[4])**5 + int(str(i)[5])**5 == i:
        fifth_power.append(i)

print sum(fifth_power)

        
