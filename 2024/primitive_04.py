coffee = {"아메리카노": 2500, "바닐라라떼": 3200,"초코라뗴": 5000,"시그니쳐커피": 6500}

order = input('안녕하세요! 어떤 메뉴로 주문하시겠어요?')
if order in coffee.keys():
    print(f'{order} 메뉴 주문 받았습니다. {coffee[order]} 원입니다.') 