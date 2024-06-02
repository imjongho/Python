from urllib.request import urlopen
import bs4

index_cd = 'KPI200'
page_n = 1
source = urlopen('https://finance.naver.com/sise/sise_index_day.nhn?code=' + index_cd + '&page=' + str(page_n)).read()
source = bs4.BeautifulSoup(source, 'lxml')

# /html/body/div/table[1]/tbody/tr[3]/td[2]
data = source.find_all('table')[0].find_all('tr')[2].find_all('td')[1].text
data = data.replace(',', '')   # 천의 자리 쉼표 제거
data = float(data)
print(data, "\n\n")


price = source.find_all('td', class_ = 'number_1')
dates = source.find_all('td', class_ = 'date')

for n in range(0, len(dates)):
    this_date = dates[n].text
    print(this_date, end=' ')
    
    this_close = price[n*4].text
    this_close = this_close.replace(',', '')   # 천의 자리 쉼표 제거
    this_close = float(this_close)
    print(this_close)
