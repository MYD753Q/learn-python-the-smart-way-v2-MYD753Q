import ast
import math
eggs = ast.literal_eval(input())

# 现在程序中有一个整数，eggs

# 在这行注释下面，编写代码，输出你的答案
'''
#判断
if eggs%12==0:
    print(eggs//12)
else:
    print((eggs//12)+1)
'''
#math.ceil() 返回 x 的向上取整，即大于或等于 x 的最小的整数。
print(math.ceil(eggs/12))   