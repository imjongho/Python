menu = ["냉면", "볶음밥", "피자", "짜장면"]
while 1:
    order = input("메뉴를 선택해주세요 ( 1. 냉면, 2. 볶음밥, 3. 피자, 4. 짜장면 (숫자로 입력해주세요)] : ")
    try: 
        print(menu[int(order) - 1] + "을 선택하셨습니다.")
    except ValueError:
        print("숫자만 입력하세요")
    except IndexError:
        print("없는 메뉴입니다.")
    else:
        break
    finally:
        print("------------------------")