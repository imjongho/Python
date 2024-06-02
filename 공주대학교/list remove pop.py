letters = ['a', 'b', 'c', 'd', 'e']

letters.remove('d')             # letters에서 'd'을 삭제
print('letters =', letters)     # remove(빼고 싶은 내용)

last_letters = letters.pop()    # lstters의 마지막 항목, 즉 'e'을 가져옴
print('pop() =', last_letters)  # pop()은 이스트의 마지막 항목을 가져옴

pop_two = letters.pop(2)        # letters의 index 2, 즉 'c'을 가져옴
print("pop_two =", pop_two)     # letters에서 c가 없어지고 pop_two에 저장됨    

print('letters =', letters) 
