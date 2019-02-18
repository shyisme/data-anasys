import pandas as pd
import requests
import json
import time
url="http://www.cpppc.org:8083/efmisweb/ppp/expertLibrary/getExpertList.do"
header={'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Mobile Safari/537.36'}
name="ppp专家.xlsx"

translate_reponse={'DIC_NAME':"行业类别",
'EXPRT_CODE':"EXPRT_CODE",
'EXPRT_ID':"EXPRT_ID",
'EXPRT_NAME':"姓名",
'GENDER':"性别",
'REMOTE_PATH':"猜测为入库时间",
'WORK_CMPNY':"所在单位"
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
    result_df.to_excel(writer,"专家")

collectdata=[]
for i in range(32):
    time.sleep(0.2)
    data={'queryPage': i}
    reponse=requests.post(url,data=data,headers=header)
    collectdata=collect_data(reponse)+collectdata


result_data=tranform_to_standard(collectdata)

storage(result_data,name)
