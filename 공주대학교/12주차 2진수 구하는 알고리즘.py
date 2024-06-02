b = []                              # 빈 리스트 b
n = int(input("10진수 입력: "))

while(n!=0):                # 몫이 0이 아니면 반복            
    b.append(n%2)           # n을 2로 나눈 나머지를 b에 추가
    n = n//2                # n을 2로 나눈 몫을 n에 저장

b.reverse()                 # reverse로 리스트 b를 역순으로 변경(원본이 변경됨) 

for i in range(len(b)):     # len(b) --> 리스트 b의 개수 
    print(b[i], end=" ")    # end=" "로 줄바꿈 X



