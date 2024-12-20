# Aim: AM or PM Caculator
# Time: 2024/12/19
# Written by: Long Yu


# 将am 或 pm转化为数字，用于运算
def de_am_pm_caculator(am_pm):
    global m
    if am_pm == 'AM' or am_pm == 'am' or am_pm == 'Am' or am_pm == 'aM':
        # 四种情况是为了解决不区分大小写的问题 ，但应该怎么才能简化这个代码呢？
        m = 0
        # print(m)
    elif am_pm == 'PM' or am_pm == 'pm':
        m = 12
        # print(m)
    return m


de_am_pm_caculator('AM')

# 先让代码正常运行，然后在考虑优化的问题。


# 将计算后的小时转为am 或 pm
def am_pm_caculator(number):
    global n
    if 0 <= number <= 12:
        n = 'AM'
        # print(n)
    else:
        n = 'PM'
        # print(n)
    return n


# am_pm_caculator('')

