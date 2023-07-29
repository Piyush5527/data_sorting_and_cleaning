import os

curr_directory=os.getcwd()
print(curr_directory)
pic_directory=os.path.join(curr_directory,r"All_data//images")
sign_directory=os.path.join(curr_directory,r"All_data//signs")
if(not os.path.exists(pic_directory)):
    os.makedirs(pic_directory)
if(not os.path.exists(sign_directory)):
    os.makedirs(sign_directory)
