# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:18:22 2018

@author: shy
"""

import pandas as pd
import requests
from lxml import etree
import json
import time
import re
link=pd.read_excel("ppp专家.xlsx",usecols="A,B,C,D")
link['email']='未提供'


def catch_email(expertId,name):
    url="http://www.cpppc.org:8083/efmisweb/ppp/expertLibrary/getExpetInfo.do?expertId={a}&expertCode=dengbing".format(a=expertId)
    header={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36'}

    reponse=requests.get(url,headers=header)
    time.sleep(3)
    result=reponse.text
    with open(".\expert\{a}.html".format(a=name),'w',encoding='utf-8') as f:
        f.writelines(result)
        f.close()
    email=re.findall('>[0-9a-zA-Z_.-]{0,19}@[0-9a-zA-Z_.-]{1,13}<',result)
    return email

for index in link.index:
    link.loc[index,'email']=catch_email(link.loc[index,'EXPRT_ID'],link.loc[index,'姓名'])

writer=pd.ExcelWriter("专家邮箱.xlsx")
link.to_excel(writer,"email")


