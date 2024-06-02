days = [1, 2, 3, 4, 5, 6, 7]
today = days[5]
print("today =", today)     # 출력값: 6

tomorrow_day = days
print("tomorrow day =", tomorrow_day[6])

print('---------------------')

# 빈 리스트(empty list)

# days = []

# 혼합된 리스트(mixed list)
# list는 정수, 문자열, 심지어 다른 리스트까지 모든 데이터를 담을 수 있다.

List = ['Lee', 'Kr', -12.5, 15.5]
print('List[0] =', List[0])
print('List[3] =', List[3])

# 혼합된 리스트의 변경
List[1] = "Welcome"     # Krdl Welcome으로 변함
print("List[1] =", List[1])
