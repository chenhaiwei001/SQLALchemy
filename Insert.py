from setting import connect_sql
from sqlalchemy.orm import sessionmaker

#写入数据的封装函数
def Insert_into(data):
    # 绑定mysql并创建会话
    session=sessionmaker(bind=connect_sql)
    Session=session()    #实例化会话对象
    Session.add(data)    #添加对象
    Session.commit()     #提交事务
    Session.close()     #关闭连接
    print("insert ok!")
"""
   说明：
    1、对写入数据进一步封装，调用时将数据传入函数的变量即可。
    2、优化代码结构，减少冗余。提高可读性。
"""
"""
    1、如果表中新增字段，需要在mysql中手动添加和student中一样的字段，不然会报错。
    2、如果部分字段不传数据，则系统会写入默认值。
    3、提交事务前要先添加对象，直接担交事务产会报错，但数据无法写入。
    4、提交完成后要关闭会话，释放相应的资源。
"""