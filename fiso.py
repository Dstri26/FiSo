# -*- coding: utf-8 -*-
"""
Created on Fri May 29 14:52:25 2020

@author: DS
"""

import os
import shutil

''' Create a predefined list of extensions '''
img_extensions=['.jpg','.jfif','.jpeg','.png','.gif']
doc_extensions=['.txt','.docx','.xlsx','.pptx','.doc','.xls','.ppt','.pdf','.ods','.csv','.odt']
aud_extensions=['.mp3','.wav']
comp_extensions=['.zip','.7z','.rar']
exe_extensions=['.exe','.EXE','.msi']
vid_extensions=['.mp4','.avi','.webm','.mkv']



''' Separate Files in directory '''

img=[]
doc=[]
comp=[]
vid=[]
aud=[]
exe=[]
files_list=os.listdir('.')

#selected_dir=input("Enter the directory you want to manage:")
selected_dir=os.getcwd()
selected_dir = selected_dir.replace("\\", "/")

for file in files_list:
    for ext in img_extensions:
        if file.find(ext)>0:
            img.append(selected_dir+"/"+file)
    for ext in aud_extensions:
        if file.find(ext)>0:
            aud.append(selected_dir+"/"+file)
    for ext in doc_extensions:
        if file.find(ext)>0:
            doc.append(selected_dir+"/"+file)
    for ext in comp_extensions:
        if file.find(ext)>0:
            comp.append(selected_dir+"/"+file)
    for ext in vid_extensions:
        if file.find(ext)>0:
            vid.append(selected_dir+"/"+file)
    for ext in exe_extensions:
        if file.find(ext)>0:
            exe.append(selected_dir+"/"+file)
            
''' Create Directories for Different Files'''

img=set(img)
doc=set(doc)
vid=set(vid)
comp=set(comp)
aud=set(aud)
exe=set(exe)

if len(img)>0:
    if not os.path.isdir("Image_files"):
        os.mkdir("Image_files")
if len(doc)>0:
    if not os.path.isdir("Document_files"):
        os.mkdir("Document_files")
if len(comp)>0:
    if not os.path.isdir("Compressed_Files"):
        os.mkdir("Compressed_Files")
if len(vid)>0:
    if not os.path.isdir("Video_Files"):
        os.mkdir("Video_Files")
if len(aud)>0:
    if not os.path.isdir("Audio_Files"):
        os.mkdir("Audio_Files")
if len(exe)>0:
    if not os.path.isdir("Executable_Files"):
        os.mkdir("Executable_Files")    



'''Move Files to Respective Folders'''

for i in img:
    shutil.move(i,selected_dir+"/Image_files")
for i in doc:
    shutil.move(i,selected_dir+"/Document_files")
for i in comp:
    shutil.move(i,selected_dir+"/Compressed_files")
for i in vid:
    shutil.move(i,selected_dir+"/Video_files")
for i in aud:
    shutil.move(i,selected_dir+"/Audio_files")
for i in exe:
    shutil.move(i,selected_dir+"/Executable_files")


