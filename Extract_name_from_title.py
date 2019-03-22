
# coding: utf-8

# In[22]:


import os
import tarfile
from six.moves import urllib
import pandas as pd
Path = "./news.csv"
Company_Name = '華航'
Output_Path = "D:/out_news.csv"
Data = pd.read_csv(Path)
Huahang = Data['title'].str.contains(Company_Name)
Data[Huahang].to_csv(Output_Path,encoding = 'utf_8_sig')

