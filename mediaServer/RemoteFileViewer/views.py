from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return render(request,'RemoteFileViewer/index.html')

def constructPath(dir):
    return "/home/seeni/"+str(dir)

def get_content_type(dir):
    return "application/"+dir.split('.')[-1]

def get_file_name(dir):
    name= dir.split('/')[-1]
    return name.replace(" ","%20")

def explore(request,dir="."):
    path=constructPath(dir)
    try:
        dirs=os.listdir(path)
    except: # if dir is a file
        with open(constructPath(dir),'rb') as file:
            response=HttpResponse(file.read())
            response['content_type']=get_content_type(dir)
            response['Content-Disposition'] = 'attachment;filename='+get_file_name(dir);
            return response
            
    context={
        'dir':dir,
        'dirs':dirs
    }
    return render(request,'RemoteFileViewer/explorer.html',context=context) 