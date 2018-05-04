from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return render(request,'RemoteFileViewer/index.html')

def constructPath(dir):
    return "/home/seeni/"+str(dir)

def explore(request,dir="."):
    path=constructPath(dir)
    dirs=os.listdir(path)
    context={
        'dir':dir,
        'dirs':dirs
    }
    return render(request,'RemoteFileViewer/explorer.html',context=context)