def collatz(number):
    collatz_sequence = [number]
    while number != 1:
        if number % 2 == 0:
            number /= 2
            collatz_sequence.append(number)
        else:
            number = 3*number + 1
            collatz_sequence.append(number)
    return collatz_sequence

maximum = 0
for i in range(1, 1000001):
    if len(collatz(i)) > maximum:
        maximum = len(collatz(i))
        print i
    
