# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 09:23:28 2017

@autGor: sGy
"""

import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pylab as plt
import scipy as sp
#数据准备，读取转换
p=7
n=20
d_p=pd.read_excel('data.xls',[0,1,2,3,4,5,6],header=0,index_col=0)
D_p=np.arange(p*n*n).reshape(p,n,n)
d=np.arange(p*3*n*n,dtype='float').reshape(p,3,n,n)
for i in d_p:
    D_p[i]=np.array(d_p[i].values)

transform={0:[0,0,0],1:[0,0,0.25],2:[0,0.25,0.5],3:[0.25,0.5,0.75],4:[0.5,0.75,1],5:[0.75,1,1]}
for l in range(7):
    for m in range(20):
        for n in range(20):
            for k in range(3):
                d[l][k][m][n]=transform[D_p[l][m][n]][k]

#三角模糊
'''
step1 标准化三角模糊数
'''
l=d[:,0,:,:]
m=d[:,1,:,:]
r=d[:,2,:,:]
d_max_k=d.max(axis=0)
d_min_k=d.min(axis=0)
max_min=d_max_k[2]-d_min_k[0]
D=(d-d_min_k)/max_min
'''
step2 计算左右限值
'''
a=D[:,0,:,:]
b=D[:,1,:,:]
c=D[:,2,:,:]
u=b/(1+b-a)
v=c/(1+c-b)

'''
step3 计算标准化总值
'''
w=(u*(1-u)+v**2)/(1-u+v)

'''
step4 计算K专家的三角模糊判断精确值
'''

t=d_min_k[0]+w*max_min

'''
step5 计算P位专家评价后的标准化精确值
'''

T=t.mean(axis=0)

'''
step6 确定风险因素模糊直接关系矩阵
'''
for i in range(n):
    T[i, i] = 0

'''
step7 确定截矩阵
'''
n = 20
limit = 0.5
M = np.arange(n*n).reshape(n, n)
for i in range(n):
    for j in range(n):
        if T[i][j]>=limit:
            M[i][j]=1
        else:
            M[i][j]=0


for i in range(n):
    M[i,i]=1


'''
step8 计算可达矩阵
'''
L=np.matrix(M)

n=20
for i in range(2,n+1):
    K=L+L**i

K[K>1]=1
K[K<0]=1
#数据保存
k=np.array(K)
K=k


FXYS=pd.DataFrame(T)
JZ=pd.DataFrame(M)
KD=pd.DataFrame(k)

G=nx.from_numpy_matrix(K)
writer=pd.ExcelWriter('save_excel.xlsx')
FXYS.to_excel(writer,'风险因素模糊直接关系矩阵')
JZ.to_excel(writer,'截矩阵')
KD.to_excel(writer,'可达矩阵')
writer.save()

#数据的可视化
plt.figure()
pos=nx.spring_layout(G)

nx.draw_networkx_nodes(G,pos)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos)
nx.draw_networkx_edge_labels(G,pos,font_size=5)

plt.show()






