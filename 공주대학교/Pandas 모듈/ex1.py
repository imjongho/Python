import pandas as pd

# 1차원 배열
dates = pd.date_range("20181201", periods = 3)
print(dates)

prices = ['1000', '2000', '3000']   # data값
s = pd.Series(prices, index = dates)
print(s)
print(type(s), "\n")

s[pd.to_datetime('2018-12-04')] = 4000
print(s, "\n")

print(s[1])
print(s['2018-12-02'], "\n")

# 2차원 배열
prices = {'A전자':[1000, 1010, 1020],     # dictionary
          'B전자':[2000, 2010, 2020],
          'C전자':[3000, 3010, 3020]}

df1 = pd.DataFrame(prices)
print(df1)

df2 = pd.DataFrame(prices, index = dates)
print(df2, "\n")

print(df2.iloc[0, 0])
print(df2.iloc[0, :])
print(df2.iloc[:, 0])
print(df2.loc['2018-12-02'])
print(df2.loc[:, 'A전자'], "\n")

df2['D엔터'] = [4000, 4010, 4020]
print(df2, "\n")

new_prices = [1010, 1020, 1030]
new_s = pd.Series(new_prices, index = dates)

df2["E텔레콤"] = new_s
print(df2, "\n")

print(s)
print(new_s)
new_s.name = 'F소프트'
print(new_s)

df2 = pd.concat([df2, new_s], axis = 1)
print(df2, "\n")


df3 = df2.iloc[1]
print(df3)
df3 = df3 + 60
print(df3)
df3.name = pd.to_datetime('20181207')
print(df3)
df2 = df2.append(df3)
print(df2)


df3 = df2.iloc[0]
df3 = df3 + 50
df3.name = pd.to_datetime('20181206')
df2 = df2.append(df3)
print(df2, "\n")

# 인데스 정렬

df2 = df2.sort_index(axis = 0, ascending = True)
print(df2, "\n")

df2 = df2.sort_index(axis = 0, ascending = False)
print(df2, "\n")

df2 = df2.drop(pd.to_datetime('20181203'), axis = 0)
print(df2, "\n")

df2 = df2.drop(['B전자'], axis = 1)
print(df2, "\n")



