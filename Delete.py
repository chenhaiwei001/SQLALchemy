from create_table import student
from setting import Session

#删除数据
Ass=Session.query(student).filter(student.id==27).first() #查询
Session.delete(Ass)  #删除查询的数据
Session.commit()     #提交事务
Session.close()    #关闭连接

"""
   说明：
    1、这里仅作删除数据处理
    2、基本思路：
       1）根据条件查询相应的数据
       2）执行删除
       3）提交事务
       4）关闭资源
"""