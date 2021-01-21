# 输入时间
sample_start_time = input()
sample_time = eval(input())
# 开始时间小时与分钟分开
if len(sample_start_time) == 4:
    h = eval(sample_start_time[0:3])
elif len(sample_start_time) == 3:
    h = eval(sample_start_time[0:2])
m = eval(sample_start_time[-3:])