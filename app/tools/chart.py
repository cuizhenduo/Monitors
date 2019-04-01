# -*- coding: utf-8 -*-
import datetime
from pyecharts import Liquid,Gauge,Pie,Line

class chart(object):
    #水球图
    def Liquid_html(self,chard_id,title,val):
        liquid = Liquid(
            "{}-{}".format(self.dt,title),
            title_pos="center",
            width="100%",
            title_color="white",
            title_text_size=14,
            height=300
        )
        liquid.chart_id = chard_id
        liquid.add("",[round(val/100,4)])
        return liquid.render_embed() #返回图表的html代码

    #仪表图
    def Gauge_html(self,chard_id,title,val):
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
            scale_range=[0,100],
            is_legend_show=False
        )
        return gauge.render_embed()
    #饼图
    def pie_html(self,chard_id,title,sub_title1,sub_title2,key1,key2,val1,val2):
        #实例化饼状图
        pie = Pie(
            "{}-{}".format(self.dt,title),
            title_pos="center",
            width="100%",
            height=300,
            title_text_size=14,
            title_color="white"
        )
        #指定id
        pie.chart_id = chard_id
        pie.add(
            sub_title1,
            key1,
            val1,
            center=[25,50],
            is_random=True,
            radius=[30,75],
            rosetype="area",
            is_legend_show=False,
            is_label_show=True
        )
        pie.add(
            sub_title2,
            key2,
            val2,
            center=[75, 50],
            is_random=True,
            radius=[30, 75],
            rosetype="area",
            is_legend_show=False,
            is_label_show=True
        )
        return pie.render_embed()
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
