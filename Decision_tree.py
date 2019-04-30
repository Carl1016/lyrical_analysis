
# coding: utf-8

# In[63]:


import os
import tarfile
import csv
from six.moves import urllib
import pandas as pd
Path = 'D:/header2.xlsx'
Data = pd.read_excel(Path,encoding = 'utf-8')
Data.head()


# In[64]:


from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
label = Data['漲跌']
label_encoded = encoder.fit_transform(label)
#零表平，1表漲，2表跌
Data['漲跌'] = label_encoded
Data.head()
"""x = Data[['工會','晶電','去年','英國','綠能','貿聯','脫歐','台燿','相關','康普','宏達電','每股','年增','創新高','罷工','新台幣','集團'
         ,'五日','開高','面板','收盤','塑化','合晶','央行','擴大','凌通','第四季','避險','新機','開低','趨勢','iphone','無法','手機'
         ,'eps','歐美','排列','中央社','日電','尾盤','區間','修正','創下','歷史','基金','景氣','減少','進行','工業','分析師','共識'
         ,'利率','權值','機率','led','低點','全年','億美','供應鏈','成本','業者','法說','近日','報告','本季','rsi','出口','高通'
         ,'衝擊','帶量','記憶體','家數','鏡頭','交易','應用','報價','盤勢','銷售','利空','陸續','隆達','日線','空間','零組件'
         ,'獲得','十日','市值','四大','貨幣','因素','攻上','高峰','認為','人民幣','雙雙','計畫','重要','日本','升溫','回檔','供需'
         ,'部份','站回','重新','商機','紡織','旗下','發表','疲弱','技術','股市部','台化','吸引','數據','將於','態度','翻黑','指標股'
         ,'強攻','啟動','引發','乖離','重點','之後','周四','漲近','南亞','小幅','攜手','緯創','力道','續創','出籠','持平','增溫','推薦'
         ,'券商','航線','新光金','揚明光','玉晶光','裕民','走強','集中','中鋼','貿易戰','漲價','兩岸','運輸'
]]"""
x = Data[['工會', '去年', '年增', '罷工', '中央社', '日電', '共識', '法說', '衝擊', '因素']]
x.head()


# In[65]:


y = Data['漲跌']
y.head()


# In[66]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3) 


# In[67]:


x_train.head()


# In[68]:


x_test.head()


# In[69]:


from sklearn.tree import DecisionTreeClassifier
DT_classifier = DecisionTreeClassifier(criterion = 'gini')
DT_classifier = DT_classifier.fit(x_train,y_train)
DT_predict = DT_classifier.predict(x_test)
print(DT_predict)
y_test.head()


# In[70]:


from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, DT_predict)
print('準確率:',accuracy)


# In[71]:


x.shape


# In[72]:


from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
selector = SelectKBest(chi2, k=10).fit(x,y)
selected_featurenames = x.columns[selector.get_support()]


# In[73]:


print(type(selected_featurenames))


# In[74]:


print(selected_featurenames)


# In[75]:


from sklearn import svm
SVM_clf = svm.SVC()
SVM_clf.fit(x_train,y_train)
result = SVM_clf.predict(x_test)
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, result)
print('準確率:',accuracy)


# In[76]:


from sklearn.metrics import classification_report
target_class = ['rise','fall']
print(classification_report(y_test, result,target_names = target_class))


# In[77]:


"""from sklearn.tree import export_graphviz
from sklearn import tree
from IPython.display import Image
import pydotplus
name = ['工會', '去年', '年增', '罷工', '中央社', '日電', '共識', '法說', '衝擊', '因素']
target = ['漲','跌']
dot_data = tree.export_graphviz(DT_classifier, out_file=None, 
                     feature_names=name,  
                     class_names= target,  
                     filled=True, rounded=True,  
                     special_characters=True)  
graph = pydotplus.graph_from_dot_data(dot_data)  """


# In[78]:


from sklearn.ensemble import RandomForestClassifier


# In[79]:


RFC = RandomForestClassifier(oob_score = False, random_state=10)
RFC.fit(x_train,y_train)


# In[80]:


RFC_result = RFC.predict(x_test)


# In[81]:


from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, RFC_result)
print('準確率:',accuracy)


# In[82]:


from sklearn.metrics import classification_report
target_class = ['rise','fall']
print(classification_report(y_test,RFC_result,target_names = target_class))

