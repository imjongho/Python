import numpy as np

# 모두 1차원

x = np.arange(0, 10, 1)     # start, stop, step
print(x)

y = np.linspace(0, 10, 25)  # 시작과 끝을 포함한 25개의 데이터 만들기
print(y)

z = np.logspace(0, 10, 10, base = np.e) # 시작, 끝, 생성할 데이터의 수, 자연상수 e
print(z)
