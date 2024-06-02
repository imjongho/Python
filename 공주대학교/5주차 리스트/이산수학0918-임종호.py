"""
A = set([ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' ])   # A 집합의 초기값
B = set([ 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ])             # B 집합의 초기값
C = set([ 'a', 'c', 'e', 'g', 'i' ])                            # C 집합의 초기값
# set 집합 : 순서가 없고 중복을 허용하지 않는다.
"""

A = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j' }     # set = 중괄호
B = { 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' }             
C = { 'a', 'c', 'e', 'g', 'i' }

print("A =", sorted(A))
print("B =", sorted(B))
print("C =", sorted(C))

print("\n(1) A - B")                # 차집합 계산
print(sorted(A - B))                # 차집합 : 빼기(-), difference 함수
print(sorted(A.difference(B)))      # sorted 정렬함수

print("\n(2) A - C")                 
print(sorted(A - C))                
print(sorted(A.difference(C))) 

print("\n(3) B - A")                 
print(sorted(B - A))                
print(sorted(B.difference(A)))

print("\n(4) C - A")                 
print(sorted(C - A))                
print(sorted(C.difference(A)))

print("\n(5) |A∩B|")                # 교집합 계산                 
print(sorted(A & B))                 # 교집합 : 그리고(&), intersection 함수
print(sorted(A.intersection(B)))     # 절대값(기수) : 원소의 개수
print("원소의 개수 : ", len(A & B))  # len() 함수 : 원소의 개수

print("\n(6) A 대칭차집합 B")
print(sorted(A ^ B))                         # 대칭차집합 계산
print(sorted(A.symmetric_difference(B)))     # 대칭차집합 : ^, symmetric_difference 함수
print(sorted((A | B) - (A & B)))             
