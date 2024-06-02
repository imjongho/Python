def hello():
    print("Hello World!")

def abs(arg = -7):      # 기본값 매개변수 : arg = -7
    result = 0
    if (arg < 0):
        result = arg * -1
    else:
        result = arg
    return result

def print_string(text, count = 1):
    for i in range(count):
        print(text)

# 문자열 안의 ‘{번호}’ 가 format() 멤버함수의 인자의 내용으로 치환 
def print_personnel(name, position = "staff", nationality = "Korea"):
    print("name = {0}".format(name))
    print('position = {0}'.format(position))
    print('nationality = {0}'.format(nationality))

# 가변 매개변수(*매개변수, 튜플로 취급()) : 입력 개수가 달라질 수 있는 매개변
def merge_string(*text_list):
    result = ''
    for s in text_list:
        print(s)
        result = result + s
    return result

# 딕셔너리 형식 가변 매개변수... ///

def print_args(argc, *argv):
    for i in range(argc):
        print(argv[i])

def multiply(a, b):
    return a * b


# 메인 함수
"""
print(multiply(2, 5))
        
print_args(4, "argv1", "argv2", "argv3", "argv4")

print(merge_string("아버지가", "방에", "들어가신다."))
# text_list[0] = "아버지가"

hello()

print(abs())
print(abs(-3))
print(abs(10))
print(abs(-5.5))

print_string("안녕하세요")
print()
print_string("안녕하세요", 3)

print_personnel('임종호', "Japan")     # 매개변수 잘못된 예
print_personnel(name = "임종호", nationality = "Japan")
print_personnel(name = "임종호", position = "인턴")
"""

