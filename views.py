from Insert import Insert_into
from setting import Session
from create_table import student

# #写入数据，没有写入的则使用默认值
# DATA=student(name="chen",passwd='hao1',sex='1',age=18,num=12)
# #调用封装的函数，写入mysql表中
# Insert_into(DATA)
#
# AA=Session.query(student.age).filter(student.id>5).all()
AA=Session.query(student.id).all()
if AA:
  print(AA)
else:
  print("on")