import numpy as np

A = {'a', 'b', 'c', 'd'}    # 집합 A 정의
R = [['a', 'b'], ['b', 'b'], ['b', 'c'], ['c', 'a']]    # 관계 R 정의 [행, 열]
S = []    # 추이폐포 
M = np.matrix([[0, 1, 0, 0], [0, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0]])
# 제곱하면서 바뀌는 행렬
M_lock = np.matrix([[0, 1, 0, 0], [0, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0]])
# 변하지 않는 행렬(고정)
Temp = np.matrix([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
# 값을 임시로 저장하기 위한 빈 행렬

# 관계 R에 대한 행렬 M(관계에 맞게 1로 채워줌)
# 'a' : 1행, 1열, 'b' : 2행, 2열, 'c' : 3행, 3열, 'd' : 4행, 4열

 
def boolean_product(M_lock, M, Temp, num):  # 추이폐포의 연결관계를 구하는 함수
    M_lock_t = M_lock.T                     # 전치 행렬
    cnt = 1
    print("\nR\n")
    print(M_lock)
    while(cnt < num):        
        for i in range(0, num, 1):       
            for j in range(0, num, 1):
                for k in range(0, num, 1):
                    if(M[i, k] & M_lock_t[j, k] == 1):
                        Temp[i, j] = 1
                    
        for i in range(0, num, 1):
            for j in range(0, num, 1):
                M[i, j] = Temp[i, j]       
                Temp[i, j] = 0          # Temp는 다시 빈 행렬로 초기화

        print("\nR^{0} = R^{1} 부울곱 R\n".format(cnt+1, cnt))
        print(M)
        cnt = cnt + 1
        
    return M    # 필요하면 사용(지금은 사용 안함)

# 교집합 &(그리고) : 하나만 1이면 1
# 합집합 |(또는) : 모두 1이면 1


# 메인 함수

num = len(A)         
print("A의 기수 : |A| =", num)   # A의 기수

M = boolean_product(M_lock, M, Temp, num)
# boolean_product(고정 행렬, 변동 행렬, 빈 행렬, 집합의 기수)

cnt = 0

for i in range(0, num):             # 추이폐포 S 숫자
    for j in range(0, num):
        if(M[i, j] == 1):
            S.extend([[i, j]])      # 리스트 확장
            cnt += 1

for i in range(0, cnt):             # 문자로 변경
    for j in range(0, 2):
        if(S[i][j] == 0):
            S[i][j] = 'a'
        elif(S[i][j] == 1):
            S[i][j] = 'b'
        elif(S[i][j] == 2):
            S[i][j] = 'c'
        elif(S[i][j] == 3):
            S[i][j] = 'd'            

print("\n추이폐포 S =", S)
        


  
