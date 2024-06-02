count = 0

while (count < 4):
    count = count + 1
    print("{}회 반복".format(count))

print("\n-------------------------------\n")

while True:
    print("반복을 계속할까요? [예/아니요] : ")
    answer = input()
    if answer == '예':
        print("반복을 계속합니다.")
    elif answer == "아니요":
        print("프로그램 종료")
        break
    else:
        print("정상적인 답변이 아닙니다.")

print("\n-------------------------------\n")

n = int(input("숫자 입력 : "))

sum = 0
step = 0

while step <= n:
    sum = sum + step
    step = step + 1
print(sum)

print("\n-------------------------------\n")
 
# range([start], stop, [step]) -> start부터 step만큼씩(증가/감소) stop전까지 범위를 지정하는 함수
# start 생략 --> 0 고정, step 생략 --> 1 고정, stop 생략 불가

n = int(input("숫자 입력"))

sum = 0
step = 0

for step in range(0, n + 1, 1):   # 시작 ~ 끝 - 1
    sum = sum + step
print(sum)























