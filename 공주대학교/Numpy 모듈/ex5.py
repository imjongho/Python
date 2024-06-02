import numpy

a = numpy.diag([1, 2, 3])   # 대각선만 채움 : 대각 행렬
print(a)

b = numpy.zeros(5)
print(b)
print(b.dtype)  # 실수

n = 10
my_int_array = numpy.zeros(n, dtype = numpy.int)
print(my_int_array)
print(my_int_array.dtype)  # 정수

c = numpy.ones((3, 3))
print(c)

d = numpy.arange(5)
print(d)
d[1] = 9.7
print(d)            # 정수
print(d.dtype) 
d = d * 0.4         # 실수
print(d) 
print(d.dtype)

e = numpy.arange(5, dtype = float)
print(e)

f = numpy.arange(3, 7, 0.5)
print(f)
