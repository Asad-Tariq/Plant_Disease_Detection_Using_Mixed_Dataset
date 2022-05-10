#!/usr/bin/python
from PIL import Image
import os, sys

path = "/home/at05439/Documents/test/tomato_septoria_leaf_spot/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
    print("DONE")
resize()