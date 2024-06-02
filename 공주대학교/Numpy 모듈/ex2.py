import numpy as np

l = [[1, 2, 3], [3, 6, 9], [2, 4, 6]]
a = np.array(l)
print(a)
print(a.shape)  # 3행 3열
print(a.dtype)  # 32비트

M = np.array([[1, 2], [3, 4]], dtype = complex)     # 복소수, 실수면 float
print(M)
print(M.shape)
print(M.dtype)

