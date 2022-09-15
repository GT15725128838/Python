"""
    ⽤Python来编写脚本简化⽇常的运维⼯作是Python的⼀个重要⽤途。在Linux下，有许多系统命令 可以让我们时刻监控系统运⾏的状态，
如 ps ， top ， free 等等。要获取这些系统信息，Python 可以通过 subprocess 模块调⽤并获取结果。但这样做显得很麻烦，
尤其是要写很多解析代码。
    在Python中获取系统信息的另⼀个好办法是使⽤ psutil 这个第三⽅模块。 psutil ,是 python system and process utilities 的缩写，
意思python的系统监控及进程的 管理的⼯具，是⼀个功能很强⼤的跨平台的系统管理库。可以实现命令⾏中类似ps、top、lsof、 netstat、ifconfig、
who、df、kill、free、nice、ionice、iostat、iotop等等命令的功能，并且以python内 置的数据结构形式返回，
官⽅⽂档（https://pythonhosted.org/psutil/） ⽬前psutil⽀持的系统有linux window os X 和freeBSD等
"""
import psutil
import datetime

# 1. 定义变量保存cpu信息
cpu_info = psutil.cpu_percent(interval=0.5)

# 2. 定义变量保存内存使用情况
memory_info = psutil.virtual_memory()

# 3. 定义变量保存磁盘使用情况
disk_info = psutil.disk_usage("/")

# 4. 获取网络收发量
net_info = psutil.net_io_counters()

# 5. 获取系统时间
current_time = datetime.datetime.now().strftime("%Y-%m-%d %T")

# 6、开始记录信息到⽇志⽂件中
# 6.1 拼接记录信息的字符串
log_str = "|-------------------|------------|-------------|-------------|----------------------------|\n"
log_str += "| 监控时间           | CPU使⽤率   | 内存使⽤率    | 硬盘使⽤率    | ⽹络收发量------------------|\n"
log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
log_str += "|%s| %s%% | %s%% | %s%% | 收:%s/发:%s |\n" % (current_time, cpu_info, memory_info.percent, disk_info.percent, net_info.bytes_recv, net_info.bytes_sent)
log_str += "|-------------------|------------|-------------|-------------|----------------------------|\n"
print(log_str)

