"""
%s  字符串
%d   整数
%f   浮点
%%    输出%


"""

#.format()

name='wade'
age=28
weight=66.5
height=175.5
print('我是%s,今年%d岁，体重：%.2f公斤，身高：%.2fcm' %(name,age,weight,height),sep=' ')


print('我是{},今年{}岁，体重：{}公斤，身高：{}'.format(name,age,weight,height))

print('我是{name},今年{age}岁，体重：{weight}公斤，身高：{height}'.format(name=name,age=age,weight=weight,height=height))

list1=['wade',45,66.5,180.0]
print('我是{0[0]},今年{0[1]}岁，体重：{0[2]}公斤，身高：{0[3]}'.format(list1))