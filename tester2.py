import pandas as pd
mainData=pd.read_excel("GSBTM_recruitment_data.xlsx",index_col=None, na_values=['NA'], usecols="A,H")
emailList=list (mainData.email)
colName="Application No."
applicationData= list(mainData["Application No."])
print(applicationData)
