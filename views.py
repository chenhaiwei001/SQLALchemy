from Insert import Insert_into
from setting import Session
from create_table import student



# #写入数据，没有写入的则使用默认值
# DATA=student(name="chen",passwd='hao1',sex='1',age=18,num=12)
# #调用封装的函数，写入mysql表中
# Insert_into(DATA)

# #根据条件查询数据对象
# Ass=Session.query(student).filter(student.id==27).first()
# #转换成字典(使用.__dict__方法)
# a=Ass.__dict__
# print(a["num"])


# #更改表中已有的数据
# #思路：根据条件查询对应的数据，然和使用update()更改数据
# Session.query(student).filter(student.id == 27).update({'name':"wei"})
# Session.commit


#将查询的结果转化为字典，去掉多余信息
ASS=Session.query(student).filter(student.id>5).all()
print(ASS)

