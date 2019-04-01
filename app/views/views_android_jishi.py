# -*- coding: utf-8 -*-
import tornado.web
from app.views.views_common import Commonhandler
from app.tools.monitor import Monitor
from app.tools.chart import chart
import tornado.gen
import tornado.concurrent
#定义手也视图
class Android_IndexHandler(Commonhandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        # self.write("<h1>首页视图</h1>")
        m = Monitor()
        c = chart()
        mem_info = m.mem()
        swap_info = m.swap()
        cpu_info = m.cpu()
        net_info = m.net()
        disk_info = m.disk()
        net_pie = [
            c.pie_html(
                "net{}".format(k + 1),
                "{}网卡信息".format(v["name"]),
                "收发包数统计",
                "收发字节统计",
                ["收包数", "发包数"],
                ["收字节", "发字节"],
                [v["packets_recv"], v["packets_sent"]],
                [v["bytes_recv"], v["bytes_sent"]]
            )
            for k, v in enumerate(net_info) if v["packets_recv"] and v["packets_sent"]
        ]
        self.html("android_index.html", data=dict(
            cpu_info=cpu_info,
            mem_info=mem_info,
            swap_info=swap_info,
            net_info=net_info,
            disk_info=disk_info,
            cpu_liquid=c.Liquid_html("cpu_avg", "温度", cpu_info["percent_avg"]),
            mem_gauge=c.Gauge_html("mem", "湿度", mem_info["percent"]),
            swap_gauge=c.Gauge_html("swap", "光照", swap_info['percent']),
            net_pie=net_pie
        ))