from urllib.request import urlopen
import bs4
import datetime

# 규칙 source = urlopen('https://finance.naver.com/sise/sise_index_day.nhn?code=KPI200&page=1')

# 매개변수
index_cd = 'KPI200'
page_n = 1
source = urlopen('https://finance.naver.com/sise/sise_index_day.nhn?code=' + index_cd + '&page=' + str(page_n)).read()
print(source)

source = bs4.BeautifulSoup(source, 'lxml')
print(source.prettify())        # prettify => 예쁘게 정렬

td = source.find_all('td')
print(len(td))  # page에 td가 54개 있다.


# 오른쪽 클릭 -> copy -> XPath(카피한 원하는 경로) /html/body/div/table[1]/tbody/tr[3]/td[1]
data = source.find_all('table')[0].find_all('tr')[2].find_all('td')[0]
print(data)
print(data.text)

# 다른 방법

def date_format(d):
    d = str(d).replace('-', '.')
    yyyy = int(d.split('.')[0])     #구별자 .
    mm = int(d.split('.')[1])
    dd = int(d.split('.')[2])
    
    this_date = datetime.date(yyyy, mm, dd)
    return this_date


date1 = source.find_all('td', class_ = 'date')[2].text
date_format(data.text)
date_format(date1)

