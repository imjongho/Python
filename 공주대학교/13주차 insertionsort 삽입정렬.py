S = [11, 9, 17, 5, 12, 14, 23, 52, 3]      # S[0] = 11, S[1] = 9, S[2] = 17, S[3] = 5, S[4] = 12

def insertionsort(S):                   
    for i in range(1, len(S)):          # 맨 앞의 11은 옮기지 않아도 되기에 i가 1부터 시작
        x = S[i]                        
        j = i - 1                       # 바로 이전 값에 위치           
        while(j >= 0 and S[j] > x):     # 몇 번째 자리에 값을 넣어야 하는지 찾는 과정
            S[j+1] = S[j]               
            j = j - 1
        S[j+1] = x                      
    print(S)

                                        
# 메인 함수
insertionsort(S)




