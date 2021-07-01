# MED minimum Edit Distance with backtracking

class Node:
    def __init__(self,num1):
        self.num1 =num1
        self.nextval = None
    def __int__(self, num1, node ):
        self.num1 = num1
        self.nextval = node


def findMinDistance(name1, name2):
    len1 = len(name1)
    len2 = len(name2)
    totalSum = 0

    rows, cols = (len1, len2)
    matrix = [[ Node(0) for i in range(cols)] for j in range(rows)]

    for i in range(len1):
        for j in range(len2):
            t1 = name1[i]
            t2 = name2[j] # for debugging purpose
            if name1[i] == name2[j]:
                if i == 0 and j == 0:
                    matrix[i][j] = Node(0)  # which means there is no change
                elif i == 0 or j == 0:
                    if j != 0:
                        matrix[i][j] = Node(matrix[i][j - 1].num1)
                        matrix[i][j].nextval = matrix[i][j-1]
                    else:
                        matrix[i][j] = matrix[i - 1][j]
                else:
                    a1 = matrix[i - 1][j].num1
                    a2 = matrix[i][j - 1].num1
                    a3 = matrix[i - 1][j - 1].num1
                    matrix[i][j] = Node(min(a1, a2, a3))
                    if matrix[i][j].num1 == a1:
                        matrix[i][j].nextval = matrix[i - 1][j]
                    elif matrix[i][j].num1 == a2:
                        matrix[i][j].nextval = matrix[i][j - 1]
                    else:
                        matrix[i][j].nextval = matrix[i - 1][j - 1]
            else:
                if i == 0 and j == 0:
                    matrix[i][j] = Node(1)
                elif i == 0 or j == 0:
                    if j != 0:
                        matrix[i][j] = Node(matrix[i][j - 1].num1 +1)
                        matrix[i][j].nextval = matrix[i][j]
                    else:
                        matrix[i][j] = Node(matrix[i - 1][j].num1 + 1)
                        matrix[i][j].nextval = matrix[i - 1][j]
                else:
                    a1= matrix[i - 1][j].num1
                    a2= matrix[i][j - 1].num1
                    a3= matrix[i - 1][j - 1].num1
                    matrix[i][j] = Node(min(a1 + 1, a2 + 1, a3 + 1))
                    if matrix[i][j].num1 == a1:
                        matrix[i][j].nextval = matrix[i - 1][j]
                    elif matrix[i][j].num1 == a2:
                        matrix[i][j].nextval = matrix[i][j - 1]
                    else:
                        matrix[i][j].nextval = matrix[i -1][j - 1]
    print("\n\n")
    print("Printing the matrix...")
    for i in range(len1):
        for j in range(len2):
            print(matrix[i][j].num1, end=" ")
        print("", end="\n")
    #print("Now printing the backtracking address")
    '''
    for i in range(len1):
        for j in range(len2):
            print(matrix[i][j].nextval, end=" ")
        print("", end="\n")
    '''
    totalSum = totalSum + matrix[len1 - 1][len2 - 1].num1

    return totalSum


name1 = input("Enter first name:\t")

name2 = input("Enter second name:\t")

MED = findMinDistance(name1.lower(), name2.lower())
#MED = findMinDistance("Hello".lower(),"World".lower())
print("The minimum edit distance is:\t"+str(MED))