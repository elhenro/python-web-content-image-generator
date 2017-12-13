# $ python3 main.py 'Der Titel' https://url.com
# -*- coding: utf-8 -*-
import sys
import os  # for os line breaks and bash
from lxml import html  # for reading dom
import requests  # for web action
from shutil import copyfile  # for file operations
import datetime  # for generating timestamp
from PIL import Image, ImageOps  # for image resize and crop
import subprocess  # for running shell scripts

TimeNow = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
heroName = (sys.argv[1])

copyfile('workbench_hero/'+heroName, 'hero/large/'+heroName)
img = Image.open('workbench_hero/' + heroName)  # read image
#
# generate medium and small version
img = img.resize((500, 130), Image.ANTIALIAS) # resize
img.save('hero/medium/'+heroName)
img = img.resize((300, 78), Image.ANTIALIAS) # resize
img.save('hero/small/'+heroName)
print ('custom hero images produced')
