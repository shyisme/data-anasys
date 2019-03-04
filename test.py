# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 11:57:04 2018

@author: shy
"""

import ode
import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt

a=10
b_0=60
c=8
d=6
e=7
f=5
c_0=8
d_0=6
e_0=7
f_0=5
h=14
i_0=15
j_0=20
l_0=15
m=4
v=0.199
w=0.199+0.999
p=0.5
t=1.1
r=0.9
q=1.0
s=0.8

def fy(t,X):
    global p
    p=w-v/X[1]
    if p<0:
        p=0
    elif p>1:
        p=1

    x_1=X[0]*(1-X[0])*(X[1]*X[2]*(0-a-e-f)+X[1]*(1-X[2])*(0-a-e+d)+(1-X[1])*X[2]*(0-a+c-f+p*b_0)+(1-X[1])*(1-X[2])*(0-a+c+d+p*b_0))
    x_2=X[1]*(1-X[1])*(X[0]*X[2]*(e+c+p*j_0-h)+X[0]*(1-X[2])*(e+c+p*i_0-h)+(1-X[0])*X[2]*(p*j_0-h)+(1-X[0])*(1-X[2])*(p*i_0-h))
    x_3=X[2]*(1-X[2])*(X[0]*X[1]*(f+p*l_0+d)+X[0]*(1-X[1])*(f-m+p*l_0+d)+(1-X[0])*X[1]*p*l_0+(1-X[0])*(1-X[1])*(0-m+p*l_0))
    for i in [x_1,x_2,x_3]:
        if i<0:
            i=0
        elif i>1:
            i=1

    dX=[x_1,
         x_2,
         x_3]
    return dX

def fz(t,X):
    global p
    p=w-v/X[1]
    if p<0:
        p=0
    elif p>1:
        p=1

    c=t*c_0*(1-X[1])
    d=r*d_0*(1-X[2])
    e=q*e_0*X[1]
    f=s*f_0*X[2]

    x_1=X[0]*(1-X[0])*(X[1]*X[2]*(0-a-e-f)+X[1]*(1-X[2])*(0-a-e+d)+(1-X[1])*X[2]*(0-a+c-f+p*b_0)+(1-X[1])*(1-X[2])*(0-a+c+d+p*b_0))
    x_2=X[1]*(1-X[1])*(X[0]*X[2]*(e+c+p*j_0-h)+X[0]*(1-X[2])*(e+c+p*i_0-h)+(1-X[0])*X[2]*(p*j_0-h)+(1-X[0])*(1-X[2])*(p*i_0-h))
    x_3=X[2]*(1-X[2])*(X[0]*X[1]*(f+p*l_0+d)+X[0]*(1-X[1])*(f-m+p*l_0+d)+(1-X[0])*X[1]*p*l_0+(1-X[0])*(1-X[1])*(0-m+p*l_0))
    for i in [x_1,x_2,x_3]:
        if i<0:
            i=0
        elif i>1:
            i=1

    dX=[x_1,
         x_2,
         x_3]
    return dX
solve=[[ 0,  1,  0],[  1,  1,  0],[ 0,  1,  1],[  1,  1,  1],[  1,  j_0*v/(j_0*w+c+e-h),  1],[  0,  -i_0*v/(-i_0*w+h),  0],[  0,  -j_0*v/(-j_0*w+h),  1]]
solve_modify=[[  0,  1,  0],
              [  1,  1,  0],
              [  0 , w*v*i_0/h,0],
              [  0,  1,  1],
              [  0,  w*v*j_0/h,  1],
              [1, 1,1]]

dt=0.1
t_range = [0,3]
t_step = 0.001
X_0=[0.96,1,1]
t_euler, x_euler = ode.euler(
        dfun=fy,
        xzero=X_0,
        timerange=t_range,
        timestep=t_step,
        )
X=np.array(x_euler)
T=np.array(t_euler)
variable=['The ratio of government regulators to monitoring','The ratio of total contracting to safe investmentratio state safety of supervise','ratio state safety of supervise']

def simulite(k,fy):

    t_euler, x_euler = ode.euler(
            dfun=fy,
            xzero=k,
            timerange=t_range,
            timestep=t_step,)
    return x_euler

def diff(k):

    vv=copy.deepcopy(k)
    for i in range(3):
        if vv[i]==1:
            vv[i]=vv[i]-dt
        else:
            vv[i]=vv[i]+dt
    return vv

def diff_result(k):
    ww=copy.deepcopy(k)
    result=np.array([ww[:],ww[:],ww[:]],dtype='float')
    vv=np.array(diff(k))
    for i in range(3):
        result[i,i]=vv[i]
    return result

def fig(T,X,titles,figname):
    variable=titles

    plt.figure(figsize=[30,18])
    for i in range(3):
        ax=plt.subplot(3,1,i+1)
        ax.plot(T, X[i,:,0],'r--',T, X[i,:,1],'b*',T, X[i,:,2],'g^')
        ax.set(xlabel='Time step', ylabel='proportion',
               title='{a} has change, the corresponding changes of other'.format(a=variable[i]))
        plt.legend(labels=variable,loc='best', fancybox=True,markerscale=0.2)



    plt.savefig('{a}.jpg'.format(a=figname),dpi=500)
    plt.show()
def sim(Solve,s,fy):
    for i in range(len(Solve)):
        result=diff_result(Solve[i]).tolist()
        wwww=[0,0,0]
        for j in range(3):
            wwww[j]=simulite(result[j],fy)
        wwwww=np.array(wwww)
        fig(T,wwwww,variable,'this is {b} {a}'.format(a=str(Solve[i]),b=s))




sample=np.random.random((100,3))
def sim_random(sample,func):
    result=[]
    for i in range(sample.shape[0]):
        result.append(simulite(sample[i],func))
    return result

jjjj=np.array(sim_random(sample,fy))
gggg=np.array(sim_random(sample,fz))
first_1=jjjj[:,0,:]
end_1=jjjj[:,3000,:]
first_2=gggg[:,0,:]
end_2=gggg[:,3000,:]
plt.figure(figsize=[30,18])
ax1=plt.subplot(2,1,1)
yy_1=ax1.hist(end_1)
ax1.set(xlabel='proportion',ylabel='persention',title='modify modle')
plt.legend(labels=variable,loc='best')
ax2=plt.subplot(2,1,2)
yy_2=ax2.hist(end_2)
ax2.set(xlabel='proportion',ylabel='persention',title='modify modle')
plt.legend(labels=variable,loc='best')
plt.savefig('compilt.png',dpi=500)
plt.show()













































