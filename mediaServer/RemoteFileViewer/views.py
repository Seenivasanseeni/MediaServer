from django.shortcuts import render
from django.http import HttpResponse
import os
from os.path import expanduser

def get_home():
    return expanduser("~")

def index(request):
    return render(request,'RemoteFileViewer/index.html')

def constructPath(dir):
    return os.path.join(get_home(),dir)

def get_content_type(dir):
    return "application/"+dir.split('.')[-1]

def getOnlydirectories(path,dirs):
    dirs_=[]
    for dir in dirs:
        dir_=os.path.join(path,dir)
        if(os.path.isdir(dir_)):
            dirs_.append(dir)
    return dirs_

def removeHidden(dirs):
    dirs_=[]
    for dir  in dirs:
        if(len(dir)>0 and dir[0]!='.'):
            dirs_.append(dir)
    return dirs_

def get_file_name(dir):
    name= dir.split('/')[-1]
    return name.replace(" ","%20")

def explore(request,dir="."):
    path=constructPath(dir)
    try:
        dirs_i=os.listdir(path)
        dirs=removeHidden(dirs_i)
        dirsOnly=getOnlydirectories(path,dirs)
    except: # if dir is a file
        with open(constructPath(dir),'rb') as file:
            response=HttpResponse(file.read())
            response['content_type']=get_content_type(dir)
            response['Content-Disposition'] = 'attachment;filename='+get_file_name(dir);
            return response

    context={
        'path':path,
        'folder':dir,
        'dirsOnly':dirsOnly,
        'dirs':dirs
    }

    return render(request,'RemoteFileViewer/explorer.html',context=context) 