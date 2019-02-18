# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 09:24:58 2019

@author: 孙浩宇
"""


from tqdm import tqdm
import time

for i in tqdm(['happy','new','year']):
     time.sleep(1.5)
 # 对元祖类型可行
for i in tqdm(('happy','new','year')):
     time.sleep(1.5)
# 字典类型可行
for i in tqdm({'year':2019,'month':1,'day':3}):
    time.sleep(1.5)