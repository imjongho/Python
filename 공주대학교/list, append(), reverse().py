list = []   # 빈 리스트

i = 0
while(i <= 4):
    list.append(i)  # list 끝에 추가 [0, 1, 2, 3, 4] append = 덧붙이다
    i = i + 1

i = i - 1   # i값이 4가 된다.
print("i = ", i)

while(i >= 0):
    print(list[i], end=' ')
    i = i - 1

list.reverse() # list을 역순(reverse)으로
print("\nlist = ", list)

list.reverse() # list을 역순(reverse)으로
print("list = ", list)

# reverse()와 append() 함수는 앞에 list.으로 쓴다.
# .이 반드시 필요
