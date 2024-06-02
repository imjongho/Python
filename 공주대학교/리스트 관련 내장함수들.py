# list에 관련된 내장 함수들

# len(List) --> List에 들어 있는 항목의 개수를 반환
# max(List) --> List에 들어 있는 항목의 최댓값을 반환
# min(List) --> List에 들어 있는 항목의 최솟값을 반환
# sum(List) --> List에 들어 있는 항목 값의 합계를 반환

# list와 문자열은 결합 => 오류 but, [문자열]은 결합 가능

first = ['apple', 'banana']
second = first + ['pineapple']  # + 'pineaplle'은 오류남 
print(second)
