# 5단 구구단

multiplier = 5              # 5단
for i in range(1, 10):      # i = 1부터 9까지 범위
    print(multiplier, '*', i, '=', multiplier * i)

print('----------------------------------------------------')

# 5단과 6단

for multiplier in range(5, 7):  # multiplier = 5부터 6까지
    for i in range(1, 10):      # i = 1부터 9까지 
        print(multiplier, '*', i, '=', multiplier * i)
    print('-----------')
  
