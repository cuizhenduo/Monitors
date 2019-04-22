# -*- coding:utf-8 -*-
import datetime
from app.views.views_common import Commonhandler
from sqlalchemy import and_,func
from app.tools.orm import ORM
from app.models.models import Cpu,Mem,Swap,Kongqiwendu,Kongqishidu,Turangwendu,Turangshidu,Guangzhao
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
        id = self.get_argument("id", 1)
        data = dict()
        c = chart()
        # id为1表示1小时内
        if int(id) == 1:
            attr_kongqiwendu, attr_kongqishidu, attr_turangshidu, attr_turangwendu, attr_guangzhao, vals_guangzhao, vals_kongqiwendu, vals_turangshidu, vals_turangwendu, vals_kongqishidu = self.data_by_hour()
            # 空气温度
            if attr_kongqiwendu and vals_kongqiwendu:
                data["kongqiwendu"] = c.line_html(
                    "空气温度数据[1小时内]",
                    attr_kongqiwendu,
                    vals_kongqiwendu,
                    "green"
                )
            else:
                data["kongqiwendu"] = "<div class='alert alert-danger'>没有温度数据</div>"
            # 空气湿度
            if attr_kongqishidu and vals_kongqishidu:
                data["kongqishidu"] = c.line_html(
                    "空气湿度数据[1小时内]",
                    attr_kongqishidu,
                    vals_kongqishidu,
                    "green"
                )
            else:
                data["kongqishidu"] = "<div class='alert alert-danger'>没有湿度数据</div>"
            # 土壤温度
            if attr_turangwendu and vals_turangwendu:
                data["turangwendu"] = c.line_html(
                    "土壤温度数据[1小时内]",
                    attr_turangwendu,
                    vals_turangwendu,
                    "green"
                )
            else:
                data["turangwendu"] = "<div class='alert alert-danger'>没有土壤温度数据</div>"
            # 土壤湿度
            if attr_turangshidu and vals_turangshidu:
                data["turangshidu"] = c.line_html(
                    "土壤湿度数据[1小时内]",
                    attr_turangshidu,
                    vals_turangshidu,
                    "green"
                )
            else:
                data["turangshidu"] = "<div class='alert alert-danger'>没有土壤湿度数据</div>"
            # 光照强度
            if attr_guangzhao and vals_guangzhao:
                data["guangzhao"] = c.line_html(
                    "光照强度数据[1小时内]",
                    attr_guangzhao,
                    vals_guangzhao,
                    "green"
                )
            else:
                data["guangzhao"] = "<div class='alert alert-danger'>没有光照数据</div>"

        # id为2表示1天内
        if int(id) == 2:
            attr_kongqiwendu,vals_kongqiwendu_max,vals_kongqiwendu_min,vals_kongqiwendu_avg, \
            attr_kongqishidu, vals_kongqishidu_max, vals_kongqishidu_min, vals_kongqishidu_avg, \
            attr_turangwendu, vals_turangwendu_max, vals_turangwendu_min, vals_turangwendu_avg, \
            attr_turangshidu, vals_turangshidu_max, vals_turangshidu_min, vals_turangshidu_avg, \
            attr_guangzhao, vals_guangzhao_max, vals_guangzhao_min, vals_guangzhao_avg = self.data_mm()
            if attr_kongqiwendu and vals_kongqiwendu_max and vals_kongqiwendu_min and vals_kongqiwendu_avg:
                data['kongqiwendu'] = c.line_three_html(
                    "空气温度今天",
                    attr_kongqiwendu,
                    vals_kongqiwendu_min,
                    vals_kongqiwendu_max,
                    vals_kongqiwendu_avg
                )
            else:
                data["kongqiwendu"] = "<div class='alert alert-danger'>没有空气温度[今天]数据</div>"
            if attr_kongqishidu and vals_kongqishidu_max and vals_kongqishidu_min and vals_kongqishidu_avg:
                data['kongqishidu'] = c.line_three_html(
                    "空气湿度今天",
                    attr_kongqishidu,
                    vals_kongqishidu_min,
                    vals_kongqishidu_max,
                    vals_kongqishidu_avg
                )
            else:
                data["kongqishidu"] = "<div class='alert alert-danger'>没有空气湿度[今天]数据</div>"
            if attr_turangwendu and vals_turangwendu_max and vals_turangwendu_min and vals_turangwendu_avg:
                data['turangwendu'] = c.line_three_html(
                    "土壤温度今天",
                    attr_turangwendu,
                    vals_turangwendu_min,
                    vals_turangwendu_max,
                    vals_turangwendu_avg
                )
            else:
                data["turangwendu"] = "<div class='alert alert-danger'>没有土壤温度[今天]数据</div>"
            if attr_turangshidu and vals_turangshidu_max and vals_turangshidu_min and vals_turangshidu_avg:
                data['turangshidu'] = c.line_three_html(
                    "土壤湿度今天",
                    attr_turangshidu,
                    vals_turangshidu_min,
                    vals_turangshidu_max,
                    vals_turangshidu_avg
                )
            else:
                data["turangshidu"] = "<div class='alert alert-danger'>没有土壤湿度[今天]数据</div>"
            if attr_guangzhao and vals_guangzhao_max and vals_guangzhao_min and vals_guangzhao_avg:
                data['guangzhao'] = c.line_three_html(
                    "光照数据今天",
                    attr_guangzhao,
                    vals_guangzhao_min,
                    vals_guangzhao_max,
                    vals_guangzhao_avg
                )
            else:
                data["guangzhao"] = "<div class='alert alert-danger'>没有光照[今天]数据</div>"

        # id为3表示1月内
        if int(id) == 3:
            attr_kongqiwendu, vals_kongqiwendu_max, vals_kongqiwendu_min, vals_kongqiwendu_avg, \
            attr_kongqishidu, vals_kongqishidu_max, vals_kongqishidu_min, vals_kongqishidu_avg, \
            attr_turangwendu, vals_turangwendu_max, vals_turangwendu_min, vals_turangwendu_avg, \
            attr_turangshidu, vals_turangshidu_max, vals_turangshidu_min, vals_turangshidu_avg, \
            attr_guangzhao, vals_guangzhao_max, vals_guangzhao_min, vals_guangzhao_avg = self.data_mm(method="month", format="%Y%m%d")
            if attr_kongqiwendu and vals_kongqiwendu_max and vals_kongqiwendu_min and vals_kongqiwendu_avg:
                data['kongqiwendu'] = c.line_three_html(
                    "空气温度本月",
                    attr_kongqiwendu,
                    vals_kongqiwendu_min,
                    vals_kongqiwendu_max,
                    vals_kongqiwendu_avg
                )
            else:
                data["kongqiwendu"] = "<div class='alert alert-danger'>没有空气温度[本月]数据</div>"
            if attr_kongqishidu and vals_kongqishidu_max and vals_kongqishidu_min and vals_kongqishidu_avg:
                data['kongqishidu'] = c.line_three_html(
                    "空气湿度本月",
                    attr_kongqishidu,
                    vals_kongqishidu_min,
                    vals_kongqishidu_max,
                    vals_kongqishidu_avg
                )
            else:
                data["kongqishidu"] = "<div class='alert alert-danger'>没有空气湿度[本月]数据</div>"
            if attr_turangwendu and vals_turangwendu_max and vals_turangwendu_min and vals_turangwendu_avg:
                data['turangwendu'] = c.line_three_html(
                    "土壤温度本月",
                    attr_turangwendu,
                    vals_turangwendu_min,
                    vals_turangwendu_max,
                    vals_turangwendu_avg
                )
            else:
                data["turangwendu"] = "<div class='alert alert-danger'>没有土壤温度[本月]数据</div>"
            if attr_turangshidu and vals_turangshidu_max and vals_turangshidu_min and vals_turangshidu_avg:
                data['turangshidu'] = c.line_three_html(
                    "土壤湿度本月",
                    attr_turangshidu,
                    vals_turangshidu_min,
                    vals_turangshidu_max,
                    vals_turangshidu_avg
                )
            else:
                data["turangshidu"] = "<div class='alert alert-danger'>没有土壤湿度[本月]数据</div>"
            if attr_guangzhao and vals_guangzhao_max and vals_guangzhao_min and vals_guangzhao_avg:
                data['guangzhao'] = c.line_three_html(
                    "光照数据本月",
                    attr_guangzhao,
                    vals_guangzhao_min,
                    vals_guangzhao_max,
                    vals_guangzhao_avg
                )
            else:
                data["guangzhao"] = "<div class='alert alert-danger'>没有光照[本月]数据</div>"

        return self.html("android_log.html", hisdata=dict(
            kongqiwendu=data["kongqiwendu"],
            kongqishidu=data["kongqishidu"],
            turangwendu = data["turangwendu"],
            turangshidu=data["turangshidu"],
            guangzhao = data["guangzhao"]
        ))

    #一小时内数据查询
    def data_by_hour(self):
        now_time,next_time = self.dt_range()
        attr_kongqiwendu,attr_kongqishidu,attr_turangwendu,attr_turangshidu,attr_guangzhao = None,None,None,None,None
        vals_kongqiwendu, vals_kongqishidu, vals_turangwendu,vals_turangshidu,vals_guangzhao = None, None, None,None,None
        session = ORM.db()
        try:
            #空气温度
            kw = self.one_hour_query(Kongqiwendu,session,now_time,next_time)
            if kw :
                attr_kongqiwendu = [v.create_time.strftime("%H:%M:%S") for v in kw ]
                vals_kongqiwendu = [float(v.percent) for v in kw]
            # 空气湿度
            ks = self.one_hour_query(Kongqishidu, session, now_time, next_time)
            if ks:
                attr_kongqishidu = [v.create_time.strftime("%H:%M:%S") for v in ks]
                vals_kongqishidu = [float(v.percent) for v in ks]
            # 土壤温度
            tw = self.one_hour_query(Turangwendu, session, now_time, next_time)
            if tw:
                attr_turangwendu = [v.create_time.strftime("%H:%M:%S") for v in tw]
                vals_turangwendu = [float(v.percent) for v in tw]
            # 土壤湿度
            ts = self.one_hour_query(Turangshidu, session, now_time, next_time)
            if ts:
                attr_turangshidu = [v.create_time.strftime("%H:%M:%S") for v in ts]
                vals_turangshidu = [float(v.percent) for v in ts]
            #光照强度
            gq = self.one_hour_query(Guangzhao,session,now_time,next_time)
            if gq :
                attr_guangzhao = [v.create_time.strftime("%H:%M:%S") for v in gq ]
                vals_guangzhao = [float(v.percent) for v in gq]
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return attr_kongqiwendu,attr_kongqishidu,attr_turangshidu,attr_turangwendu,attr_guangzhao,vals_guangzhao,vals_kongqiwendu,vals_turangshidu,vals_turangwendu,vals_kongqishidu
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
        attr_kongqiwendu, vals_kongqiwendu_max, vals_kongqiwendu_min, vals_kongqiwendu_avg = None,None,None,None
        attr_kongqishidu, vals_kongqishidu_max, vals_kongqishidu_min, vals_kongqishidu_avg = None,None,None,None
        attr_turangwendu, vals_turangwendu_max, vals_turangwendu_min, vals_turangwendu_avg = None,None,None,None
        attr_turangshidu, vals_turangshidu_max, vals_turangshidu_min, vals_turangshidu_avg = None,None,None,None
        attr_guangzhao, vals_guangzhao_max, vals_guangzhao_min, vals_guangzhao_avg = None,None,None,None
        try:
            #空气温度
            kongqiwendu = self.three_query(Kongqiwendu,session,method,format)
            attr_kongqiwendu = [ v[0] for v in kongqiwendu]
            vals_kongqiwendu_max = [ float(v[1]) for v in kongqiwendu]
            vals_kongqiwendu_min = [ float(v[2]) for v in kongqiwendu]
            vals_kongqiwendu_avg = [ round(float(v[3]),1) for v in kongqiwendu]
            # 空气湿度
            kongqishidu = self.three_query(Kongqishidu, session, method, format)
            attr_kongqishidu = [v[0] for v in kongqishidu]
            vals_kongqishidu_max = [float(v[1]) for v in kongqishidu]
            vals_kongqishidu_min = [float(v[2]) for v in kongqishidu]
            vals_kongqishidu_avg = [round(float(v[3]), 1) for v in kongqishidu]
            # 土壤温度
            turangwendu = self.three_query(Turangwendu, session, method, format)
            attr_turangwendu = [v[0] for v in turangwendu]
            vals_turangwendu_max = [float(v[1]) for v in turangwendu]
            vals_turangwendu_min = [float(v[2]) for v in turangwendu]
            vals_turangwendu_avg = [round(float(v[3]), 1) for v in turangwendu]
            # 土壤湿度
            turangshidu = self.three_query(Turangshidu, session, method, format)
            attr_turangshidu = [v[0] for v in turangshidu]
            vals_turangshidu_max = [float(v[1]) for v in turangshidu]
            vals_turangshidu_min = [float(v[2]) for v in turangshidu]
            vals_turangshidu_avg = [round(float(v[3]), 1) for v in turangshidu]
            # 光照强度
            guangzhao = self.three_query(Guangzhao, session, method, format)
            attr_guangzhao = [v[0] for v in guangzhao]
            vals_guangzhao_max = [float(v[1]) for v in guangzhao]
            vals_guangzhao_min = [float(v[2]) for v in guangzhao]
            vals_guangzhao_avg = [round(float(v[3]), 1) for v in guangzhao]
        except Exception as e:
            session.rollback()
        else:
            session.commit()
        finally:
            session.close()
        return attr_kongqiwendu,vals_kongqiwendu_max,vals_kongqiwendu_min,vals_kongqiwendu_avg, \
            attr_kongqishidu, vals_kongqishidu_max, vals_kongqishidu_min, vals_kongqishidu_avg, \
            attr_turangwendu, vals_turangwendu_max, vals_turangwendu_min, vals_turangwendu_avg, \
            attr_turangshidu, vals_turangshidu_max, vals_turangshidu_min, vals_turangshidu_avg, \
            attr_guangzhao, vals_guangzhao_max, vals_guangzhao_min, vals_guangzhao_avg
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
