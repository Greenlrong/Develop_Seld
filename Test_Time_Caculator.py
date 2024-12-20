# Aim: Test Time Caculator
# Time: 2024/12/18
# Written by: Long Yu

# Time_Caculator的初步测试，完成了start和duration的小时、分钟的输入以及运算
import Time_Caculator


Time_Caculator.add_time('11:22 PM', '10:22', 'Sunday')
Time_Caculator.add_time('3:30 PM', '2:12')
Time_Caculator.add_time('11:55 AM', '3:12')
Time_Caculator.add_time('11:59 PM', '24:05')
Time_Caculator.add_time('8:16 PM', '466:02')
Time_Caculator.add_time('3:30 PM', '2:12', 'Monday')
Time_Caculator.add_time('2:59 AM', '24:00', 'Sunday')
Time_Caculator.add_time('11:59 PM', '24:05', 'Wednesday')
Time_Caculator.add_time('8:16 PM', '466:02', 'Tuesday')

# , 'Saturday'
# 由于是12小时制的时间，所有输入时间中，正确的小时的范围是[0, 12]，分钟[0, 59]
# 后面出现PM时，小时的范围是[1, 11]，在条件判断时，PM需要加12，最终结果才能是正确的。

# 最终的目标：怎么把这个集成一个界面呢？
