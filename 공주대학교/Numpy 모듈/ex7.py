import numpy as np

data = np.load("saved_matrix.npy")
print(data, "\n")   
print(data.ndim)        # 차원
print(data.size)        # 크기
print(data.shape)       # n행 m열
print(data.dtype)       
print(data.itemsize, "\n")    # 하나의 원소를 저장한 바이트의 크기


x = np.array([1, 2, 3, 4])
y = x.copy()
print(x is y)
x[0] = 9
print(x)
print(y, "\n")


arr = np.arange(10, 20)
div_by_3 = (arr % 3 == 0)
print(div_by_3)
print(arr[div_by_3], "\n")


arr2 = np.arange(10, 20)
print(arr2)
arr2 = arr2.reshape(2, 5)     # 차원 설정 중요
print(arr2)
arr2 = arr2.reshape(5, 2)
print(arr2, "\n")


print(arr2.sum())
print(arr2.mean())
print(arr2.std())
print(arr2.max())
print(arr2.min())
print(div_by_3.all())
print(div_by_3.any())
print(div_by_3.sum())
print(div_by_3.nonzero())




