from sqlalchemy import create_engine #mysql连接函数
from sqlalchemy.orm import sessionmaker

#mysql连接配置
connect_sql=create_engine(
    #mysql连接配置
    "mysql+pymysql://root:bai940126@111.67.196.17/Mysite",
    encoding="utf-8",  #编码
    #echo=True    #打印结果
    )

#连接会话
session = sessionmaker(bind=connect_sql)
Session = session()  # 实例化会话对象


#单个对象转字典去掉多余信息（多个对象时需要写到models中）
def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}

#配合to_dict将多个对象转换为字典格式
#需要在类中加to_dict方法
def to_dicts(all_vendors):
    v = [ven.to_dict() for ven in all_vendors]
    return v



"""
    1、该文件为mysql连接的公共配置文件，供所有需要连接的文件调用。
    2、写成配置文件的形式，可以优化代码，并且可以方便后期更改维护。
    
    3、to_dicts()函数为多个sql查询对象转字典的函数，配合class中的内置函数使用。

"""