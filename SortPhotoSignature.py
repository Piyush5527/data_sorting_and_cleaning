# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 18:33:22 2022

@author: Mahendrasinh Jadhav
"""
import os
import re
import pandas as pd
import shutil
os.chdir('E:\\PhotoAndSignature\\upload')
data = pd.read_csv("E:\\PhotoAndSignature\\GSBTM_recruitment_data.csv")



email = data.iloc[:,7:8].values.tolist()
print(type(email))

for (root,dirs,files) in os.walk('E:\\PhotoAndSignature\\upload', topdown=True):
    for j in email :
        for i in files :
            if re.search("^"+str(j)+".*jpg$", i) or re.search("^"+str(j)+".*jpeg$", i) or re.search("^"+str(j)+".*png$", i) :
                if (os.path.getsize(i)/1024) < 30 and not(os.path.exists('E:\\PhotoAndSignature\\upload\\PhotosAndSignature\\'+i)) :
                    shutil.move('E:\\PhotoAndSignature\\upload\\'+i, 'E:\\PhotoAndSignature\\upload\\PhotosAndSignature\\'+i)