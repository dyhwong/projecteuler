def loadHands():
    inFile = open('poker.txt', 'r+')
    handList = inFile.read().split('\n')
    for i in xrange(len(handList)):
        handList[i] = handList[i].split(' ')
    return handList

def isFlush(hand):
    suits = []
    for card in hand:
        suits.append(card[-1])
    if suits.count(suits[0]) == len(suits):
        return True
    return False

def isStraight(hand):
    numbers = []
    string = "abcdefghijklmnopq"
    for card in hand:
        if card[:-1] == "J":
            numbers.append(string[11])
        elif card[:-1] == "Q":
            numbers.append(string[12])
        elif card[:-1] == "K":
            numbers.append(string[13])
        elif card[:-1] == "A":
            numbers.append(string[14])
        else:
            numbers.append(string[int(card[:-1])])
    numbers.sort()
    numbers = "".join(numbers)
    if numbers in string:
        return True
    return False

def isStraightFlush(hand):
    if isStraight(hand) and isFlush(hand):
        return True
    return False

def 
