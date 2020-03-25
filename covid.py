import requests
from bs4 import BeautifulSoup
import json

URL = 'https://www.sms4india.com/api/v1/sendCampaign'


# get request
def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

def getData(url):
    r=requests.get(url)
    return r.text


if __name__=="__main__":
    dat=getData('https://www.mohfw.gov.in/')  
    
    soup=BeautifulSoup(dat,'html.parser')
    myDatastr=""
    
    for tr in soup.find_all('tbody')[7].find_all('tr'):
        myDatastr+=tr.get_text()

myDatastr=myDatastr[1:]        

msg="Arbaz\nCorona Live Status:\n"
states=['Delhi','Uttar Pradesh']
itemlist=myDatastr.split("\n\n")
for item in itemlist[0:26]:
    datalist=item.split("\n")
    if datalist[1] in states:
        msg+=f"{datalist[1]} Cases:{datalist[2]} Death:{datalist[5]}\n"
        
no=int(input("Enter Your Number(without+91):"))
# get response
response = sendPostRequest(URL, 'MXB1G65252TFSD68KM9VMS23I0HOSH46', 'GXKK9U14SOB4SYH9', 'stage', no, 'SMSIND', msg )
"""
  Note:-
    you must provide apikey, secretkey, usetype, mobile, senderid and message values
    and then requst to api
"""
# print response if you want
print("\nSuccess!!!\nMade By Arbaz Alam") 
