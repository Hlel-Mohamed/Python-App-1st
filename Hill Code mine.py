print('----------Hill Encryption----------')
from numpy import zeros

msg = input("Plain text : ")
space = [i for i in range(len(msg)) if msg.startswith(" ", i)]
msg=msg.replace(" ", "")
if len(msg)%2 != 0:
    msg += "0"

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


def hill_encrypt():
    enc_msg=""
    for i in range (int((len(msg)/2))):
        row=msg_mat[0][i]*key_mat[0][0]+msg_mat[1][i]*key_mat[0][1]
        elem=int (row%26 + 65)
        enc_msg+=chr(elem)
        row=msg_mat[0][i]*key_mat[1][0]+msg_mat[1][i]*key_mat[1][1]
        elem=int (row%26 + 65)
        enc_msg+=chr(elem)
    for i in space:
        enc_msg=enc_msg[:i] + " " + enc_msg[i:]
    print(enc_msg)



def adjugate(c):
    adju = c
    adju[0][0], adju[1][1] = adju[1, 1], adju[0, 0]
    adju[0][1] *= -1
    adju[1][0] *= -1
    adju %=26
    return adju

def multDet(key_mat,determinant):
    return adjugate(key_mat)*inversible(determinant)%26

cipher = input("Input 4 letter cipher: ")
key_mat=keyToMat(cipher)

determinant = 0
determinant = key_mat[0][0]*key_mat[1][1]-key_mat[0][1]*key_mat[1][0]
determinant %= 26

print(inversible(determinant))
print(key_mat)
print(multDet(key_mat,determinant))

msg_mat=msgToMat(msg)
#hill_encrypt()