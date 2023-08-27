x = int(input())
# 现在程序中有一个变量x

# 在这行注释下面，编写代码，输出你的答案
if x%4==0 and x%100!=0:
    print("True")
elif x%400==0:
    print("True")
else:
    print("False")
