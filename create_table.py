from sqlalchemy.ext.declarative import declarative_base  #ORM基类
from sqlalchemy import Column,String,Integer   #导入数据库类型
from setting import connect_sql #mysql连接变量

#创建orm基类
Base=declarative_base()
#创建ORM对像（类）并继承基类
class student(Base):
    __tablename__='student' #表名，必须设置
    id=Column(Integer,primary_key=True,autoincrement=True) #id字段，设置为主键
    name=Column(String(20),default='')    #用户名
    passwd=Column(String(30),default="") #密码
    sex=Column(Integer,default='1')
    age=Column(String(16),default="18")
    num=Column(String(16),default='18')
    ig= Column(String(16), default='18')
    ie = Column(String(16), default='18')

Base.metadata.create_all(connect_sql)