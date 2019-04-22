# -*- coding: utf-8 -*-
import tornado.web
from app.views.views_common import Commonhandler
from app.tools.chart import chart
import tornado.gen
import tornado.concurrent
#定义手也视图
class IndexHandler(Commonhandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        # self.write("<h1>首页视图</h1>")
        c = chart()

        self.html("index.html", data=dict(
            kongqiwen=c.Gauge_html_kw("kongqiwen", "温度(单位 ℃)", 0),
            kongqishi=c.Gauge_html_ks("kongqishi", "湿度(单位 vol%)", 0),
            turangwen=c.Gauge_html_tw("turangwen", "温度(单位 ℃)", 0),
            turangshi=c.Gauge_html_ts("turangshi", "湿度(单位 vol%)", 0),
            guangzhao=c.Gauge_html_gq("guangzhao", "光照强度(单位 lux(勒克斯）)", 0)
        ))