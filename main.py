import os
import re
import time


currentPath = "D:\\Downloads\\"
currentLenght = 0
prevLength = 0

regexAndFolders = {
    "(.*)\.(jpg|JPG)" : "Images",
    "(.*)\.jpeg" : "Images",
    "(.*)\.png" : "Images",
    "(.*)\.zip" : "Zip archives",
    "(.*)\.rar" : "Rar archives",
    "(.*)\.(mov|MOV)" : "Videos",
    "(.*)\.(mp4|MP4)" : "Videos",
    "(.*)\.(mp3|MP3)" : "Music",
    "(.*)\.pdf" : "PDFs",
    "(.*)\.exe" : "Executables",
    "(.*)\.torrent" : "Torrents",
    "(.*)\.docx" : "Words",
    "(.*)\.(doc|odt)" : "Words",
    "(.*)\.pps" : "Powerpoints",
    "(.*)\.xlsx" : "Excell",
    "(.*)\.ppt" : "Powerpoints",
    "(.*)\.iso" : "ISOs",
    "(.*)\.txt" : "Txt files",
    "(.*)\.mkv" : "Videos",
    "(.*)\.(java|class|py|bin|dll|js|php|c|cpp|c)" : "Code"
}



def matches(pattern, fileName):
    pattern = re.compile(pattern)

    if(re.match(pattern, fileName)):
        return True

    return False


def returnDirectoryForFile(fileName: str):

    for regexKey in regexAndFolders:

        if(matches(regexKey, fileName)):
            return regexAndFolders[regexKey]

    return "Misc"





def initDirs(path):
    for dirName in regexAndFolders.values():
        if(not os.path.isdir(path + dirName)):
            os.mkdir(path + dirName)

def init():
    if(os.path.isfile(os.getcwd() + "/config.txt")):
        config = open("config.txt")
        data = config.read()
        print(data)
        prevLength = int(data)

    else:
        f = open("config.txt", "w")
        f.close()

initDirs(currentPath)
init()

while 1:

    currentLenght = len(os.listdir(currentPath))
    print("running")

    if(currentLenght != prevLength):
        f = open("config.txt", "w")
        f.write(str(currentLenght))
        f.close()
        for filename in os.listdir(currentPath):

            if (not os.path.isdir(currentPath + filename)):
                print(currentPath + filename + " ----> " + currentPath + returnDirectoryForFile(filename) + "\\" + filename)
                os.rename(currentPath + filename, currentPath + returnDirectoryForFile(filename) + "\\" + filename)

    time.sleep(60)