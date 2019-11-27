import  os

path = "D:\\Downloads\\PDFs\\"
prefix = "PDFs"


for filename in os.listdir(path):
    if(not filename == prefix):
        if(prefix in filename):
            newFileName = filename.split(prefix)
            print(newFileName[1])
            if(not os.path.exists(path + newFileName[1])):
                os.rename(path + filename, path + newFileName[1])
            else:
                os.remove(path + filename)