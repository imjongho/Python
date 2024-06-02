sum = 0
i = 0
while (i <= 10):
    sum = sum + i
    i = i + 1
print("sum =", sum)

print("---------------------")

# while문을 for문으로 변환

sum = 0
for i in range(1, 11):
    sum = sum + i
print("sum =", sum)

print("----------------------")

# list 사용

sum = 0
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + i
print("sum =", sum)
