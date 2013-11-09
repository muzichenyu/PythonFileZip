#!/usr/bin/python
# Filename: filecopy.py 
import zipfile
import time
import os
def addfoldertozip(folder,myzipfile):
    for filename in os.listdir(folder):
        subpath=os.path.join(folder,filename)
        if os.path.isfile(subpath):
            myzipfile.write(subpath)
        elif os.path.isdir(subpath):
            addfoldertozip(subpath,myzipfile)
        else:
            raise TypeError("非法文件类型")
source ='E:\\eclipse'
target_dir='E:\\'
target=target_dir+time.strftime('%Y%m%d')+'.zip'
myzipfile=zipfile.ZipFile(target,'w')
addfoldertozip(source,myzipfile)
myzipfile.close()

raw_input("Press enter key to close this window")