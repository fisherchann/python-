# 在这里写计算过程,然后将答案赋值给 a1
import math
#import datetime as d
from datetime import datetime as d


def time_delta_datetime(year1, month1, day1, year2, month2, day2):
    time1 = d(year=2021, month=month1, day=day1)
    time2 = d(year=2021, month=month2, day=day2)
    return (time2-time1).days


delta_D = time_delta_datetime(
    year1=2021,
    month1=9,
    day1=18,
    year2=2021,
    month2=9,
    day2=24)
print(delta_D*24)

delta_D = len(list_beijing)
print(delta_D)


def ludian(temp, sh):
    gama = 17.27*temp/(237.7+temp) + math.log(sh/100)
    return 237.7*gama/(17.27-gama)


list_ludian = [0 for x in range(0, delta_D)]
for i in range(0, delta_D):
    list_ludian[i] = ludian(temp=list_beijing[i][1], sh=list_beijing[i][2])
a1 = int(min(list_ludian))  # 等号后面写上计算出来的答案
print(a1)
