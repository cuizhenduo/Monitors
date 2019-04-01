# -*- coding: utf-8 -*-
import psutil,time
from pprint import pprint
import datetime
#定义获取系统信息的类
class Monitor(object):
    #单位转换
    def bytes_to_gb(self,data,key=""):
        if key == "percent":
            return data
        else:
            return round(data / (1024 ** 3), 2)
    #获取cpu信息
    def cpu(self):
        #percpu：True获取每个cpu的使用率，False获取平均使用率
        #1.平均 2单独 3物理CPU核心数 4逻辑cpu核心数
        data = dict(
            percent_avg = psutil.cpu_percent(percpu=False,interval=0),
            percent_per = psutil.cpu_percent(percpu=True, interval=0),
            num_p = psutil.cpu_count(logical=False),
            num_l = psutil.cpu_count(logical=True)
        )
        return data
    # 获取内存信息
    def mem(self):
        info = psutil.virtual_memory()
        data = dict(
            total = self.bytes_to_gb(info.total),
            used=self.bytes_to_gb(info.used),
            free=self.bytes_to_gb(info.free),
            percent=info.percent
        )
        return data

    #获取交换分区信息
    def swap(self):
        info = psutil.swap_memory()
        data = dict(
            total=self.bytes_to_gb(info.total),
            used=self.bytes_to_gb(info.used),
            free=self.bytes_to_gb(info.free),
            percent=info.percent
        )
        return data

    #获取磁盘信息
    def disk(self):
        # 专门获取磁盘分区信息
        info = psutil.disk_partitions()
        # 列表推导式
        data = [
            dict(
                device=v.device,
                mountpoint=v.mountpoint,
                fstype=v.fstype,
                opts=v.opts,
                used={
                    k: self.bytes_to_gb(v, k)
                    for k, v in psutil.disk_usage(v.mountpoint)._asdict().items()
                }
            )
            for v in info
        ]
        return data

    #获取网络信息
    def net(self):
        #获取地址信息
        addrs = psutil .net_if_addrs()
        addrs_info = {
            k:[
                dict(
                    family = val.family.name,
                    address = val.address,
                    netmask = val.netmask,
                    broadcast = val.broadcast
                )
                for val in v if val.family.name == "AF_INET"
            ][0]
            for k,v in addrs.items()
        }
        #获取输入输出信息
        io = psutil.net_io_counters(pernic=True)
        data = [
            dict(
                name = k,
                bytes_sent = v.bytes_sent,
                bytes_recv=v.bytes_recv,
                packets_sent = v.packets_sent,
                packets_recv=v.packets_recv,
                **addrs_info[k]
            )
            for k,v in io.items()
        ]
        return data
    #转化时间戳
    def td(self,tm):
        dt = datetime.datetime.fromtimestamp(tm)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    #获取日期时间
    def dt(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #获取最近开机时间
    def lastest_start_time(self):
        return self.td(psutil.boot_time())
    #获取登录用户
    def logined_user(self):
        data = [
            dict(
                name = v.name,
                terminal = v.terminal,
                host = v.host,
                started = self.td(v.started),
                pid = v.pid
            )
            for v in psutil.users()
        ]
        return data

if __name__ == "__main__":
    m = Monitor()
    #print(m.mem())
    pprint(m.logined_user())
    """
    for v in range(1,11):
        print(m.cpu())
        time.sleep(1)
    """