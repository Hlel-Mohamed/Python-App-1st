print('----------Hill Decryption----------')
from numpy import zeros

#msg = input("Plain text : ")
#msg=msg.replace(" ", "")

def txtToMat(string):
    integers = [ord(c.upper())-65 for c in string]
    length = len(integers)
    print(integers)
    m = zeros((2,int(length/2)))
    i=0
    for row in range(int(length/2)):
        for column in range(2):
            m[row][column]=integers[i]
            i+=1
    print(m)
    return m

determinant = 0

cipher = input("Input 4 letter cipher: ")
c=txtToMat(cipher)
determinant = c[0][0]*c[1][1]-c[0][1]*c[1][0]
print(determinant)

determinant %= 26
print(determinant)





