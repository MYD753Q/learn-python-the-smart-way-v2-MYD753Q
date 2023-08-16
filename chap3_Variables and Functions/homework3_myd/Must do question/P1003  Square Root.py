import ast
import math
x1 = ast.literal_eval(input())

# 现在程序中有一个变量x1

# 在这行注释下面，编写代码，输出你的答案
y1=math.sqrt(x1)
# 当你想在输出保留两位小数时，你可以这样做
# y1 = 1.0000 #最后输出的变量
print('%.2f' %y1)
