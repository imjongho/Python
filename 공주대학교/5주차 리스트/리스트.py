
a = [1, 2, 3]   # list 변함
b = (1, 2, 3)   # tuple 변하지 않음

print(a)
a.append(4)
print(a)
a.extend([5, 6, 7])
print(a)
a.insert(2, 10)
print(a)
a.remove(10)
print(a)
a.pop()
print(a)
print(a.index(2))
one, two, three = a  # 언패킹
print(one + 10)

"""
dic = {}
dic['파이썬'] = 'www.python.org'
dic['마이크로소프트'] = 'www.Microsoft.com'
dic['apple'] = 'www.apple.com'

print(type(dic))
print(dic)
print(dic['마이크로소프트'])

print(dic.keys())
print(dic.values())
print(dic.items())

print('apple' in dic.keys())

dic.pop('apple')
print(dic)

dic.clear()
print(dic)
"""
