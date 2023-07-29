import pandas as pd
import os
import glob
import shutil
import face_recognition

#================functions area====================

def checker(dictionary,pic_directory,sign_directory):
    picsNotRenamed=[]
    signNotRenamed=[]
    extensions=[".jpeg",".jpg",".png",".JPEG",".JPG"]
    for picsName in dictionary:
        roll=dictionary.get(picsName)
        filteredRoll=roll.replace("GSBTM/01/2022/TCC/","")    
        picNotFoundCnt=0
        signNotFoundCnt=0
        for extension in extensions:
            if(not (os.path.exists(pic_directory+"/"+filteredRoll+extension))):
                picNotFoundCnt+=1
            if(not os.path.exists(sign_directory+"/"+filteredRoll+extension)):
                signNotFoundCnt+=1
        if(picNotFoundCnt==5):
            picsNotRenamed.append(filteredRoll)
        if(signNotFoundCnt==5):
            signNotRenamed.append(filteredRoll)
    print("pics not found:",picsNotRenamed)
    print("total pics not found:",len(picsNotRenamed))
    print("sign not found:",signNotRenamed)
    print("total sign not found:",len(signNotRenamed))
    df=pd.DataFrame()
    df['Pics Problems RollNum']=pd.DataFrame(picsNotRenamed)
    df['Signs Problems RollNum']=pd.DataFrame(signNotRenamed)
    
    
    # print(type(df))
    df.to_excel("Pics And Signs Not Found.xlsx",index=False)
    print("")
    print("===============================================================")
    print("NOTE: A EXCEL FILE HAS CREATED FOR PICS AND SIGN ERROR PLEASE CHECK BOTH IF ANY ERROR FOUND IN PICS")
    
    
    
def renamer(emailList,ApplicantList,pic_directory,sign_directory,dictionary):
    imagesList=os.listdir(pic_directory)
    signList=os.listdir(sign_directory)
    renamingErrCnt=0
    # images renaming
    for email in dictionary:
        # print(email)
        
        for image in imagesList:
            if(image.find(email) != -1):
                roll=dictionary.get(email)
                # print(roll)
                filteredRoll=roll.replace("GSBTM/01/2022/TCC/","")     
                # print(filteredRoll)
                (fileName,extension)=os.path.splitext(image)
                # print(extension)
                try:
                    newName=filteredRoll+extension
                    oldFile=os.path.join(pic_directory,image)
                    newFile=os.path.join(pic_directory,newName)
                    os.rename(oldFile,newFile)
                except FileExistsError as err:
                   renamingErrCnt+=1
        
    print("renaming errors in pics",renamingErrCnt)
    renamingErrCnt=0
    # sign renamaing
    for email in dictionary:
        # print(email)
        
        for sign in signList:
            if(sign.find(email) != -1):
                roll=dictionary.get(email)
                # print(roll)
                filteredRoll=roll.replace("GSBTM/01/2022/TCC/","")     
                # print(filteredRoll)
                (fileName,extension)=os.path.splitext(image)
                # print(extension)
                try:
                    newName=filteredRoll+extension
                    oldFile=os.path.join(sign_directory,sign)
                    newFile=os.path.join(sign_directory,newName)
                    os.rename(oldFile,newFile)
                except FileExistsError as err:
                   renamingErrCnt+=1
    print("renaming errors in signs ",renamingErrCnt)
    
        
def signatureSorter(imagesName,dataDirectory,sign_directory):
    percentage=100/len(emailList)
    compPercent=0
    for image in imagesName:
        try: 
            if((os.path.getsize(dataDirectory+"/"+image)/1024)<17 and not(os.path.exists(sign_directory+"/"+image))):
                for jpegfile in glob.iglob(os.path.join(dataDirectory,image)):
                    shutil.move(jpegfile,sign_directory)
                    compPercent+=percentage
                print(compPercent,"% signed moved")
        except Exception as exc:
            print("error in sign")
        
def ImageSorter(imagesName,dataDirectory,pic_directory):
    percentage=100/len(emailList)
    compPercent=0
    for image in imagesName:
        try:
            if((os.path.getsize(dataDirectory+"/"+image)/1024)<17 and not(os.path.exists(pic_directory+"/"+image))):
                imageName = face_recognition.load_image_file(dataDirectory+"/"+image)
                face_locations = face_recognition.face_locations(imageName)
                if(len(face_locations)>=1):
                        
                        for jpegFile in glob.iglob(os.path.join(dataDirectory,image)):
                            shutil.move(jpegFile,pic_directory)
                            compPercent+=percentage
                        print(compPercent,"% pics moved")
        except Exception as err:
            print(err)
                
        
def dictionaryOfData(emailD,applicantD):
    dictionary[emailD]=applicantD
    
# functions area end

# ====Directory code====

curr_directory=os.getcwd()
print(curr_directory)
pic_directory=os.path.join(curr_directory,r"All_data//images")
sign_directory=os.path.join(curr_directory,r"All_data//signs")
if(not os.path.exists(pic_directory)):
    os.makedirs(pic_directory)
if(not os.path.exists(sign_directory)):
    os.makedirs(sign_directory)
    
# Directory code ended

# =====Reading data from file as dataframe =====

mainData=pd.read_excel("1GSBTM_recruitment_data.xlsx",index_col=None, na_values=['NA'], usecols="A,H")
emailList=list (mainData.email)
applicantList=list(mainData['Application No.'])
dictionary={}
dictMaker=map(dictionaryOfData,emailList,applicantList)
list(dictMaker)
#Reading logic ended

# ====getting all images name=====

dataDirectory=curr_directory+"//upload"
cnt=0
imagesName=[]
for image in os.listdir(dataDirectory):
    if(image.endswith(".jpeg") or image.endswith(".jpg") or image.endswith(".png") or image.endswith(".JPG") or image.endswith(".JPEG")):
        imagesName.append(image)
        cnt+=1
# images logic end

# ====function runners====

# ImageSorter(imagesName, dataDirectory, pic_directory)
# signatureSorter(imagesName, dataDirectory, sign_directory)
# renamer(emailList,applicantList,pic_directory,sign_directory,dictionary)
checker(dictionary, pic_directory, sign_directory)
# print(dictionary)

