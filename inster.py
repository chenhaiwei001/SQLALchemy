from create_table import student  #导入操作对象（学生表）
from setting import Session #sql会话对象 （在setting.py文件中写好）

#需要写入的数据
DATA=student(name="chen",passwd='hao',sex='1',age=18,num=12)


Session.add(DATA)   #添加对象
Session.commit()    #提交事务
Session.close()    #关闭会话，释放资源

"""
说明：
    1、如果表中新增字段，需要在mysql中手动添加和student中一样的字段，不然会报错。
    2、如果部分字段不传数据，则系统会写入默认值。
    3、提交事务前要先添加对象，直接担交事务产会报错，但数据无法写入。
    4、提交完成后要关闭会话，释放相应的资源。

"""