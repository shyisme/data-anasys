import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
#读取数据
data_raw=pd.read_excel("求权重调查问卷修改.xlsx",
                       sheetname=1,
                       skiprows=5,
                       index_col=0,
                       parse_cols="A:L")

rgb=np.array(data_raw['项目'])

index=[   '内部控制',       '内部控制',       '内部控制',       '内部控制',      '内部控制',  '内部控制环境',
              '内部控制环境',        '内部控制环境',        '内部控制环境', '风险识别与评估',       '风险识别与评估',    '控制活动',
             '控制活动',       '控制活动', '信息交流与反馈',       '信息交流与反馈',       '信息交流与反馈',  '内部控股监督',
             '内部控股监督',    '组织机构',       '组织机构',       '组织机构',       '组织机构',  '内部控制目标',
             '内部控制目标',       '内部控制目标',   '农商行文化',       '农商行文化',    '人力资源',       '人力资源',
             '人力资源',    '风险识别',       '风险识别',       '风险识别',    '风险评估',       '风险评估',
             '风险评估', '存款及柜台业务',       '存款及柜台业务',       '存款及柜台业务',       '存款及柜台业务',    '贷款业务',
              '贷款业务',        '贷款业务',        '贷款业务',       '贷款业务',    '中间业务',      '中间业务',
             '中间业务',   '交流与沟通',      '交流与沟通' ,   '信息系统',       '信息系统',    '信息反馈',
             '信息反馈',       '信息反馈',    '自我监督',       '自我监督',      '自我监督',    '内部审计',
             '内部审计',      '内部审计',  '整体内部控制',       '整体内部控制']
data_raw.index=index
#用data来存放主要数据
data=np.array(data_raw)
#用result存放结果
result=np.zeros((64,10))

#确定层次结构
data_tree={'A':{'A1':{'A11','A12','A13','A14'},
        'A2':{'A21','A22','A23'},
        'A3':{'A31','A32'},
        'A4':{'A41','A42','A43'}},
   'B':{'B1':{'B11','B12','B13'},
        'B2':{'B21','B22','B23'}},
   'C':{'C1':{'C11','C12','C13','C14'},
        'C2':{'C21','C22','C23','C24','C25'},
        'C3':{'C31','C32','C33'}},
   'D':{'D1':{'D21','D22'},
        'D2':{'D21','D22'},
        'D3':{'D31','D32','D33'}},
   'E':{'E1':{'E11','E12','E13'},
        'E2':{'E21','E22','E23'}}}
G=nx.Graph(data_tree)
G.add_node('M')
G.add_edges_from([('M','A'),('M','B'),('M','C'),('M','D'),('M','E')])
nx.from_dict_of_dicts


#coralation是各个层级的结构
coralation=[[5],
            [4],
            [2],
            [3],
            [3],
            [2],
            [4,3,2,3],
            [3,3],
            [4,5,3],
            [2,2,3],
            [3,3],
            [2]]
#第一层结构
first=[0,1,6,20]
#k是矩阵的索引值
k=[0]
number=0
for i in coralation:
    for j in i:
        number=number+j
        k.append(number)
#将比较关系转换为数值的字典
transform={0:1,1:3,2:5,3:7,4:9,-1:1/3,-2:1/5,-3:1/7,-4:1/9}

#获取评分，求出价值判断矩阵
def convert_compare_matric(k):
    compare_matric=np.zeros((k.size,k.size))
    for i in range(k.size):
        for j in range(k.size):
            compare_matric[i,j]=transform[k[i]-k[j]]
    return compare_matric

#求解权重
def weight(compare_matric):
    a,b=np.linalg.eig(compare_matric) #计算特征值和特征向量
    weight=b[:,np.argmax(a)]/np.sum(b[:,np.argmax(a)])
    return weight

#进行系数求解
for i in range(10):
    for j in range(21):
        result[k[j]:k[j+1],i]=weight(convert_compare_matric(data[k[j]:k[j+1],i+1]))

sample_resolt=np.zeros((4,4,10))
for i in range(10):
    sample_resolt[:,:,i]=convert_compare_matric(data[19:23,i+1])

sample=np.mean(sample_resolt,axis=2)
#求解权重平均值
weight_mean=np.mean(result,axis=1)


shy=pd.DataFrame(data_raw['项目'],index=index)
shy['权重']=weight_mean

index_sample=['A11','A12','A13','A14']
sample_first=pd.DataFrame(sample,index=index_sample,columns=index_sample)
sample_first['权重']=weight_mean[19:23]


writer=pd.ExcelWriter('权重结果.xlsx')
shy.to_excel(writer,'weight')
sample_first.to_excel(writer,'sample')
writer.save()
