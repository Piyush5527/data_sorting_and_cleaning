import pandas as pd

data=pd.read_csv('OMR_rollnum.csv')
rows,cols=data.shape
histData=data.copy()
data=data.fillna(0)
# print(data)
constraints=['a','b','c','d','e','f','g','h','i','j','k','l','m']

def createNewCsv(updatedData):
    try:
        updatedData.to_csv('RollCalculated.csv',index=False)
    except PermissionError as err:
        print("File opened in a window please close it Or its write protected")
        
    
def generateRollNum(row,cols,vals,loopings):
    roll="'"
    for j in range(loopings):
        for i in range(0,len(vals)):
             vals[i]=vals[i].replace('|','')
             if(vals[i].find(constraints[j]) != -1):
                 roll=roll+str(cols[i]-1)
    histData.roll[row]=roll
    print(roll)
    
# starting point of the logic
    
if(rows>=0 or cols>0):
    for i in range(0,rows):
        colsIndexes=[]
        Vals=[]
        constraints_looping=0
        # temp_cnt=0
        for j in range(0,cols):
            if(data.iloc[i][j] != 0):
                colsIndexes.append(j)
                constraints_looping=constraints_looping+len(data.iloc[i][j].replace('|',''))
                Vals.append(data.iloc[i][j])
        generateRollNum(i,colsIndexes,Vals,constraints_looping)
# for sending data to the file
createNewCsv(histData)
    
       