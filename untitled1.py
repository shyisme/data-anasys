# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:34:07 2018

@author: shy
"""

#求解政府监理施工总承包的博弈
from sympy import *
a,b,c,d,e,f,g,h,i,j,k,l,m=symbols("a b c d e f g h i j k l m")
x,y,z=symbols("x y z")
f1,f2,f3=symbols("f1,f2,f3")
"""
w,v,p=symbols("w v p")
p=w+v/x
b0,i0,j0,l0=symbols("b0 i0 j0 l0")
b=p*b0
i=p*i0
j=p*j0
l=p*l0
"""

f1=simplify(x*x*(1-x)*(y*z*(-a-e-f)+y*(1-z)*(-a-e+d)+
           (1-y)*z*(-a+c-f+b)+(1-y)*(1-z)*(-a+c+d+b)))
f2=simplify(y*x*(1-y)*(x*z*(e+c+j-h)+x*(1-z)*(e+c+i-h)+
           (1-x)*z*(j-h)+(1-x)*(1-z)*(i-h)))
f3=simplify(z*x*(1-z)*(x*y*(f+l+d)+x*(1-y)*(f-m+l+d)+
            (1-x)*y*l+(1-x)*(1-y)*(-m+l)))


system = [f1,f2,f3]
vars = [x, y, z]
result = simplify(solve(system,vars))