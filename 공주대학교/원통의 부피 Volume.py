import math

def CylinderVolume(Radius, Height):      # def로 CylinderVolume 함수 정의
    Volume = 3.14 * Radius**2 * Height   # math.pi를 3.14로 고정
    return Volume

# 메인 함수

Radius = float(input("반지름 입력: "))   # 반지름: 3.45 높이: 12.7
Height = float(input("높이 입력: "))

print("원통의 부피 = ", CylinderVolume(Radius, Height))
