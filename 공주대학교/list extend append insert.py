my_list = ['a', 'b', 'c', 1, 2.5, 3.5, 'abc', 'def']
my_list.append("new")                   # 리스트 끝에 'new' 항목 추가
my_list.extend(['apple', 'banana'])     # 리스트에 ['apple', 'banana']을 추가
print('my_list =', my_list)             # my_list을 출력


# append()는 끝에 하나 추가
# extend()는 끝에 여러개 추가


letters = ['a', 'b', 'c']
letters.insert(3, 'd')          # 리스트의 index 3에 'd'을 추가
print('letters =', letters)
letters.insert(1, 'dog')        # 리스트의 index 1에 'dog'을 추가
print('letters =', letters) 
letters.insert(0, 3)
print("letters =", letters)

# insert(위치, 넣고 싶은 것)
