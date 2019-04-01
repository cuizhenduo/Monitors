# -*- coding:utf-8 -*-
import datetime
from app.views.views_common import Commonhandler
from sqlalchemy import and_,func
from app.tools.orm import ORM
from app.models.models import Cpu,Mem,Swap
from app.tools.chart import chart
import tornado.gen
import tornado.concurrent
class LogHandler(Commonhandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        # 用id标识参数
        id = 2
        data = dict()
        c = chart()
        # id为1表示1小时内
        if int(id) == 1:
            attr_swap, attr_mem, attr_cpu, vals_swap, vals_mem, vals_cpu = self.data_by_hour()
            # 内存折线图
            if attr_mem and vals_mem:
                data["mem_line"] = c.line_html(
                    "内存使用率日志[1小时内]",
                    attr_mem,
                    vals_mem,
                    "green"
                )
            else:
                data["mem_line"] = "<div class='alert alert-danger'>没有内存数据</div>"
            # 交换分区折线图
            if attr_swap and vals_swap:
                data["swap_line"] = c.line_html(
                    "交换分区使用率日志[1小时内]",
                    attr_swap,
                    vals_swap,
                    "red"
                )
            else:
                data["swap_line"] = "<div class='alert alert-danger'>没有交换分区数据</div>"
            # CPU折线图
            if attr_cpu and vals_cpu:
                data["cpu_line"] = c.line_html(
                    "交换分区使用率日志[1小时内]",
                    attr_cpu,
                    vals_cpu,
                    "blue"
                )
            else:
                data["cpu_line"] = "<div class='alert alert-danger'>没有cpu数据</div>"
        # id为2表示1天内
        if int(id) == 2:
            attr_mem, vals_mem_max, vals_mem_min, vals_mem_avg, attr_swap, vals_swap_max, vals_swap_min, vals_swap_avg, attr_cpu, vals_cpu_max, vals_cpu_min, vals_cpu_avg = self.data_mm()
            if attr_mem and vals_mem_max and vals_mem_min and vals_mem_avg:
                data['mem_line'] = c.line_three_html(
                    "温度",
                    attr_mem,
                    vals_mem_min,
                    vals_mem_max,
                    vals_mem_avg
                )
            else:
                data["mem_line"] = "<div class='alert alert-danger'>没有内存使用率[今天]数据</div>"
            if attr_swap and vals_swap_max and vals_swap_min and vals_swap_avg:
                data['swap_line'] = c.line_three_html(
                    "湿度",
                    attr_swap,
                    vals_swap_min,
                    vals_swap_max,
                    vals_swap_avg
                )
            else:
                data["swap_line"] = "<div class='alert alert-danger'>没有交换分区使用率[今天]数据</div>"
            if attr_cpu and vals_cpu_max and vals_cpu_min and vals_cpu_avg:
                data['cpu_line'] = c.line_three_html(
                    "光照",
                    attr_cpu,
                    vals_cpu_min,
                    vals_cpu_max,
                    vals_cpu_avg
                )
            else:
                data["cpu_line"] = "<div class='alert alert-danger'>没有CPU使用率[今天]数据</div>"
        # id为3表示1月内
        if int(id) == 3:
            attr_mem, vals_mem_max, vals_mem_min, vals_mem_avg, \
            attr_swap, vals_swap_max, vals_swap_min, vals_swap_avg, \
            attr_cpu, vals_cpu_max, vals_cpu_min, vals_cpu_avg = self.data_mm(method="month", format="%Y%m%d")
            if attr_mem and vals_mem_max and vals_mem_min and vals_mem_avg:
                data['mem_line'] = c.line_three_html(
                    "内存使用率本月",
                    attr_mem,
                    vals_mem_min,
                    vals_mem_max,
                    vals_mem_avg
                )
            else:
                data["mem_line"] = "<div class='alert alert-danger'>没有内存使用率[本月]数据</div>"
            if attr_swap and vals_swap_max and vals_swap_min and vals_swap_avg:
                data['swap_line'] = c.line_three_html(
                    "内存使用率本月",
                    attr_swap,
                    vals_swap_min,
                    vals_swap_max,
                    vals_swap_avg
                )
            else:
                data["swap_line"] = "<div class='alert alert-danger'>没有交换分区使用率[本月]数据</div>"
            if attr_cpu and vals_cpu_max and vals_cpu_min and vals_cpu_avg:
                data['cpu_line'] = c.line_three_html(
                    "内存使用率本月",
                    attr_cpu,
                    vals_cpu_min,
                    vals_cpu_max,
                    vals_cpu_avg
                )
            else:
                data["cpu_line"] = "<div class='alert alert-danger'>没有CPU使用率[本月]数据</div>"
        return self.html("android_log.html", data=dict(
            line_cpu=data["cpu_line"],
            line_mem=data["mem_line"],
            line_swap=data["swap_line"]
        ))

    #一小时内数据查询
    def data_by_hour(self):
        now_time,next_time = self.dt_range()
        attr_cpu,attr_mem,attr_swap = None,None,None
        vals_cpu, vals_mem, vals_swap = None, None, None
        session = ORM.db()
        try:
            #内存
            mem = self.one_hour_query(Mem,session,now_time,next_time)
            if mem :
                attr_mem = [v.create_time.strftime("%H:%M:%S") for v in mem ]
                vals_mem = [float(v.percent) for v in mem]
            #交换分区
            swap = self.one_hour_query(Swap, session, now_time, next_time)
            if swap:
                attr_swap = [v.create_time.strftime("%H:%M:%S") for v in swap]
                vals_swap = [float(v.percent) for v in swap]
            #CPU
            cpu = self.one_hour_query(Cpu, session, now_time, next_time)
            if cpu:
                attr_cpu = [v.create_time.strftime("%H:%M:%S") for v in cpu]
                vals_cpu = [float(v.percent) for v in cpu]
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return attr_swap,attr_mem,attr_cpu,vals_swap,vals_mem,vals_cpu
    #一小时查询方法
    def one_hour_query(self,model,session,now_time,next_time):
        data = session.query(model).order_by(model.create_dt.asc()).filter(
            and_(
                model.create_dt>=now_time.strftime("%Y-%m-%d %H")+":00:00",
                model.create_dt < next_time.strftime("%Y-%m-%d %H") + ":00:00",
            )
        ).all()
        return data

    #按天查询最大最小和平均值
    def data_mm(self,method="Day",format="%Y%m%d%H" ):
        session = ORM.db()
        attr_mem,vals_mem_max,vals_mem_min,vals_mem_avg = None,None,None,None
        attr_swap, vals_swap_max, vals_swap_min, vals_swap_avg = None, None, None, None
        attr_cpu, vals_cpu_max, vals_cpu_min, vals_cpu_avg = None, None, None, None
        try:
            #内存
            mem = self.three_query(Mem,session,method,format)
            attr_mem = [ v[0] for v in mem]
            vals_mem_max = [ float(v[1]) for v in mem]
            vals_mem_min = [ float(v[2]) for v in mem]
            vals_mem_avg = [ round(float(v[3]),1) for v in mem]
            #交换分区
            swap = self.three_query(Swap, session, method, format)
            attr_swap = [v[0] for v in swap]
            vals_swap_max = [float(v[1]) for v in swap]
            vals_swap_min = [float(v[2]) for v in swap]
            vals_swap_avg = [round(float(v[3]),1) for v in swap]
            #CPU
            cpu = self.three_query(Cpu, session, method, format)
            attr_cpu = [v[0] for v in cpu]
            vals_cpu_max = [float(v[1]) for v in cpu]
            vals_cpu_min = [float(v[2]) for v in cpu]
            vals_cpu_avg = [round(float(v[3]),1) for v in cpu]
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return attr_mem,vals_mem_max,vals_mem_min,vals_mem_avg,attr_swap, vals_swap_max, vals_swap_min, vals_swap_avg,attr_cpu, vals_cpu_max, vals_cpu_min, vals_cpu_avg
    #查询最大值最小值平均值方法
    def three_query(self,model,session,method="Day",format="%Y%m%d%H"):
        model_query = session.query(
            func.date_format(model.create_dt,format), #转化日期格式
            func.max(model.percent),
            func.min(model.percent),
            func.avg(model.percent),
        )
        data = None
        if method=="Day":
            data = model_query.filter(
                func.to_days(model.create_dt)==func.to_days(func.now())
            ).group_by(
                func.date_format(model.create_dt,format)
            ).order_by(model.create_dt.asc()).all()
        if method=="month":
            data = model_query.filter(
                func.date_format(model.create_dt,"%Y%m") == func.date_format(func.curdate(),"%Y%m")
            ).group_by(
                model.create_dt
            ).order_by(model.create_dt.asc()).all()
        return data
    #时间范围方法
    def dt_range(self):
        now_time = datetime.datetime.now()
        next_time = now_time+datetime.timedelta(hours=1)
        return now_time,next_time
