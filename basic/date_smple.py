from datetime import datetime, timedelta
from dateutil.parser import parse
from b2.util import date_util



d = "2021.01.03 21:23"
str = date_util.date_format(d)
print(str)
exit()

# str = convt_base.date_format("2021.01.03 21:23", "%Y/%m/%d")
# print(str)
# exit()

d = "2021.01.03 21:23:23"
dt = parse(d)
print(dt)
print(type(dt))

convt_date = dt.strftime("%Y-%m-%d")
print(convt_date)
exit()



# 오늘 날짜
today1 = datetime.today()
print(today1)
print( today1.strftime("%Y-%m-%d %H:%M:%S") )
# str_date = datetime.strptime("2021/02/03 10:12:23", "%Y-%m-%d %H:%M:%S").date()
str_date = datetime.strptime("2021-02-03", "%Y-%m-%d")
print(str_date)


print()
time1 = datetime.now()
print(time1) 


# 5일 후
print()
time = time1 + timedelta(days=5)
print(time)


# 5일 뒤 2시간 전
print()
time = time1 + timedelta(days=5, hours=-2)
print(time)