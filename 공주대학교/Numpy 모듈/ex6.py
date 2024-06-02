import numpy as np

x, y = np.mgrid[0:5, 0:5]   # 두 변수 필요
print(x, "\n")
print(y, "\n")

a = np.random.rand(5, 5)    # 0~1사이의 랜덤한 숫자
print(a, "\n")

data = np.genfromtxt("temp_file.txt", delimiter = ",", skip_header = 1)
# delimiter : 구분 문자
print(data)
print(data.shape, "\n")

np.save("saved_matrix.npy", x)
data2 = np.load("saved_matrix.npy")
print(data2)

