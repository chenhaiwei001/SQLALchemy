from setting import Session,to_dicts,to_dict
from create_table import student


#查询单个字段(以元组形式返回)
Ass=Session.query(student.name).filter(student.id==27).first()
print(Ass)


#查询多个字段(以元组形式返回)
Ass=Session.query(student.name,student.age).filter(student.id==27).first()
print(Ass)


#查询单条数据（obj形式返回，需要转字典才可读）
Ass=Session.query(student).filter(student.id==27).first()
print(to_dict(Ass))


#重写models，承继student,添加to_dict方法
class student(student):
    # 单个对象转字典去掉多余信息（多个对象时需要写到models中）
    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}
#查询多个对象（obj形式返回，需要转字典才可读）
ASS=Session.query(student).filter(student.id>5).all() #查询
print(to_dicts(ASS)) #转字典



"""
   说明：
   1、这里仅作简单的查询参考
   
   2、models建议反向影射生成，不建议直接在models中创建。
      一是因为新增字段会比较麻烦，二是因为原有表不好操作。
      
   3、多个对象转字典时，建议使用新建类，再继承表类的方法，这样可以不用
     用在models中添加任何数据，sql表中新增字段时，执行相关命令即可根据数据库
     的变化而变化，不用考虑相关的影响，便于维护。
"""