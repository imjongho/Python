while True:
    try:
        current_day = int (input ('오늘 일자를 입력해주세요: '))
        assert 0 < current_day <= 31

    except ValueError:
        print('숫자만 입력해주세요.')
    except AssertionError:
        print('5월은 1일부터 31일까지 존재합니다')
    else:
        print(f'오늘은 5월 {current_day} 입니다.')
        break
    finally:
        print('-' * 40)