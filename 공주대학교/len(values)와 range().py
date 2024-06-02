values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    # len = 10
sum = 0 # 0  1  2  3  4  5  6  7  8  9 <--- index는 0부터 시작

for i in range(len(values)):    # len() => list의 개수 ----> length 길이 
    sum = sum + values[i]   # i의 index는 0부터 9까지 된다.
print('x =', sum)
