# -*- coding: utf-8 -*-
"""
Created on Sun May  6 16:00:42 2018

@author: shy
"""

from sympy import *
x, y, z = var("x y z")
g, f = var("g f")
a, b, c, d, e, f, w, v = var("a b c d e g w v")
v,w=symbols("v w")

# 建立概率p的函数表达式
p,m,n = var("p m n")
p = m*z + n

# 建立分包的期望收益函数
g = simplify(x*(y*(a-v)
       +(1-y)*(-p*b-(1-p)*c))
    +(1-x)*(y*(a-v)
          +(1-y)*(p*a-(1-p)*c)))

# g = y*(a*x-v-z*d+(1-z)*(p*e+(1-p)*f))+(1-y)*(-p*(b-e)-(1-p)*(c-f))

# 建立工人的期望收益函数
f = y*(z*(d-w)+(1-z)*(-p*e-(1-p)*f))+(1-y)*(z*(d-w)+(1-z)*(p*d-(1-p)*f))

# 求分包和工人期望收益函数的导数
dg, df = var("dg df")
dg = diff(g,y)
df = diff(f,z)

# 求解博弈模型  方程
system = [dg, df]
vars = [y, z]
result = simplify(solve(system,vars))
y,z = result[0]

# 计算概率
p = m*z+n


