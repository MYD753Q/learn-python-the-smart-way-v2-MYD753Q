import ast
x1,y1,r1,x2,y2,r2 = ast.literal_eval(input())
# 现在程序中有六个变量，x1,y1,r1,x2,y2,r2

# 在这行注释下面，编写代码，输出你的答案
"""
判断两个圆是否相交，可以通过计算两个圆心之间的距离与两个圆的半径之和进行比较。
如果圆心之间的距离小于等于两个圆的半径之和，那么这两个圆是相交的。 
"""
if (x1-x2)**2+(y1-y2)**2<=(r1+r2)**2:
    print('True')
else:
    print('False')