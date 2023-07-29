
import os
import pandas as pd
currDirectory=os.getcwd()
# print(currDirectory)
try:
    def dictionaryOfFileNames(oldName,newName):
        dictionaryOfNames[oldName]=newName
    
    def findingAndRenaming(fileNames,currDirectory,dictionaryOfNames):
        errCnt=0
        for oldName in dictionaryOfNames:
            try:
                temp=oldName
                oldName=str(oldName)
                
                # print(type(oldName))
                oldName=oldName+".pdf"
                # print(oldName)
                index=fileNames.index(oldName)
                file=fileNames[index]
                (prevFileName,extension)=os.path.splitext(file)
                newFileNameWithExtension=str(dictionaryOfNames[temp])+extension
                oldFileRenameDir=os.path.join(currDirectory,oldName)
                newFileRenameDir=os.path.join(currDirectory,newFileNameWithExtension)
                # print(oldFileRenameDir)
                os.rename(oldFileRenameDir,newFileRenameDir)
                
            except ValueError as err:
                errCnt+=1
        print("Error count:",errCnt)
    
    FileName=input("Enter the filename with extension(only filename)")
    # FileName="book1.xlsx"
    fileDirectory=currDirectory+"/"+FileName
    # print(fileDirectory)
    data=pd.read_excel(fileDirectory)
    oldFileName=data.Old_filename
    newFileName=data.New_filename
    
    fileNames=[]
    cnt=0
    for file in os.listdir(currDirectory):
        if(file.endswith(".pdf") or file.endswith(".PDF")):
            fileNames.append(file)
            cnt+=1
    # print(cnt)
    
    dictmaker=map(dictionaryOfFileNames,oldFileName,newFileName)
    dictionaryOfNames={}
    list(dictmaker)
    findingAndRenaming(fileNames,currDirectory,dictionaryOfNames)
except FileNotFoundError as err:
    print("Entered file name is not in the program directory")