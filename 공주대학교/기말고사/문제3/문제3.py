import numpy as np

def movieInfo(num):     # 영화번호를 매개변수로 영화정보를 출력하는 함수
    try:
        index = np.where(movies == str(num))[0][0]    # 인덱스 행 위치 찾기
        # print(index)
        title = movies[index][1]                    # 영화이름(제작년도)
        genres = movies[index][2].split('|')        # 장르|장르|...

        # 영화 제목에 ()가 있는 경우가 있기 때문에
        if(title.count('(') >= 2):
            title = title.rstrip(')')    # 오른쪽 끝 ')' 제거
            title = title.replace(') (', '  ').split('  ')
            print("영화이름 :", title[0], end = ")")
            for i in range(1, len(title) - 1, 1):
                print(' (' + title[i] + ')', end = "")
            print("\n제작년도 :", title[len(title) - 1])
        else:
            title = title.replace(')', '').split(' (')
            print("영화이름 :", title[0])
            print("제작년도 :", title[1])
        
        print("영화장르 :", end = " ")
        for genre in genres:
            print(genre, end = " ")
        print("\n")
        
    except IndexError as err:               # 만약 없는 영화번호를 입력했을 때, 오류메세지 표시
        print("{0}은 없는 영화번호입니다.".format(num))
        print("이유 :", err, "\n")




def movieInfoByGenre(genre):     # 영화장르를 입력하면 관련된 영화 이름 전체가 출력되는 함수
    count = 0                    # 장르가 몇개 있는지 세는 변수
    for i in range(0, len(movies), 1):  # 모든 행에 대하여
        if genre in movies[i][2]:       # 만약 i행 2열(장르)에 입력값이 있다면 수행
            count += 1
            title = movies[i][1] 
            if(title.count('(') >= 2):
                title = title.rstrip(')')
                title = title.replace(') (', '  ').split('  ')
                print(title[0], end = ")")
                for j in range(1, len(title) - 1, 1):
                    print(' (' + title[j] + ')', end = "")
                print()
            else:
                title = title.replace(')', '').split(' (')
                print(title[0])
            
    try:
        if(count == 0):     # 입력한 장르가 없음을 의미
            raise Exception("{0}장르와 관련된 영화는 없습니다.".format(genre))
    except Exception as err:
        print(err)
                




# main

movie_info = []      # 영화 하나의 리스트
movies_info = []     # 영화들의 리스트

with open('movies.dat', 'r') as file:            # movies.dat 파일 읽기
    for line in file.readlines():
        movie_info = line.strip().split("::")    # ::을 기준으로 나눈다.
        movies_info.append(movie_info)           # 영화번호, 영화이름(제작년도), 영화장르

movies = np.array(movies_info, dtype = None)     # numpy 객체에 문자열로 2차원 배열 저장(3952행 * 3열)
print(movies, "\n\n")


# 값이 없는 경우도 있다. (증거) 90 -> 92(91번 영화가 없음))
movieInfo(1)        # 제목에 가로()가 1개 있는 경우
movieInfo(3952)

movieInfo(293)      # 제목에 가로가 2개 있는 경우
movieInfo(683)

movieInfo(2019)     # 제목에 가로가 3개 있는 경우

movieInfo(91)       # 오류
movieInfo(-6)
movieInfo(7000)



print("\n\nAnimation 장르에 속하는 영화")
movieInfoByGenre('Animation')
print("\n\nMusical 장르에 속하는 영화")
movieInfoByGenre('Musical')

print("\n")     # 오류
movieInfoByGenre("Children'zz")
movieInfoByGenre('drama')



    
