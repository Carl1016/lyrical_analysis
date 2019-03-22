
# coding: utf-8

# In[13]:


import os
import tarfile
from six.moves import urllib
import pandas as pd
Path = "./out_news.csv"
Data = pd.read_csv(Path)
Content = Data['content']

import jieba,math
import jieba.analyse
keyword = ''
for x in (Content):
    a=jieba.analyse.extract_tags(x, topK = 5, withWeight = False, allowPOS = ())
    print (a)
    for string in (a):
        keyword = keyword+string

result=jieba.analyse.extract_tags(keyword, topK = 5, withWeight = False, allowPOS = ())
print("overall-result:",result)

