#import numpy as np
#调用numpy库非常耗时
import ast
import math
n = ast.literal_eval(input())
# 现在程序中有一个整数，n

# 在这行注释下面，编写代码，输出你的答案
#反向求解，并注意向上取整。解方程a*2+a-2n=0，a是所需要的总行数
def Reverse_solution(n):
   x1,x2=(-1+math.sqrt(1+8*n))/2,(-1-math.sqrt(1+8*n))/2
   if x1>=0:
      return math.ceil(x1)    #数学逻辑实现取整更快，对0取整作为判断条件。满足直接输出，不满足整除1再加1
   else:
      return math.ceil(x2) 

print(Reverse_solution(n))


'''
#超时
coefficients = [1, 1, -2*n]  # 代表方程 x^2 + x - 2*n = 0 的系数
roots = np.roots(coefficients)
if roots[0]<0:
   print(math.ceil(roots[1])) 
else:
   print(math.ceil(roots[0]))
'''