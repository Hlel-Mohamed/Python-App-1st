def alphabatical(x):
    for i in range(len(x)):
        if (ord(x[i])>=65 and ord(x[i])<=90)or(ord(x[i])>=97 or ord(x[i])<=122):
            return True
    return False