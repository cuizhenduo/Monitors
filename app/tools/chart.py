# -*- coding: utf-8 -*-
import datetime
from pyecharts import Liquid,Gauge,Pie,Line

class chart(object):
    #空气温度仪表图
    def Gauge_html_kw(self,chard_id,title,val):
        gauge = Gauge(
            "{}-{}".format(self.dt, title),
            title_pos="center",
            width="100%",
            title_color="white",
            title_text_size=14,
            height=300
        )
        gauge.chart_id = chard_id
        gauge.add(
            "",
            "",
            val,
            scale_range=[0,35],
            is_legend_show=False
        )
        return gauge.render_embed()

    # 空气湿度仪表图
    def Gauge_html_ks(self, chard_id, title, val):
        gauge = Gauge(
            "{}-{}".format(self.dt, title),
            title_pos="center",
            width="100%",
            title_color="white",
            title_text_size=14,
            height=300
        )
        gauge.chart_id = chard_id
        gauge.add(
            "",
            "",
            val,
            scale_range=[0, 100],
            is_legend_show=False
        )
        return gauge.render_embed()

    # 土壤温度仪表图
    def Gauge_html_tw(self, chard_id, title, val):
        gauge = Gauge(
            "{}-{}".format(self.dt, title),
            title_pos="center",
            width="100%",
            title_color="white",
            title_text_size=14,
            height=300
        )
        gauge.chart_id = chard_id
        gauge.add(
            "",
            "",
            val,
            scale_range=[5, 40],
            is_legend_show=False
        )
        return gauge.render_embed()

    # 土壤湿度仪表图
    def Gauge_html_ts(self, chard_id, title, val):
        gauge = Gauge(
            "{}-{}".format(self.dt, title),
            title_pos="center",
            width="100%",
            title_color="white",
            title_text_size=14,
            height=300
        )
        gauge.chart_id = chard_id
        gauge.add(
            "",
            "",
            val,
            scale_range=[-30, 60],
            is_legend_show=False
        )
        return gauge.render_embed()

    # 光照强度仪表图
    def Gauge_html_gq(self, chard_id, title, val):
        gauge = Gauge(
            "{}-{}".format(self.dt, title),
            title_pos="center",
            width="100%",
            title_color="white",
            title_text_size=14,
            height=300
        )
        gauge.chart_id = chard_id
        gauge.add(
            "",
            "",
            val,
            scale_range=[0,3000],
            is_legend_show=False
        )
        return gauge.render_embed()

    #折现面积图
    def line_html(self,title,key,value,color=None):
        line = Line(
            title,
            title_pos="center",
            width="100%",
            height=300
        )
        line.add(
            "",
            key,
            value,
            mark_point=["average","max","min"],
            mark_line=["average","max","min"],
            area_color=color,
            line_opacity=0.2,#透明度
            area_opacity=0.4,
            is_datazoom_show=True, #是否支持缩放
            datazoom_range=[0,100],#缩放范围
            symbol=None
        )
        return line.render_embed()

    # 折线图
    def line_three_html(self, title,key,val_min,val_max,val_avg):
        line = Line(
            title,
            title_pos="left",
            width="100%",
            height=300
        )
        line.add(
            "最小值",
            key,
            val_min,
            mark_point=["average", "max", "min"],
            is_datazoom_show=True,  # 是否支持缩放
            datazoom_range=[0, 100],  # 缩放范围
            is_smooth=True
        )
        line.add(
            "最大值",
            key,
            val_max,
            mark_point=["average", "max", "min"],
            is_datazoom_show=True,  # 是否支持缩放
            datazoom_range=[0, 100],  # 缩放范围
            is_smooth=True
        )
        line.add(
            "平均值",
            key,
            val_avg,
            mark_point=["average", "max", "min"],
            is_datazoom_show=True,  # 是否支持缩放
            datazoom_range=[0, 100],  # 缩放范围
            is_smooth=True
        )
        return line.render_embed()
    @property
    def dt(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
