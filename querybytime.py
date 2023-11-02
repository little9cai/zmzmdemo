import calendar
import pywencai


def query_by_time(a, b=0, c=0):  # 返回两个list，一个是年月日，另一个是星期
    date_day = []
    week_day = []
    if b!=0:  # 查询的是某个月的数据
        if c == 0:
            # print(str(a) + '-' + str(b) + '数据如下')
            if b in (1, 3, 5, 7, 8, 10, 12):
                while c < 31:
                    c += 1
                    date_str = str(a) + '-' + str(b) + '-' + str(c)
                    date_obj = calendar.datetime.datetime.strptime(date_str, '%Y-%m-%d')
                    weekdays = calendar.weekday(date_obj.year, date_obj.month, date_obj.day) + 1
                    if weekdays > 5:
                        continue
                    date_day.append(date_str)
                    week_day.append(weekdays)
            elif b in (4, 6, 9, 11):
                while c < 30:
                    c += 1
                    date_str = str(a) + '-' + str(b) + '-' + str(c)
                    date_obj = calendar.datetime.datetime.strptime(date_str, '%Y-%m-%d')
                    weekdays = calendar.weekday(date_obj.year, date_obj.month, date_obj.day) + 1
                    if weekdays > 5:
                        continue
                    date_day.append(date_str)
                    week_day.append(weekdays)
            elif b == 2:
                if a % 4 != 0:
                    d = 28
                else:
                    d = 29
                while c < d:
                    c += 1
                    date_str = str(a) + '-' + str(b) + '-' + str(c)
                    date_obj = calendar.datetime.datetime.strptime(date_str, '%Y-%m-%d')
                    weekdays = calendar.weekday(date_obj.year, date_obj.month, date_obj.day) + 1
                    if weekdays > 5:
                        continue
                    date_day.append(date_str)
                    week_day.append(weekdays)
        elif c !=0:  #查询的是某天的数据
                date_str = str(a) + '-' + str(b) + '-' + str(c)
                date_obj = calendar.datetime.datetime.strptime(date_str, '%Y-%m-%d')
                weekdays = calendar.weekday(date_obj.year, date_obj.month, date_obj.day) + 1
                if weekdays > 5:
                    raise IndexError('查询日期为周末')
                elif weekdays<6:
                    date_day.append(date_str)
                    week_day.append(weekdays)
    elif b == 0:  # 查询的是整年的数据
        while b < 12:
            b += 1
            if c == 0:
                # print(str(a) + '-' + str(b) + '数据如下')
                if b in (1, 3, 5, 7, 8, 10, 12):
                    while c < 31:
                        c += 1
                        date_str = str(a) + '-' + str(b) + '-' + str(c)
                        date_obj = calendar.datetime.datetime.strptime(date_str, '%Y-%m-%d')
                        weekdays = calendar.weekday(date_obj.year, date_obj.month, date_obj.day) + 1
                        if weekdays > 5:
                            continue
                        date_day.append(date_str)
                        week_day.append(weekdays)
                elif b in (4, 6, 9, 11):
                    while c < 30:
                        c += 1
                        date_str = str(a) + '-' + str(b) + '-' + str(c)
                        date_obj = calendar.datetime.datetime.strptime(date_str, '%Y-%m-%d')
                        weekdays = calendar.weekday(date_obj.year, date_obj.month, date_obj.day) + 1
                        if weekdays > 5:
                            continue
                        date_day.append(date_str)
                        week_day.append(weekdays)
                elif b == 2:
                    if a % 4 != 0:
                        d = 28
                    else:
                        d = 29
                    while c < d:
                        c += 1
                        date_str = str(a) + '-' + str(b) + '-' + str(c)
                        date_obj = calendar.datetime.datetime.strptime(date_str, '%Y-%m-%d')
                        weekdays = calendar.weekday(date_obj.year, date_obj.month, date_obj.day) + 1
                        if weekdays > 5:
                            continue
                        date_day.append(date_str)
                        week_day.append(weekdays)
            c = 0
    return date_day, week_day
