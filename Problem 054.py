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
        elif card[:-1] == "T":
            numbers.append(string[10])            
        else:
            numbers.append(string[int(card[:-1])])
    numbers.sort()
    numbers = "".join(numbers)
    if numbers in string:
        return numbers[-1]
    return False

def isStraightFlush(hand):
    if isStraight(hand) and isFlush(hand):
        return isStraight(hand)
    return False

def compare(hand1, hand2):
    while max(hand1) == max(hand2):
        hand1.remove(max(hand1))
        hand2.remove(max(hand2))
    if max(hand1) > max(hand2):
        return True
    return False            

def getMultiples(hand):
    letters = []
    count = []
    string = "abcdefghijklmnopq"

    def checkLetter(letter):
        if letter in letters:
            count[letters.index(letter)] += 1
        else:
            letters.append(letter)
            count.append(1)
            
    for card in hand:
        if card[0] == "T":
            checkLetter(string[10])
        elif card[0] == "J":
            checkLetter(string[11])
        elif card[0] == "Q":
            checkLetter(string[12])
        elif card[0] == "K":
            checkLetter(string[13])
        elif card[0] == "A":
            checkLetter(string[14])
        else:
            checkLetter(string[int(card[0])])
    return [letters, count]

def isFourKind(count):
    if 4 in count:
        return True
    return False

def isFullHouse(count):
    if 3 in count and 2 in count:
        return True
    return False

def isThreeKind(count):
    if 3 in count:
        return True
    return False

def isTwoPair(count):
    if count.count(2) == 2:
        return True
    return False

def isPair(count):
    if 2 in count:
        return True
    return False

def determineRank(hand):
    if isStraightFlush(hand):
        return [8, isStraightFlush(hand)]
    elif isFourKind(getMultiples(hand)[1]):
        return [7, getMultiples(hand)]
    elif isFullHouse(getMultiples(hand)[1]):
        return [6, getMultiples(hand)]
    elif isFlush(hand):
        return [5, getMultiples(hand)[0]]
    elif isStraight(hand):
        return [4, isStraight(hand)]
    elif isThreeKind(getMultiples(hand)[1]):
        return [3, getMultiples(hand)]
    elif isTwoPair(getMultiples(hand)[1]):
        return [2, getMultiples(hand)]
    elif isPair(getMultiples(hand)[1]):
        return [1, getMultiples(hand)]
    else:
        return [0, getMultiples(hand)[0]]

def determineWinner(hand1, hand2):
    rank1 = determineRank(hand1)
    rank2 = determineRank(hand2)
    if rank1[0] > rank2[0]:
        return True
    elif rank1[0] < rank2[0]:
        return False
    else:
        if rank1[0] == 8:
            return compare(rank1[1], rank2[1])
        elif rank1[0] == 7:
            if rank1[1][0][rank1[1][1].index(4)] > rank2[1][0][rank2[1][1].index(4)]:
                return True
            elif rank1[1][0][rank1[1][1].index(4)] < rank2[1][0][rank2[1][1].index(4)]:
                return False
            else:
                if rank1[1][0][rank1[1][1].index(1)] > rank2[1][0][rank2[1][1].index(1)]:
                    return True
                else:
                    return False
        elif rank1[0] == 6:
            if rank1[1][0][rank1[1][1].index(3)] > rank2[1][0][rank2[1][1].index(3)]:
                return True
            elif rank1[1][0][rank1[1][1].index(3)] < rank2[1][0][rank2[1][1].index(3)]:
                return False
            else:
                if rank1[1][0][rank1[1][1].index(2)] > rank2[1][0][rank2[1][1].index(2)]:
                    return True
                else:
                    return False
        elif rank1[0] == 5:
            return compare(rank1[1], rank2[1])
        elif rank1[0] == 4:
            return compare(rank1[1], rank2[1])
        elif rank1[0] == 3:
            if rank1[1][0][rank1[1][1].index(3)] > rank2[1][0][rank2[1][1].index(3)]:
                return True
            elif rank1[1][0][rank1[1][1].index(3)] < rank2[0][rank2[1][1].index(3)]:
                return False
            else:
                rank1[1][0].pop(rank1[1][1].index(3))
                rank2[1][0].pop(rank2[1][1].index(3))
                return compare(rank1[1][0], rank2[1][0])
        elif rank1[0] == 2:
            pairs1 = []
            pairs2 = []
            for i in xrange(len(rank1[1][1])):
                if rank1[1][1][i] == 2:
                    pairs1.append(rank1[1][0][i])
                if rank2[1][1][i] == 2:
                    pairs2.append(rank2[1][0][i])
            if max(pairs1) > max(pairs2):
                return True
            elif max(pairs1) < max(pairs2):
                return False
            else:
                if min(pairs1) > min(pairs2):
                    return True
                elif min(pairs1) < min(pairs2):
                    return False
                else:
                    if rank1[1][0][rank1[1][1].index(1)] > rank2[1][0][rank2[1][1].index(1)]:
                       return True
                    else:
                        return False
        elif rank1[0] == 1:
            if rank1[1][0][rank1[1][1].index(2)] > rank2[1][0][rank2[1][1].index(2)]:
                return True
            elif rank1[1][0][rank1[1][1].index(2)] < rank2[1][0][rank2[1][1].index(2)]:
                return False
            else:
                rank1[1][0].pop(rank1[1][1].index(2))
                rank2[1][0].pop(rank2[1][1].index(2))
                return compare(rank1[1][0], rank2[1][0])
                
        else:
            return compare(rank1[1], rank2[1])

def main():
    player1 = 0
    for hand in loadHands():
        if hand == ['']:
            pass
        elif determineWinner(hand[0:5], hand[5:10]):
            player1 += 1
    print player1

main()
