def loadWords():
    inFile = open('keylog.txt', 'r+')
    wordList = "".join(inFile.read().split('"')).split('\n')
    wordList = [n for n in wordList if n]
    return sorted(wordList)

print sorted(loadWords())

def removeDuplicates(array):
    array = sorted(array)
    new_array = [array[0]]
    for i in xrange(1, len(array)):
        if new_array[-1] != array[i]:
            new_array.append(array[i])

    return new_array

print removeDuplicates(loadWords())

#completed with pencil and paper

