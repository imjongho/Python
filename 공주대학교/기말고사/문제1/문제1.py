class Calculator:
    def __init__(self, num_list):     # 초기화, 객체 cal1은 5개, cal2는 3개로
        self.num_list = num_list      # 매개변수의 개수가 다르기에 리스트로 묶어서 계산

    def sum(self):
        result = 0
        for num in self.num_list:           # 리스트에 있는 값들을 더하는 for문
            result += num                   # 모든 숫자의 합 계산
        return result

    def avg(self):
        total = self.sum()                  # 클래스 안에 있는 sum메소드(함수) 사용
        return total / len(self.num_list)   # 평균 = 모든 숫자의 합 / 숫자의 개수
        


if(__name__ == "__main__"):
    cal1 = Calculator([1, 2, 3, 4, 5])      # 인스턴스화, 객체 cal1 생성
    print(cal1.sum())
    print(cal1.avg())

    cal2 = Calculator([4, 5, 6])            # 인스턴스화, 객체 cal2 생성
    print(cal2.sum())
    print(cal2.avg())




