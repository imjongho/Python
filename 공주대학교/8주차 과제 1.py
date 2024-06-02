def Exercise(N):    # 재귀 함수
    print(N)
    if(N < 3):
        Exercise(N+1)
    print(N)


# 메인 함수

Exercise(1)   # N에 1을 배정
              # Exercise(1)을 call  
