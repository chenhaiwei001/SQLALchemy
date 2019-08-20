from sqlalchemy import create_engine #mysql连接函数
from sqlalchemy.orm import sessionmaker

#mysql连接配置
connect_sql=create_engine(
    #mysql连接配置
    "mysql+pymysql://root:bai940126@111.67.196.17/Mysite",
    encoding="utf-8",  #编码
    #echo=True    #打印结果
    )

session = sessionmaker(bind=connect_sql)
Session = session()  # 实例化会话对象

"""
    1、该文件为mysql连接的公共配置文件，供所有需要连接的文件调用。
    2、写成配置文件的形式，可以优化代码，并且可以方便后期更改维护。

"""