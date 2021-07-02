# working with n-grams
import re

file = open("shakes.txt", 'r')
buff = file.read()# buff will now contain all the words that are supposed to be existing in the shakes.txt folder, in a systematic manner
buff = re.findall("[A-Za-z]+", buff)# I am adding this in order to make the buffer list without any special characters
total = len(buff)
distinctTotal = len(set(buff))
print("for now i am making bigram matrix and bigram generator. for initial simplicity")


class Matrix:
    def __init__(self):
        self.matrix = [[None for i in range(distinctTotal)] for j in range(distinctTotal)] # initializing the matrix
        temp = list(set(buff))
        print(temp)
        for i in range(1, distinctTotal):

            self.matrix[i][0] = temp[i].lower()
            self.matrix[0][i] = temp[i].lower()
        #this will make this matrix a table of words



    def add(self, rowName, colName, val):
        global row, col
        for i in range(distinctTotal):
            if self.matrix[i][0] == rowName:
                row = i
        for j in range(distinctTotal):
            if self.matrix[0][j] == colName:
                col = j
        self.matrix[row][col] = str(val)
    def show(self, row, col):
        if row ==0 or col ==0:
            print(matrix[row][col], end="  ")
        else:
            print("\t" + matrix[row][col], end= "\t")
# Created the class

def chain(A):
    A= list(A)
    print(A)
    net = P(A[0])
    for i in range(1, len(A)):
        temp = [A[j] for j in range(1, i)]
        net = net * P(A[i]) / chain(temp)
    return net


def P(a):
    sum = 0
    for i in buff:
        if a == i:
            sum = sum + 1
    return sum / total


def PP(W, m):
    n = len(W)
    result = chain(W) ** (-1 / n)
    m.add(W[0], W[1], str(result))


def makeChain():
    matrix= Matrix()
    t= len(buff)
    '''for i in range(t):
        temp = {buff[i].lower(), buff[i+1].lower()}
        PP(temp, matrix)
        i= i+1'''
    i = 0
    while i< t:
        temp = {buff[i].lower(), buff[i+1].lower()}
        i = i+2
        PP(temp, matrix)

    #finally the matrix is made and is now ready to use.
    return matrix

matrix = Matrix()
matrix =makeChain()
for i in range(8):
    for j in range(8):
        matrix.show(i, j)
    print()
