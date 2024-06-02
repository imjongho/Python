# 마라톤 훈련 Marathon training assistant

import math

def total_seconds(min, sec):
    return(min * 60 + sec)

def speed(time):
    return(3600 / time)

# main 함수

pace_minutes = int(input('Minutes per mile? '))
pace_seconds = int(input('Seconds per mile? '))
miles = int(input('Total mile? '))

mph = speed(total_seconds(pace_minutes, pace_seconds))
print('Your speed is ' + str(mph) + ' mph')

total = miles * total_seconds(pace_minutes, pace_seconds)
elapsed_minutes = total // 60
elapsed_seconds = total % 60

print('Yoir elapsed time is ' + str(elapsed_minutes) +
          ' mins ' + str(elapsed_seconds) + ' secs')
