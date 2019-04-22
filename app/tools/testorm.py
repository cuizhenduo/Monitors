from app.models.models import Kongqishidu,Kongqiwendu,Turangshidu,Turangwendu,Guangzhao
from app.tools.orm import ORM

session = ORM.db()
kw = session.query(Kongqiwendu).order_by(Kongqiwendu.create_dt.desc()).first()
print(kw.percent)