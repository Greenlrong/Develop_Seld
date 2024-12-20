# Aim: Time Caculator
# Time: 2024/12/18
# Written by: Long Yu
import Week_Caculator
import AM_PM_Caculator


def add_time(start, duration, week=''):
    # 条件
    # 1）12小时制的开始时间AM或PM结尾，表示小时数和分钟数的持续时间，可选一周的开始日期，不区分大小写，该函数应该将持续时间添加到开始时间并返回结果
    # 2）如果结果是第二天，则应在时间后显示(第二天)。如果结果晚于一天以上，则应在时间后显示(n天后)。n是天数
    # 3）如果为函数提供了可选的开始日期参数，则输出应显示结果的星期几。输出中的星期几应出现在时间之后和天数之前。
    # start: 开始时间；duration:持续时间；
    # 输入情况：1）包含小时和分钟；2）包含小时、分钟和星期
    # 分析start + duration的结果是什么，
    # 针对第一种情况：1）在同一天内；2）大于1天；
    # 针对第二种情况：1）在同一天内，小时分钟改变，星期不变；2）大于1天小于六天，根据计算时间分钟和星期都改变；3）以七天为周期，计算更大的时间尺度。

    # 代码逻辑：输入，输入分为两种情况，考虑使用if-else，进行两种选择。if是时间分钟，这个内容下面有两种，同样使用if-else结构，
    # if是同一天内，else是大于1天的情况；第一个if-else结构的else是输入带有星期的情况，这里有三种情况，那还可以直接使用if-else吗？

    # 定义初始量
    # global new_time
    global new_time
    global week1
    import re

    # 提取start和duration中的时间部分
    time1 = re.findall(r'\d+', start)
    time2 = re.findall(r'\d+', duration)

    # 提取am 或 pm
    # start_str = start[0]
    am_pm = start[-2:]
    # print('读取输入的上午或下午：', am_pm)
    # 将提取的am、pm分别转为0、12
    Am_Pm = AM_PM_Caculator.de_am_pm_caculator(am_pm)
    # print('输入的上午或者下午转为数字用于计算：', Am_Pm)

    # 提取start时间部分得到['12', '09'], 目前的类型还是<class 'list'>，list里面的'12' '09'是str类型
    # print('\n初始时间及其类型:', time1, type(time1))
    # duration同理
    # print('持续时间及其类型:', time2, type(time2))

    # 验证list中的str
    # A = time[0] + time[1]
    # print(A)   # 这里time是list类型，但是里面的'12' '09'都不是list类型，只是str类型，可以用 + 符号，效果是直接拼凑在一起。

    # 将提取的数字类型转为整型
    hours1 = int(time1[0])
    minutes1 = int(time1[1])
    hours2 = int(time2[0])
    minutes2 = int(time2[1])

    # 将am 或pm 转为数字之后加到hours1上用于后续的计算
    hours1 += Am_Pm

    # 打印转换后的数据类型，都转为了<class, int>
    # print('初始时间转换为int类型', hours1, type(hours1), '\n', minutes1, type(minutes1))
    # print('持续时间转换为int类型', hours2, type(hours2), '\n', minutes2, type(minutes2))

    # 问题1： list类型能够直接用于运算吗？list可以，str不能，str只是拼凑
    # 验证start字符串的值可以通过 + 来拼凑；
    # B = '12' + ':' + '09' + ',' + ' ' + 'AM'
    # print(B, type(B))    # 经验证，确实可行

    # 按照60分钟进1小时的计算方法，应该先计算分钟，再计算小时
    # 先算是否大于一天，即24；再计算上午还是下午的问题
    # if hours1 + hours2 >= 24:
    #     # 取整的目的是，得到的结果就是n+1天
    #     hours3_day = (hours1 + hours2) // 24
    #     hours3_am_pm = (hours1 + hours2) % 24
    #     print('最终时间', hours3_day, hours3_am_pm)
    #     # minutes相加肯定是小于120，因为数字是按照正常的12小时制的时间输入的
    # 注意计算顺序：判断week是否正常输入 --> minutes --> hours --> week---------------------

    # week没有输入的情况
    if week == '':
        if minutes1 + minutes2 >= 120:
            print('Your time is wrong, Please input right time type.')
        elif 120 > minutes1 + minutes2 >= 60:
            # minutes_plus = (minutes1 + minutes2) // 60    # 这里不需要，直接将小时 +1 即可。
            minutes_end = (minutes1 + minutes2) % 60
            # 既然minutes已经大于60了，那么小时直接 +1 即可，小时不可能出现+2的情况，时间输入都是正确的
            # print('最终的minutes：', minutes_end)
            if hours1 + hours2 + 1 >= 24:
                # 取整的目的是，得到的结果就是n+1天
                day_end = (hours1 + hours2 + 1) // 24  # 等于1，即明天next day。
                hours3_am_pm = (hours1 + hours2 + 1) % 24
                AP = AM_PM_Caculator.am_pm_caculator(hours3_am_pm)
                # print(f'天数： ({day_end} later day), 用于判断上午或下午的当日小时: {hours3_am_pm}')
                # 打印时，当天无需打印，过了一天打印next day， 大于1天，打印 n later days
                if day_end < 1:
                    # 也就是当天
                    # 上、下午的判断
                    if hours3_am_pm > 12:
                        hours_end = hours3_am_pm % 1
                        # print(f'Return：{hours_end}:{minutes_end} PM ')
                        new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP
                        print(f'Return: {new_time}')
                        # return new_time
                    # elif整句是不是直接用else代替就行了呢？因为就只有两种情况了。
                    # elif 12 >= hours3_am_pm:
                    else:
                        hours_end = hours3_am_pm
                        # print(f'Return：{hours_end}:{minutes_end} AM')
                        new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP
                        print(f'Return: {new_time}')
                        # return new_time
                elif day_end == 1:
                    # 也就是Next day
                    # week1 = Week_Caculator.week_caculator(week)
                    # 上、下午的判断
                    if hours3_am_pm > 12:
                        hours_end = hours3_am_pm % 1
                        # print(f'Return：{hours_end}:{minutes_end} PM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ' ' + '(next day)')
                        print(f'Return: {new_time}')
                        # return new_time
                    # elif整句是不是直接用else代替就行了呢？因为就只有两种情况了。
                    # elif 12 >= hours3_am_pm:
                    else:
                        hours_end = hours3_am_pm
                        # print(f'Return：{hours_end}:{minutes_end} AM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ' ' + '(next day)')
                        print(f'Return: {new_time}')
                        # return new_time
                elif day_end > 1:
                    # 上、下午的判断
                    # AP = AM_PM_Caculator.am_pm_caculator(hours3_am_pm)

                    if hours3_am_pm > 12:
                        hours_end = hours3_am_pm % 12
                        # print(f'Return：{hours_end}:{minutes_end} PM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ', ' + str(day_end)
                                    + ' days later')
                        print(f'Return: {new_time}')
                        # return new_time
                    # elif整句是不是直接用else代替就行了呢？因为就只有两种情况了。
                    # elif 12 >= hours3_am_pm:
                    else:
                        hours_end = hours3_am_pm
                        # print(f'Return：{hours_end}:{minutes_end} AM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ', ' + str(day_end)
                                    + ' days later')
                        print(f'Return: {new_time}')
                        # return new_time
            else:
                day_end = (hours1 + hours2 + 1) // 12  # 等于1，则是下午；为0，则是上午
                hours3_am_pm = (hours1 + hours2 + 1) % 12
                AP = AM_PM_Caculator.am_pm_caculator(hours1 + hours2 + 1)
                # print(f'天数： ({day_end} later day), 用于判断上午或下午的当日小时: {hours3_am_pm}， 上午还是下午{AP}')
                # 判断上下午
                if day_end == 0:
                    # 上午
                    hours_end = hours3_am_pm
                    # print(f'Return： {hours_end}：{minutes_end} AM')
                    new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP
                    print(f'Return: {new_time}')
                    # return new_time
                else:
                    # 下午
                    hours_end = hours3_am_pm
                    # print(f'Return： {hours_end}：{minutes_end} PM')
                    new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP
                    print(f'Return: {new_time}')
                    # return new_time

        elif minutes1 + minutes2 < 60:
            minutes_end = minutes1 + minutes2
            if hours1 + hours2 >= 24:

                # 取整的目的是，得到的结果就是n+1天
                day_end = (hours1 + hours2) // 24  # 等于1，即明天next day。
                hours3_am_pm = (hours1 + hours2) % 24
                AP = AM_PM_Caculator.am_pm_caculator(hours3_am_pm)
                # print(f'天数： {day_end} later day, 用于判断上午或下午的当日小时: {hours3_am_pm}')
                # 打印时，当天无需打印，过了一天打印next day， 大于1天，打印 n later days
                if day_end < 1:
                    # 上、下午的判断直接使用AP即可（通过调用函数的方式）
                    if hours3_am_pm > 12:
                        hours_end = hours3_am_pm % 12
                        # print(f'Return：{hours_end}:{minutes_end} PM ')
                        new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP
                        print(f'Return: {new_time}')
                        # return new_time

                    # elif整句是不是直接用else代替就行了呢？因为就只有两种情况了。
                    # elif 12 >= hours3_am_pm:
                    else:
                        hours_end = hours3_am_pm
                        # print(f'Return：{hours_end}:{minutes_end} AM')
                        new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP
                        # print(f'Return: {new_time}')
                        # return new_time

                elif day_end == 1:
                    # 上、下午的判断
                    if hours3_am_pm > 12:
                        hours_end = hours3_am_pm % 1
                        # print(f'Return：{hours_end}:{minutes_end} PM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ' ' + '(next day)')
                        print(f'Return: {new_time}')
                        # return new_time

                    # elif整句是不是直接用else代替就行了呢？因为就只有两种情况了。
                    # elif 12 >= hours3_am_pm:
                    else:
                        hours_end = hours3_am_pm
                        # print(f'Return：{hours_end}:{minutes_end} AM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ' ' + '(next day)')
                        print(f'Return: {new_time}')
                        # return new_time
                elif day_end > 1:
                    # 上、下午的判断
                    if hours3_am_pm > 12:
                        hours_end = hours3_am_pm % 1
                        # print(f'Return：{hours_end}:{minutes_end} PM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ', ' + str(day_end)
                                    + ' days later')
                        print(f'Return: {new_time}')
                        # return new_time
                    # elif整句是不是直接用else代替就行了呢？因为就只有两种情况了。
                    # elif 12 >= hours3_am_pm:
                    else:
                        hours_end = hours3_am_pm
                        # print(f'Return：{hours_end}:{minutes_end} AM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ', ' + str(day_end)
                                    + ' days later')
                        print(f'Return: {new_time}')
                        # return new_time
            else:
                # 当日
                day_end = (hours1 + hours2) // 12  # 等于1，则是下午；为0，则是上午
                hours3_am_pm = (hours1 + hours2) % 12
                AP = AM_PM_Caculator.am_pm_caculator(hours1 + hours2)
                # print(f'天数： ({day_end} later day), 用于判断上午或下午的当日小时: {hours3_am_pm}')
                # 判断上下午
                if day_end == 0:
                    # 上午
                    hours_end = hours3_am_pm
                    # print(f'Return： {hours_end}：{minutes_end} AM')
                    new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP
                    print(f'Return: {new_time}')
                    # return new_time
                else:
                    # 下午
                    hours_end = hours3_am_pm
                    # print(f'Return： {hours_end}：{minutes_end} PM')
                    new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP
                    print(f'Return: {new_time}')
                    # return new_time
    # week有输入的情况
    else:
        # week1 = 0
        week1 = Week_Caculator.week_caculator(week)  # 得到的是数字，即星期对应的数字
        # 在后续中要重复使用的话，使用global变量进行全局定义才行，否则后续不能重复使用变量的数据类型和变量本身
        # print(week1, type(week1))

        if minutes1 + minutes2 >= 120:
            print('Your time is wrong, Please input right time type.')
        elif 120 > minutes1 + minutes2 >= 60:
            # minutes_plus = (minutes1 + minutes2) // 60    # 这里不需要，直接将小时 +1 即可。
            minutes_end = (minutes1 + minutes2) % 60
            # 既然minutes已经大于60了，那么小时直接 +1 即可，小时不可能出现+2的情况，时间输入都是正确的
            # print('最终的minutes：', minutes_end)
            if hours1 + hours2 + 1 >= 24:
                # 取整的目的是，得到的结果就是n+1天
                day_end = (hours1 + hours2 + 1) // 24   # 等于1，即明天next day。
                hours3_am_pm = (hours1 + hours2 + 1) % 24
                AP = AM_PM_Caculator.am_pm_caculator(hours3_am_pm)
                # print(f'天数： ({day_end} later day), 用于判断上午或下午的当日小时: {hours3_am_pm}')
                # 打印时，当天无需打印，过了一天打印next day， 大于1天，打印 n later days
                if day_end < 1:
                    # 也就是当天
                    # 上、下午的判断
                    if hours3_am_pm > 12:
                        hours_end = hours3_am_pm % 1
                        # print(f'Return：{hours_end}:{minutes_end} PM ')
                        new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ',' + ' ' + week
                        print(f'Return: {new_time}')
                        # return new_time
                    # elif整句是不是直接用else代替就行了呢？因为就只有两种情况了。
                    # elif 12 >= hours3_am_pm:
                    else:
                        hours_end = hours3_am_pm
                        # print(f'Return：{hours_end}:{minutes_end} AM')
                        new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ',' + ' ' + week
                        print(f'Return: {new_time}')
                        # return new_time
                elif day_end == 1:
                    # 也就是Next day
                    # week1 = Week_Caculator.week_caculator(week)
                    week1 += 1  # 星期数加1
                    # 将计算后的数字转化为星期作为输出
                    numbers = Week_Caculator.de_week_caculator(week1)
                    # 上、下午的判断
                    if hours3_am_pm > 12:
                        hours_end = hours3_am_pm % 1
                        # print(f'Return：{hours_end}:{minutes_end} PM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ' ' + '(next day)'
                                    + ',' + ' ' + numbers)
                        print(f'Return: {new_time}')
                        # return new_time
                    # elif整句是不是直接用else代替就行了呢？因为就只有两种情况了。
                    # elif 12 >= hours3_am_pm:
                    else:
                        hours_end = hours3_am_pm
                        # print(f'Return：{hours_end}:{minutes_end} AM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ' ' + '(next day)'
                                    + ',' + ' ' + numbers)
                        print(f'Return: {new_time}')
                        # return new_time
                elif day_end > 1:
                    # week1 = Week_Caculator.week_caculator(week)
                    week1 = week1 + day_end   # 星期的计算
                    numbers = Week_Caculator.de_week_caculator(week1)  # 数字计算后，转化为星期
                    # 上、下午的判断
                    # AP = AM_PM_Caculator.am_pm_caculator(hours3_am_pm)

                    if hours3_am_pm > 12:
                        hours_end = hours3_am_pm % 12
                        # print(f'Return：{hours_end}:{minutes_end} PM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ', ' + str(day_end)
                                    + ' days later' + ',' + ' ' + numbers)
                        print(f'Return: {new_time}')
                        # return new_time
                    # elif整句是不是直接用else代替就行了呢？因为就只有两种情况了。
                    # elif 12 >= hours3_am_pm:
                    else:
                        hours_end = hours3_am_pm
                        # print(f'Return：{hours_end}:{minutes_end} AM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ', ' + str(day_end)
                                    + ' days later' + ',' + ' ' + numbers)
                        print(f'Return: {new_time}')
                        # return new_time
            else:
                day_end = (hours1 + hours2 + 1) // 12   # 等于1，则是下午；为0，则是上午
                hours3_am_pm = (hours1 + hours2 + 1) % 12
                AP = AM_PM_Caculator.am_pm_caculator(hours1 + hours2 + 1)
                # print(f'天数： ({day_end} later day), 用于判断上午或下午的当日小时: {hours3_am_pm}， 上午还是下午{AP}')
                # 判断上下午
                if day_end == 0:
                    # 上午
                    hours_end = hours3_am_pm
                    # print(f'Return： {hours_end}：{minutes_end} AM')
                    new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ',' + ' ' + week
                    print(f'Return: {new_time}')
                    # return new_time
                else:
                    # 下午
                    hours_end = hours3_am_pm
                    # print(f'Return： {hours_end}：{minutes_end} PM')
                    new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ',' + ' ' + week
                    print(f'Return: {new_time}')
                    # return new_time

        elif minutes1 + minutes2 < 60:
            minutes_end = minutes1 + minutes2
            if hours1 + hours2 >= 24:

                # 取整的目的是，得到的结果就是n+1天
                day_end = (hours1 + hours2) // 24   # 等于1，即明天next day。
                hours3_am_pm = (hours1 + hours2) % 24
                AP = AM_PM_Caculator.am_pm_caculator(hours3_am_pm)
                # print(f'天数： {day_end} later day, 用于判断上午或下午的当日小时: {hours3_am_pm}')
                # 打印时，当天无需打印，过了一天打印next day， 大于1天，打印 n later days
                if day_end < 1:
                    # 上、下午的判断直接使用AP即可（通过调用函数的方式）
                    if hours3_am_pm > 12:
                        hours_end = hours3_am_pm % 12
                        # print(f'Return：{hours_end}:{minutes_end} PM ')
                        new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ',' + ' ' + week
                        print(f'Return: {new_time}')
                        # return new_time

                    # elif整句是不是直接用else代替就行了呢？因为就只有两种情况了。
                    # elif 12 >= hours3_am_pm:
                    else:
                        hours_end = hours3_am_pm
                        # print(f'Return：{hours_end}:{minutes_end} AM')
                        new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ',' + ' ' + week
                        print(f'Return: {new_time}')
                        # return new_time

                elif day_end == 1:
                    # week1 = Week_Caculator.week_caculator(week)
                    week1 = week1 + day_end
                    numbers = Week_Caculator.de_week_caculator(week1)
                    # 上、下午的判断
                    if hours3_am_pm > 12:
                        hours_end = hours3_am_pm % 1
                        # print(f'Return：{hours_end}:{minutes_end} PM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ' ' + '(next day)'
                                    + ',' + ' ' + numbers)
                        print(f'Return: {new_time}')
                        # return new_time

                    # elif整句是不是直接用else代替就行了呢？因为就只有两种情况了。
                    # elif 12 >= hours3_am_pm:
                    else:
                        hours_end = hours3_am_pm
                        # print(f'Return：{hours_end}:{minutes_end} AM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ' ' + '(next day)'
                                    + ',' + ' ' + numbers)
                        print(f'Return: {new_time}')
                        # return new_time
                elif day_end > 1:
                    # week1 = Week_Caculator.week_caculator(week)
                    week1 += day_end
                    numbers = Week_Caculator.de_week_caculator(week1)
                    # 上、下午的判断
                    if hours3_am_pm > 12:
                        hours_end = hours3_am_pm % 1
                        # print(f'Return：{hours_end}:{minutes_end} PM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ', ' + str(day_end)
                                    + ' days later' + ',' + ' ' + numbers)
                        print(f'Return: {new_time}')
                        # return new_time
                    # elif整句是不是直接用else代替就行了呢？因为就只有两种情况了。
                    # elif 12 >= hours3_am_pm:
                    else:
                        hours_end = hours3_am_pm
                        # print(f'Return：{hours_end}:{minutes_end} AM ({day_end} next day)')
                        new_time = (str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ', ' + str(day_end)
                                    + ' days later' + ',' + ' ' + numbers)
                        print(f'Return: {new_time}')
                        # return new_time
            else:
                # 当日
                day_end = (hours1 + hours2) // 12   # 等于1，则是下午；为0，则是上午
                hours3_am_pm = (hours1 + hours2) % 12
                AP = AM_PM_Caculator.am_pm_caculator(hours1 + hours2)
                # print(f'天数： ({day_end} later day), 用于判断上午或下午的当日小时: {hours3_am_pm}')
                # 判断上下午
                if day_end == 0:
                    # 上午
                    hours_end = hours3_am_pm
                    # print(f'Return： {hours_end}：{minutes_end} AM')
                    new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ',' + ' ' + week
                    print(f'Return: {new_time}')
                    # return new_time
                else:
                    # 下午
                    hours_end = hours3_am_pm
                    # print(f'Return： {hours_end}：{minutes_end} PM')
                    new_time = str(hours_end) + ':' + str(minutes_end) + ' ' + AP + ',' + ' ' + week
                    print(f'Return: {new_time}')
                    # return new_time
    return new_time    # return直接得到的结果与print得到的结果应该是需要区分的
    # 仅return可有可无


# 问题2： 怎么正确使用上述函数。 -----完成
# 思路2： 注意每个def 最终return的参量，不恰当的return返回的结果会影响后续的运算。
#        出现的问题是在week caculator哈函数后没有添加正确的return，导致得到的结果类型是None。

# 问题3： AM PM没有加入到里面，需要检测输入时存在的AM和PM，因为使用的是12小时制的时间。-----完成
# 思路3： 读取输入的AM和PM --> AM和PM出现的条件，只有判断上下午时使用 --> 最后的调用

# 问题4： 怎么全局返回的问题。-----完成
# 思路4： 使用"global 变量" 的方式将变量设为全局变量。

# 问题5： 怎么在函数定义时添加“可选参数”呢？先添加星期。----完成
# 思路5： 自定义一个星期循环的函数，可用于这个计算时间函数。

# 问题6： 根据不同的输入应该导向不同运算结果-----完成
# 思路6： 输入存在不同的情况，如start + duration； 或 start + duration + week

# 问题7： 怎么将星期作为一个可选参量输出呢？现在会返回两个Return，其中一个在没有星期输入时，
#        没有星期输出；但是最后的输出却有。   -----完成
# 思路7： 只要输入的week是空的，那么后续关于week的计算都不使用。直接在最初的判断处就先判断了week
#        是否有输入再做后续的判断。


# 对于问题2的使用函数的回答，输入参数之后需要全部运行才能正确返回
# add_time('2:2', '3:3', 'Monday')

