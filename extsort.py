#sort files according to their extensions. 
import os

def extsort(files):
    return sorted(files,key=lambda x: os.path.splitext(x)[1])

file = ['first.py','second.html','third.js','fourth.cpp','fifth.c']
newfile = extsort(file)
print(newfile)