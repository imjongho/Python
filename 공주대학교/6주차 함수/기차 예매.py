destination_pay = {"춘천":5000, "부산":30000, "대구":20000, "수원":10000}
train_type_pay = {"KTX":10000, "새마을호":5000, "무궁화호":3000}
seat_pay = {"좌석":0, "입석":-2000}

total_pay = 0

def first_stage(key):
    global total_pay
    total_pay = total_pay + destination_pay[key]

def second_stage(key):
    global total_pay
    total_pay = total_pay + train_type_pay[key]

def third_stage(key):
    global total_pay
    total_pay = total_pay + seat_pay[key]


destination = input("도착지점 : ")
first_stage(destination)
train_type = input("기차유형 : ")
second_stage(train_type)
seat = input("좌석 or 입석 : ")
third_stage(seat)

print("지불하실 금액은 {0}원 입니다".format(total_pay))
