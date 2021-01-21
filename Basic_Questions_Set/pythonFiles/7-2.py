# 输入时间
s1, s2 = input().split(' ', 2)
sample_start_time = s1
sample_change_time = eval(s2)
# 开始时间小时与分钟分开
if len(sample_start_time) == 4:
    h = eval(sample_start_time[0:2])
elif len(sample_start_time) == 3:
    h = eval(sample_start_time[0:1])
m = eval(sample_start_time[-2:])
# 时间变化
m += sample_change_time
# 处理变化时间
sth = m // 60
m = m % 60
h += sth
# 格式调整
if m < 0:
    m += 60
    h -= 1
# 输出
print(h,end="")
if m < 10:
    print("0%d"%m)
else:
    print(m)