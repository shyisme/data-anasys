from sympy import *
import numpy as np
l,d,t,e=symbols("l d t e")
a,o,I,W,p,x,k,c,q,t0,b,o1,o2,f1,f2,f3,f1_l,f1_t,f2_e,f3_d=symbols("a o  I  W p x k c q t0 b o1 o2 f1 f2 f3  f1_l f1_t f2_e f3_d")
f1=(a-l)*e*o+p*d+d*t+l*x-q*t
f2=l*e*o-l*x-1/2*k*(e**2)
f3=(1-d)*c+b*(t-t0)-d*t
f1_l=diff(f1,l)
f1_t=diff(f1,t)
f2_e=diff(f2,e)
f3_d=diff(f3,d)
system=[f1_l,f1_t,f2_e,f3_d]
system_simplity=simplify(system)
vars=[l,t,e,d]
result = simplify(solve(system,vars))

