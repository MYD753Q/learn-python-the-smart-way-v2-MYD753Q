import ast
x1,x2 = ast.literal_eval(input())
# 现在程序中有变量x1和x2

# 在这行注释下面，编写代码，输出你的答案

# 注意，输出样例与描述不符合。描述是输出用空格隔开，给出的样例是以逗号隔开。
# 以描述为准，否则无法通过
if x1>x2:
    print(x2,x1)
else:
    print(x1,x2)