a = 1071
b = 1029

while (True):
    R = a % b
    if(R != 0):
        a = b
        b = R
    else:
        break

print("GCD(1071, 1029) = ", b)
