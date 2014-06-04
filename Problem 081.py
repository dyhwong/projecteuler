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
    matrix = Matrix('matrix81.txt')
    D = {}
    def DP((r, c)):
        if (r, c) in D:
            return D[(r, c)]
        if (r, c) == (79, 79):
            D[(79, 79)] = int(matrix.entry((79, 79)))
            return D[(79, 79)]
        D[(r, c)] = int(matrix.entry((r, c))) + min([DP((i, j)) for (i, j) in matrix.successors((r, c))])
        return D[(r, c)]
    
    print DP((0, 0))

main()
