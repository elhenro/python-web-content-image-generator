# $ python3 main.py 'Der Titel' https://url.com
# -*- coding: utf-8 -*-
import sys
import os  # for os line breaks and bash
from lxml import html  # for reading dom
import requests  # for web action
from shutil import copyfile  # for file operations
import datetime  # for generating timestamp
from PIL import Image, ImageOps  # for image resize and crop
import subprocess  # for running shell scripts# crop image
import PIL  # import python-imaging

filename = (sys.argv[1])

print ('Generating Images...')


img = Image.open('workbench/'+ filename)  # read image
# large image
img = img.resize((1000, 600), Image.ANTIALIAS)
img.save('data/large/'+ filename)  # save down large image
# medium image
img = img.resize((600, 400), Image.ANTIALIAS)
img.save('data/medium/'+ filename)  # save down large image
# small image
img = img.resize((300, 180), Image.ANTIALIAS)
img.save('data/small/'+ filename)  # save down large image
# crop square image
thumb = ImageOps.fit(img, (100, 100), Image.ANTIALIAS)
# img = ImageOps.fit((100, 100), Image.ANTIALIAS)
thumb.save('data/square/'+ filename)  # save down large image
print ('Images generated successful.')
#logger(TimeNow + ' successfully resized and cropped large - square')

