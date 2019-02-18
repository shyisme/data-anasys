import numpy as np
import pandas as pd
zyx = np.array([[1, 3, 1/3, 3],
                [1/3, 1, 1/3, 1],
                [3, 3, 1, 3],
                [1/3, 1, 1/3, 1]])

xyz = np.array([[1,3],[1/3,1]])
def weight(compare_matric):
    a,b=np.linalg.eig(compare_matric) #计算特征值和特征向量
    weight=b[:,np.argmax(a)]/np.sum(b[:,np.argmax(a)])
    return weight

shy=weight(zyx)
yhs=weight(xyz)
shy=np.float16(shy)
yhs=np.float16(yhs)
love=pd.DataFrame(shy)
psy=pd.DataFrame(yhs)
write=pd.ExcelWriter("love.xlsx")
love.to_excel(write,"内部控制环境各指标权重")
psy.to_excel(write,"季度权重")