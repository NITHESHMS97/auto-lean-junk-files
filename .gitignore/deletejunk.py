import os
dirPath="C:\\Users\\Nithesh M S\\AppData\\Local\\Temp"
print(os.getcwd())
fileList=os.listdir(dirPath)

for file in fileList:
    try:
#        print(file)
        if(os.path.isfile(dirPath+"\\"+file)):
            os.remove(dirPath+"\\"+file)
        elif(os.path.isdir(dirPath+"\\"+file)):
            os.rmdir(dirPath+"\\"+file)
    except Exception as e:
        print(e)
