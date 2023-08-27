import ast
y,m=ast.literal_eval(input())
# 现在程序中有两个变量y,m

# 在这行注释下面，编写代码，输出你的答案
if y%4==0 and y%100!=0:
    isLeapyear=True
elif y%400==0:
    isLeapyear=True
else:
    isLeapyear=False

if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print(31)
if m==4 or m==6 or m==9 or m==11:
    print(30)
if m==2:
    if isLeapyear==True:
        print(29)
    else:
        print(28)