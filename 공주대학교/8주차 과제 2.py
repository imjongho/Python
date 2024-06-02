def MysteryPrint(N):    # 재귀 함수
    if(N > 0):
        print(N)
        MysteryPrint(N-2)
    print(N+1)


# 메인 함수
MysteryPrint(3)     # 값 3
                    # MysteryPrint(3)을 call
