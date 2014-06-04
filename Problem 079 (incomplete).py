def loadWords():
    inFile = open('keylog.txt', 'r+')
    wordList = "".join(inFile.read().split('"')).split('\n')
    wordList = [n for n in wordList if n]
    return sorted(wordList)

print sorted(loadWords())

def removeDuplicates(array):
    for i in xrange(len(array)):
    
