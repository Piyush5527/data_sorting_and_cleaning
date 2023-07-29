 

import os

examName=input("Enter the Exam name that is used to rename :")

if(examName == ""):
    print("Exam name Can't be empty")
    
else:
    try:
        directory=input("Enter the Directory path :")
        # os.listdir(directory)
        
        # cnt=len([name for name in os.listdir(directory) if os.path.isfile(name)])
        # print (len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name)) and name.endswith(".pdf")]))
        cnt= len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name)) and name.endswith(".pdf")])
        print("Total {} files found in given location".format(cnt))
        print("Starting Renaming files")
        progressStep=100/cnt
        progress=0
        for file in os.listdir(directory):
            if(file.endswith(".pdf")):
                try:
                    oldFileNameDirectory=os.path.join(directory,file)
                    newFileNameDirectory=os.path.join(directory,examName+"_"+file)
                    os.rename(oldFileNameDirectory,newFileNameDirectory)
                    progress+=progressStep
                    print("{}% completed".format(progress))
                except Exception as ex:
                    print("Error in renaming {}".format(file))
        
    except FileNotFoundError as err:
        print("Invalid Directory Name")