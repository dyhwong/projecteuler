from operator import xor

def loadCipher():
    inFile = open('cipher1.txt', 'r+')
    numberList = inFile.read().split(',')
    return numberList

def buildKeys():
    keys = []
    string = 'abcdefghijklmnopqrstuvwxyz'
    for letter in string:
        for letter2 in string:
            for letter3 in string:
                keys.append([letter, letter2, letter3])
    return keys

def findKey():
    for key in buildKeys():
        message = ''
        for i in xrange(len(loadCipher())):
            if i % 3 == 0:
                message += chr(xor(ord(key[0]), int(loadCipher()[i])))
            elif i % 3 == 1:
                message += chr(xor(ord(key[1]), int(loadCipher()[i])))
            else:
                message += chr(xor(ord(key[2]), int(loadCipher()[i])))
        if 'the ' in message.lower() and 'to ' in message.lower():
            print message, key

def decrypt():
    message = ''
    for i in xrange(len(loadCipher())):
        if i % 3 == 0:
            message += chr(xor(ord('g'), int(loadCipher()[i])))
        elif i % 3 == 1:
            message += chr(xor(ord('o'), int(loadCipher()[i])))
        else:
            message += chr(xor(ord('d'), int(loadCipher()[i])))
    return message

def main():
    total = 0
    for char in decrypt():
        total += ord(char)
    print total

main()
