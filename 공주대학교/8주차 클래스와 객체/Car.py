class Car:
    def __init__(self, manufacturer, model, year):  # 초기화
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        car_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return car_name         # 문자열 반환
        
    def read_odometer(self):    # 현재까지 주행거리 출력
        print("This car has {0} miles on it".format(self.odometer))

    def update_odometer(self, reset):      # 주행거리 재설정
        if(reset >= self.odometer):        # 단, 현재 주행거리보다 큰 값만
            self.odometer = reset
        else:
            print("error!!")

    def increment_odometer(self, miles):   # 주행거리를 매개변수만큼 증가시킴
        self.odometer += miles




if(__name__ == "__main__"):
    my_new_car = Car("Audi", "A4", 2015)
    print(my_new_car.get_descriptive_name())
    my_new_car.increment_odometer(42)
    my_new_car.read_odometer()
    my_new_car.update_odometer(10)
    
    print()
    
    my_old_car = Car("Samsung", "SM7", 2009)
    print(my_old_car.get_descriptive_name())
    my_old_car.update_odometer(15000)
    my_old_car.read_odometer()
    my_old_car.increment_odometer(28)
    my_old_car.read_odometer()




    
        
