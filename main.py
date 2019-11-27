import sys
import os
import shutil
import re

currentPath = "D:\\Downloads\\"


regexAndFolders = {
    "(.*)\.jpg" : "Images",
    "(.*)\.png" : "Images",
    "(.*)\.zip" : "Zip archives",
    "(.*)\.rar" : "Rar archives",
    "(.*)\.mov" : "Videos",
    "(.*)\.mp4" : "Videos",
    "(.*)\.mp3" : "Music",
    "(.*)\.pdf" : "PDFs",
    "(.*)\.exe" : "Executables",
    "(.*)\.torrent" : "Torrents",
    "(.*)\.docx" : "Words",
    "(.*)\.ppt" : "Powerpoints",
    "(.*)\.iso" : "ISOs"
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


initDirs(currentPath)


for filename in os.listdir(currentPath):
    shutil.move(currentPath + filename, currentPath + returnDirectoryForFile(filename) + "\\" + filename)