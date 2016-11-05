#coding:utf-8
import psutil
import time
import socket
import os,sys
print "===========  系统当前用户:%s        ==============="%psutil.users()[0].name
print "===========  系统当前时间:%s  ==============="%time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
print 
def mem():
    mem=psutil.virtual_memory()
    mem_list=[mem.total,mem.used,mem.free,mem.percent]
    return(mem_list)
   
def disk():
    disk_list=[psutil.disk_usage('/').total,psutil.disk_usage('/').used,psutil.disk_usage('/').free,psutil.disk_usage('/').percent]
    return disk_list
def net():
    net_list=[psutil.net_io_counters().bytes_sent, psutil.net_io_counters().bytes_recv, psutil.net_io_counters().packets_sent, psutil.net_io_counters().packets_recv]
    return net_list
def cpu():
    cpu_list=[psutil.cpu_times().user,psutil.cpu_times().system,psutil.cpu_times().iowait,psutil.cpu_times().idle,psutil.cpu_percent()]
    return cpu_list
cpulist=cpu()
netlist=net()
memlist=mem()
disklist=disk()

myfile = open(r'1.txt','w+')
myfile.write("系统当前用户:%s\n"%psutil.users()[0].name)
myfile.write("系统当前时间:%s\n"%time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
myfile.write("---------------------\n")
myfile.write("执行用户进程的时间百分比%s%%\n"%(cpulist[0]//1))
myfile.write("执行内核进程和中断的时间百分比%s%%\n"%(cpulist[1]//1))
myfile.write("空闲时间比%s%%\n"%(cpulist[3]//1/100))
myfile.write("处于idle状态的时间百分比%s%%\n"%(cpulist[2]//1))
myfile.write("cpu使用率%s%%\n"%(cpulist[4]))
myfile.write("---------------------\n")
myfile.write("网络发送字节数:%sM\n"%(netlist[0]//1000000))
myfile.write("网络接收字节数:%sM\n"%(netlist[1]//1000000))
myfile.write("网络发送数据包:%sM\n"%(netlist[2]//1000000))
myfile.write("网络接收数据包:%sM\n"%(netlist[3]//1000000))
myfile.write("---------------------\n")
myfile.write("内存总数 :%sM\n"%(memlist[0]//1000000))
myfile.write("内存使用 :%sM\n"%(memlist[1]//1000000))
myfile.write("内存空闲 :%sM\n"%(memlist[2]//1000000))
myfile.write("内存使用率:%s\n"%(memlist[3]))
myfile.write("---------------------\n")
myfile.write("硬盘总数 :%sM\n"%(disklist[0]//1000000))
myfile.write("硬盘使用:%sM\n"%(disklist[1]//1000000))
myfile.write("硬盘空闲:%sM\n"%(disklist[2]//1000000))
myfile.write("硬盘使用率:%s\n"%(disklist[3]))
myfile.close()
f = open(r'1.txt','r')
result= f.read()

def reader(path):
        con=os.popen('cat %s'%path)
        content=con.read()
        con.close()
        return content

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('192.168.0.7',8001))
while True:
    canshu=sock.recv(2048)
    print(canshu)
    sock.send(result)   
    f.close() 
    print("success")
sock.close()
