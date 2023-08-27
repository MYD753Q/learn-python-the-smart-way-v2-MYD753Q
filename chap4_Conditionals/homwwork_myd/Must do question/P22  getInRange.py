import ast
x,bound1,bound2 = ast.literal_eval(input())


# 现在程序中有三个变量 x,bound1,bound2

# 在这行注释下面，编写代码，输出你的答案
if bound1<bound2:
    floor=bound1
    upper_limit=bound2
else:
    floor=bound2
    upper_limit=bound1

if x<=floor:
    print(floor)
elif x>=upper_limit:
    print(upper_limit)
else:
    print(x)
