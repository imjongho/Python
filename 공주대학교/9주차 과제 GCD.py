def GCD(a, b):          # GCD 함수          
    while(True):
        R = a % b
        if(R != 0):
            a = b
            b = R
        else:
            break       # break로 while문을 빠져 나옴, b = 21
    return(b)           # while문 밖에서 return


# main 함수

print('GCD(1071, 1029) =', GCD(1071, 1029))     # GCD 함수 call
