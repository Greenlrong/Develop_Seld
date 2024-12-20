# Aim: Week Caculator
# Time: 2024/12/18
# Written by: Long Yu


# 框架：将输入的星期根据duration变为对应的星期，如果没有输入则应该没有return
# 星期转化为数字，用于计算
def week_caculator(week):
    global week1
    if week == 'Monday':
        week1 = int(1)
        # print(week1, type(week1))
    elif week == 'Tuesday':
        week1 = int(2)
        # print(week1, type(week1))
    elif week == 'Wednesday':
        week1 = int(3)
        # print(week1, type(week1))
    elif week == 'Thursday':
        week1 = int(4)
        # print(week1, type(week1))
    elif week == 'Friday':
        week1 = int(5)
        # print(week1, type(week1))
    elif week == 'Saturday':
        week1 = int(6)
        # print(week1, type(week1))
    elif week == 'Sunday':
        week1 = int(7)
        # print(week1, type(week1))
    elif week == '':
        week1 = None
    return week1
    # 注意： return加上会更好，否则在条用函数时，会出现函数得到的结果的类型时None。
    # 没有return返回的结果是： 1 <class 'int'>,会将整个结果都传递给后续的过程
    # 使用return week1，则只返回week1所包含的量，能够正常用于后续的运算

# 直接使用int()函数将值赋值变量，避免了输出是NoneType的情况
# week_caculator('Saturday')


# 经过计算之后，将得到数字转化为星期，用于return结果
def de_week_caculator(numbers):
    numbers = int(numbers)
    global week
    numbers = numbers % 7
    if numbers == 0:
        week = 'Sunday'
        # print(week)
    elif numbers == 1:
        week = 'Monday'
        # print(week)
    elif numbers == 2:
        week = 'Tuesday'
        # print(week)
    elif numbers == 3:
        week = 'Wednesday'
        # print(week)
    elif numbers == 4:
        week = 'Thursday'
        # print(week)
    elif numbers == 5:
        week = 'Friday'
        # print(week)
    elif numbers == 6:
        week = 'Saturday'
        # print(week)
    return week


# 直接call
# week_caculator('Monday')   # 返回的是int类型，但是为什么返回的值
# de_week_caculator(16)
