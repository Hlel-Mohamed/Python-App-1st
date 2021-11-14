from numpy import zeros

def msgToMat(string):
    integers = [ord(c.upper())-65 for c in string]
    length = len(integers)
    m = zeros((2,int(length/2)))
    i=0
    for column in range(int(length/2)):
        for row in range(2):
            m[row][column]=integers[i]
            i+=1
    return m
def keyToMat(string):
    integers = [ord(c.upper())-65 for c in string]
    length = len(integers)
    m = zeros((2,int(length/2)))
    i=0
    for row in range(int(length/2)):
        for column in range(2):
            m[row][column]=integers[i]
            i+=1
    return m

def inversible(determinant):
    for i in range(26):
        inverse = determinant * i
        if inverse%26 ==1:
            return i
    return -1