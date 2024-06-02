class AirConditioner:
    def __init__(self):             # 초기화
        self.temp = 25              # 멤버변수 : temp = 온도(실수), power = 전원상태(boolean)
        self.power = False          # 초기 전원은 off 상태, 초기 온도는 25(변경 가능)

    def turn_on(self):              # 전원을 키는 메소드(함수)
        self.power = True

    def turn_off(self):             # 전원을 끄는 메소드
        self.power = False

    
    # 전원이 On 상태가 아니면 아래 메소드들이 수행되지 않음
    
    def setTemp(self, temp):              # 온도입력(입력한 온도로 설정) 메소드
        if(self.power == True):
            self.temp = temp

    def getTemp(self):                    # 온도반환(온도를 리턴) 메소드
        if(self.power == True):
            return self.temp

    def read_temp(self):                  # 현재온도출력 메소드
        if(self.power == True):
            print("현재 온도 : ", self.temp)

    def increment_temp(self):             # 현재온도증가(1도 증가) 메소드
        if(self.power == True):
            self.temp += 1 

    def decrement_temp(self):             # 현재온도감소(1도 감소) 메소드
        if(self.power == True):
            self.temp -= 1




if(__name__ == "__main__"):
    ac = AirConditioner()       # 객체 ac 생성
    ac.read_temp()              # 전원 off 상태에서 출력 불가능

    ac.turn_on()                # 전원 on
    ac.read_temp()              # 전원 on 상태에서 출력 가능
    
    ac.setTemp(20)              # 온도 입력(20)
    ac.read_temp()

    # ac.turn_off()             # 전원 off, 기능이 수행되지 않음
    
    ac.increment_temp()         # 온도 2도 증가
    ac.increment_temp()
    ac.read_temp()

    ac.decrement_temp()         # 온도 1도 감소
    ac.read_temp()
    






    
            
