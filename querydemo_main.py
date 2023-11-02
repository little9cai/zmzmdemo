import pywencai
import querybytime
import time
import calendar

# 可用于拓展-输入指定日期，YYYY/MM/DD;日期为0表示查询当月数据，月份日期均为零表示查询当年数据。
date_for_query, weekdays_for_query = querybytime.query_by_time(2023, 0, )
y = 0
for i in date_for_query:
    res1 = pywencai.get(query=i + '二连板，不含ST')
    if res1 is None:
        print(i + ',星期' + str(weekdays_for_query[y]) + ',二连板数目为0')
    else:
        print(i + ',星期' + str(weekdays_for_query[y]) + ',二连板数目为' + str(int(res1.size / 8)))
    y += 1
