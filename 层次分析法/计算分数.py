import pandas as pd
import numpy as np
from read_excel import k,first,rgb

weight=np.array(pd.read_excel("权重结果.xlsx",index_col=0,parse_cols='b:c'))

mark=pd.read_excel('打分.xlsx',sheetname=list(range(10)),skiprows=10,index_col=0,parse_cols='a:c')
mark_data=np.zeros((10,46,2))
grade=np.zeros((10,46,2))
transform={5:90,4:75,3:65,2:60,1:0}
#形成多维打分数据
for i in range(10):
    mark_data[i,:,:]=np.array(mark[i])


for i in range(10):
    for j in range(46):
        for m in range(2):
            grade[i,j,m]=transform[mark_data[i,j,m]]


#计算个人季度权重和。并将数据降维
grade_data=np.zeros((46,10))
def reason_weight(l):
    reason_weight_1=weight[k[first[l]]:k[first[l]+1]]
    reason_weight_2=reason_weight_1.T
    reason_weight_3=reason_weight_2.tolist()
    return reason_weight_3
for i in range(10):
    grade_data[:,i]=np.average(grade[i],axis=1,weights=reason_weight(3)[0])

#计算三级指标权重之和
third_count=first[3]-first[2]
third_rank_sum_weight=np.zeros((third_count,10))
for l in range(10):
    for i in range(third_count):
        forword_index=k[first[2]+i]
        next_index=k[first[2]+i+1]
        weight_index_0=weight[forword_index:next_index]
        weight_index=weight_index_0.reshape(weight_index_0.size)
        third_rank_sum_weight[i,l]=np.average(grade_data[(forword_index-first[3]+1):(next_index-first[3]+1),l],weights=weight_index)

#计算二级指标权重之和
secord_count=first[2]-first[1]
secord_rank_sum_weight=np.zeros((secord_count,10))
for l in range(10):
    for i in range(secord_count):
        forword_index=k[first[1]+i]
        next_index=k[first[1]+i+1]
        weight_index_0=weight[forword_index:next_index]
        weight_index=weight_index_0.reshape(weight_index_0.size)
        secord_rank_sum_weight[i,l]=np.average(third_rank_sum_weight[(forword_index-first[2]+1):(next_index-first[2]+1),l],weights=weight_index)

#计算以及指标权重
first_count=first[1]-first[0]
first_rank_sum_weight=np.zeros((first_count,10))
for l in range(10):
    for i in range(first_count):
        forword_index=k[first[0]+i]
        next_index=k[first[0]+i+1]
        weight_index_0=weight[forword_index:next_index]
        weight_index=weight_index_0.reshape(weight_index_0.size)
        first_rank_sum_weight[i,l]=np.average(secord_rank_sum_weight[(forword_index-first[1]+1):(next_index-first[1]+1),l],weights=weight_index)

resoult=np.mean(first_rank_sum_weight)

first_rank=pd.DataFrame(np.mean(first_rank_sum_weight,axis=1))
secord_rank=pd.DataFrame(np.mean(secord_rank_sum_weight,axis=1))
secord_rank.index=rgb[0:5]
third_rank=pd.DataFrame(np.mean(third_rank_sum_weight,axis=1))
third_rank.index=rgb[5:19]

sample_=np.mean(grade_data[0:4,:],axis=1)
sample=pd.DataFrame(sample_,index=['A11','A12','A13','A14'],columns=['得分'])

writer=pd.ExcelWriter('得分.xlsx')
first_rank.to_excel(writer,'最后得分')
secord_rank.to_excel(writer,'一级指标得分')
third_rank.to_excel(writer,'二级指标得分')
sample.to_excel(writer,'sample')
writer.save()
