# -*- coding: utf-8 -*-
import tornado.web
from app.views.views_common import Commonhandler
import json
import tornado.gen
import tornado.concurrent
from app.models.models import Facility
from app.tools.orm import ORM

# myOpen
class AjaxHandler(Commonhandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        id = self.get_argument('id')
        nzt = self.get_argument('zt')
        session = ORM.db()
        kw = session.query(Facility).filter(Facility.id==id).first()
        if nzt=="关闭":
            if kw.stat=="关闭":
                kw.stat = "打开"
                session.commit()
                session.close()
            else:
                pass
        ret = {'states': '成功', 'message': ''}
        self.write(json.dumps(ret))

# myClose
class AjaxHandlerClose(Commonhandler):
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield self.get_response()

    @tornado.concurrent.run_on_executor
    def get_response(self):
        id = self.get_argument('id')
        nzt = self.get_argument('zt')
        session = ORM.db()
        kw = session.query(Facility).filter(Facility.id==id).first()
        if nzt=="打开":
            if kw.stat=="打开":
                kw.stat = "关闭"
                session.commit()
                session.close()
            else:
                pass
        ret = {'states': '成功', 'message': ''}
        self.write(json.dumps(ret))
