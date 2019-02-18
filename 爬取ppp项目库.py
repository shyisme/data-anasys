import pandas as pd
import requests
import json
import time
url="http://www.cpppc.org:8086/pppcentral/map/getPPPList.do"
header={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36'}
name="项目库.xlsx"

translate_reponse={'CODE_NAME': '项目示范级别',
'CREATING_UNAME': '举办单位',
 'DATABASE_NAME': '项目是否储备',
'ESTIMATE_COPER': '合作期限',
'CODE_NAME': '项目级别',
 'INVEST_COUNT': '项目总投资（万元）',
 'IVALUE': '所属行业',
 'IVALUE2': '所属行业子类',
 'LINK_TEL': '联系电话',
 'LINK_UNAME': '联系人',
 'LOCAL_LINKMAN': '本地联系人',
 'LOCAL_LINKTEL': '本地联系电话',
'OPERATE_MODE_NAME': '项目运作方式',
'PROJ_NAME': '项目名称 ',

'PROJ_RID': '项目url',
'PROJ_STATE_NAME': '项目所处阶段',
 'PROJ_SURVEY': '项目概况',
'PROJ_TYPE_NAME': '项目类型 ',
'PRV': '地区 ',
'RETURN_MODE_NAME': '回报机制',
'START_TIME': '项目开始时间',
'START_UNAME': '开始单位',
}
def collect_data(reponse):
    result=reponse.content
    result=result.decode(encoding="utf-8")
    #decode的作用是将其他编码的字符串转换成unicode编码
    result=json.loads(result)
    #把Json格式字符串解码转换成Python对象   json.loads()
    result_list=result['list']
    return result_list



def tranform_to_standard(result_list):
    result_data=[]
    for i in range(len(result_list)):
        result_data.append({})
        for j in translate_reponse.keys():
            result_data[i][translate_reponse[j]]=result_list[i][j]
    return result_data

def storage(result_data,name):
    writer=pd.ExcelWriter(name)
    result_df=pd.DataFrame(result_data)
    result_df.to_excel(writer,"项目库")

collectdata=[]
for i in range(948):
    time.sleep(0.2)
    data={'queryPage': i,"projStateType": 1}
    reponse=requests.post(url,data=data,headers=header)
    collectdata=collect_data(reponse)+collectdata


result_data=tranform_to_standard(collectdata)

storage(result_data,name)








