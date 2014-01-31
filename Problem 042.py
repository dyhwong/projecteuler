def loadWords():
    inFile = open('words42.txt', 'r+')
    wordList = "".join(inFile.read().split('"')).split(',')
    return wordList

def buildDict():
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for letter in string:
        dictionary[letter] = string.index(letter) + 1

def getValue(word):
    value = 0
    for letter in word:
        value += dictionary[letter]
    return value

def isTriangle(value):
    triangular = [ x * (x + 1) / 2 for x in xrange(1, 52)]
    if value in triangular:
        return True
    else:
        return False

dictionary = {}
buildDict()
wordList = loadWords()
for word in wordList[:]:
    if not isTriangle(getValue(word)):
        wordList.remove(word)
print len(wordList)
