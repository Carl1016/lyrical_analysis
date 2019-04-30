
# coding: utf-8

# In[2]:


import os
import tarfile
import csv
from six.moves import urllib
import pandas as pd
import codecs
Path = "D:/台科課堂/數位金融創新服務/label.csv"
def open_csvfile(path): 
    List = []
    with open (Path,'r',encoding = 'utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for i in reader:
            List.append(i)
        return List


# In[3]:


csv_list = open_csvfile(Path)
for x in csv_list:
    print(x)
#csv_list為含有整個csv的Dictlist
#csv_list中一筆資料即一列(row)
news_fall_list = ['工會','晶電','去年','英國','綠能','貿聯','脫歐','台燿','相關','康普','宏達電','每股','年增',
                  '創新高','罷工','新台幣','集團','五日','開高','面板','收盤','塑化','合晶','央行'
                  ,'擴大','凌通','第四季','避險','新機','開低','趨勢','iphone','無法','手機','eps','歐美','排列','中央社','日電'
                  ,'尾盤','區間','修正','創下','歷史','基金','景氣','減少','進行','工業','分析師','共識','利率','權值','機率','led'
                  ,'低點','全年','億美','供應鏈','成本','業者','法說','近日','報告','本季','rsi','出口','高通','衝擊','帶量','記憶體'
                  ,'家數','鏡頭','交易','應用','報價','盤勢','銷售','利空','陸續','隆達','日線','空間','零組件','獲得','十日','市值'
                  ,'四大','貨幣','因素','攻上','高峰','認為','人民幣','雙雙','計畫','重要','日本','升溫','回檔','供需','部份','站回'
                  ,'重新','商機','紡織','旗下','發表','疲弱','技術','股市部','台化','吸引','數據','將於','態度','翻黑','指標股','強攻'
                  ,'啟動','引發','乖離','重點','之後','周四','漲近','南亞','小幅','攜手','緯創','力道','續創','出籠','持平','增溫']
print(len(news_fall_list))


# In[53]:


def write_csvfile(Path,lst):
    #lst為一二維list
    f = codecs.open(Path,'w','utf_8_sig')
    writer = csv.writer(f)
    print(len(lst))
    for row in lst:
        writer.writerow(row)
#write_csvfile('D:/newsfall_header.csv',news_fall_list)


# In[54]:



all_row =[]
for row in csv_list:
    one_row = []
    content = row['content']
    for keyword in news_fall_list:
        if keyword in content:
            one_row.append(1)
        else:
            one_row.append(0)
    all_row.append(one_row)
print(len(all_row))


# In[55]:


result = []
result.append(news_fall_list)
for i in all_row:
    result.append(i)
print(len(result))
write_csvfile('D:/newsfall_header.csv',result)

