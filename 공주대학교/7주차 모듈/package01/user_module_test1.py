import user_module      # import : 외부 모듈 내의 다른 코드에 대한 접근
                        # 다른 코드 : 변수, 함수, 클래스 사용 가능

# 1. 모듈명.함수, 변수, 클래스(매개 변수)
print(user_module.plus(10, 5))

from user_module import minus, divide

# 모듈명 생략 가능, 단 minus함수만 가능
print(minus(10, 5))
print(user_module.multiply(10, 5))      # 가능
# print(multiply(10, 5))                # 불가능
print(int(divide(10, 5)))               # 가능

from user_module import *
# 모든 것을 임포트(모듈 생략)(코드 가독성을 저하시킴)
# 왠만하면 사용하지 말자

print(plus(4, 8))
print(minus(4, 8))
print(multiply(4, 8))
print(divide(4, 8))

# as : 별칭 생성(부르는 이름을 다시 설정), 긴 이름 -> 짧은 이름
import user_module as m

print(m.plus(3, 4))
print(m.minus(3, 4))
print(m.multiply(3, 4))
print(m.divide(3, 4))

"""
import sys
print(sys.builtin_module_names)

for path in sys.path:
    print(path)
"""












