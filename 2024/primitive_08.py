def remove_duplicates(input_list):
    return list(set(input_list))


test_list = [1, 3, 2, 1, 5, 2, 7, 8, 3]
print("원본 리스트:", test_list)
print("중복 제거 후:", remove_duplicates(test_list))
