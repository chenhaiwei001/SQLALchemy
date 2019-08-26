
from setting import Session        #导入封装好的会话函数
from create_table import student   #导入表


# #方式一
# Session.query(student).filter(student.id == 27).update({'name':"wei11"}) #更改数据
# Session.commit()   #提交事务
# Session.close()  #关闭连接

#方式二：
Ass=Session.query(student).filter(student.id==27).first()
Ass.name="陈海龟"
Session.commit()   #提交事务
Session.close()  #关闭连接

"""
说明：
    1、这里演示更改数据操作
    2、更改思路：
        1）根据条件查询需要更改的某一行数据
        2）更改对应的字段
    3、使用update方法更改

"""