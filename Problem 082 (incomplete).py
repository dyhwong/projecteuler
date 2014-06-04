class Matrix:
    def __init__(self, filename):
        inFile = open(filename, 'r+')
        array = inFile.read().split('\n')[:-1]
        matrix = []
        for row in array:
            matrix.append(str(row).split(','))
        self.matrix = matrix

    def __str__(self):
        print '['
        for row in self.matrix:
            print row
        print ']'
        return ''

    def entry(self, (r, c)):
        return self.matrix[r][c]

    def successors(self, (r, c)):
        array = []
        if r < 0 or r >= len(self.matrix) or c < 0 or c >= len(self.matrix):
            return None
        if r != len(self.matrix) - 1:
            array.append((r + 1, c))
        if c != len(self.matrix) - 1:
            array.append((r, c + 1))
        return array

def main():
    matrix = Matrix('matrix82.txt')
