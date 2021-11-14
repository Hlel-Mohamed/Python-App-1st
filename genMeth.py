
def alphabatical(x):
    m = True
    for i in range(len(x)):
        asc=ord(x[i])
        if (asc<65 or asc>90)and(asc<97 or asc>122):
            m = False
            break
    return m
