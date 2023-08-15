import ast
import math
n, k = ast.literal_eval(input())
# 现在程序中有两个整数，n, k

# 在这行注释下面，编写代码，输出你的答案

""" print((1234%10)//1)
print((1234%100)//10)
print((1234%1000)//100)
print((1234%10000)//1000) """

def result(n,k):
    print((n%(10**(k+1)))//10**k)

result(n,k)
