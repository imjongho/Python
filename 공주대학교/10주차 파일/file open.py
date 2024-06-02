"""
file = open('test.txt', 'w')
file.write("hello ")
file.write("World")
file.close()


with open("test2.txt", mode = "wt") as file:
    file.write("ABC")
    # file.close() 생략

lines = ["안녕하세요!!\n",
         "저는 임종호입니다.\n",
         "현재 공주대 소프트웨어 전공입니다.\n"]

with open("self_introduction.txt", "w") as file:
    for line in lines:
        file.write(line)
    file.writelines(lines)  # 위와 같은 결과
"""


with open("self_introduction.txt", "r") as file:
    line = file.readline()

    while line != '':
        print(line, end='')
        line = file.readline()

print("\n-------------------------------------------\n")
  
with open("self_introduction.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    
    for line in lines:
        print(line, end='')
