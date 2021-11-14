print('----------Hill Decryption----------')
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


cipher = input("Input 4 letter cipher: ")
key_mat=keyToMat(cipher)
msg_mat=msgToMat(msg)

hill_encrypt()


determinant = 0
#determinant = key_mat[0][0]*key_mat[1][1]-key_mat[0][1]*key_mat[1][0]

#determinant %= 26





