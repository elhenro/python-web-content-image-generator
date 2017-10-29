# $ python3 main.py 'Der Titel' https://url.com
import sys
import os  # for os line breaks and bash
from lxml import html  # for reading dom
import requests  # for web action
from shutil import copyfile  # for file operations
import datetime  # for generating timestamp
from PIL import Image, ImageOps  # for image resize and crop
import subprocess  # for running shell scripts

TimeNow = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
item_title = (sys.argv[1])
item_url = (sys.argv[2])
kleinb = item_title.lower()

kleinbdash = kleinb.replace(' ', '-').lower()
jpegFileName = kleinbdash + '.jpg'  # TODO: Umlaute
heroName = 'hero_'+jpegFileName
print (jpegFileName)

# log function
def logger ( entry ) :
    # print ( entry )  # debug
    f = open('log/log.txt', 'r+')
    f.read()
    f.write(entry + "\n")
    f.close()
    return

#log input
input_entry = TimeNow + ' got input: ' + item_title + '  Url: ' + item_url
logger(input_entry)

# log Title and filename
name_entry = TimeNow + ' generating filename: '+ jpegFileName + ' from title: ' + item_title
logger(name_entry)

# read website
page = requests.get(item_url)
tree = html.fromstring(page.content)
author = ''.join(tree.xpath('//h3[@class="mini-profile__name"]//a/text()'))
print ('Author: ', author)

# write author to log
author_entry = TimeNow + ' got Author: ' + author
logger(author_entry)

# get download link
page = requests.get(item_url)
webpage = html.fromstring(page.content)
downloadurl = webpage.xpath('//div[@class="image-section__sidebar"]//div[@class="box box--no-margin-bottom"]//div[@class="btn-primary btn--lg btn--splitted"]/a/@href')
imagelink = ''.join(downloadurl)
print ('Image Download Link: ' + imagelink)

# download image
print ('Downloading...')
f = open('workbench/' + jpegFileName, 'wb')
f.write(requests.get(imagelink).content)
f.close()
logger(TimeNow + ' Download of ' + imagelink + ' Successful.')
# copy image for hero
# call(["bash", "cp workbench/"+jpegFileName+' workbench_hero/'+heroName])
copyfile('workbench/'+jpegFileName, 'workbench_hero/'+heroName)

# crop image
print ('Generating Images...')
import PIL  # import python-imaging
img = Image.open('workbench/'+jpegFileName)  # read image
# large image
img = img.resize((1000, 600), Image.ANTIALIAS)
img.save('data/large/'+jpegFileName)  # save down large image
# medium image
img = img.resize((600, 400), Image.ANTIALIAS)
img.save('data/medium/'+jpegFileName)  # save down large image
# small image
img = img.resize((300, 180), Image.ANTIALIAS)
img.save('data/small/'+jpegFileName)  # save down large image
# crop square image
thumb = ImageOps.fit(img, (100, 100), Image.ANTIALIAS)
# img = ImageOps.fit((100, 100), Image.ANTIALIAS)
thumb.save('data/square/'+jpegFileName)  # save down large image
print ('Images generated successful.')
logger(TimeNow + ' successfully resized and cropped large - square')

# HERO SECTION
logger('Starting hero-image production...')
# crop hero
img = Image.open('workbench_hero/' + heroName)  # read hero image
# img = img.resize((960, 250), Image.ANTIALIAS)  # resize
hero = ImageOps.fit(img, (960, 250), Image.ANTIALIAS)
hero.save('workbench_hero/' + heroName)  # save down hero image to workbench
logger(TimeNow + ' Starting shell script for CTA and Hero-image..')
proj_path = '/home/hnr/web/ci-generator/'
hero_path = proj_path + 'workbench_hero/' + heroName
# generate CTA from button.html and -.css and merge with hero
os.system('sh hero-generator.sh workbench_hero/' + heroName + ' "' + item_title + '" workbench_hero/' + heroName)

copyfile('workbench_hero/'+heroName, 'hero/large/'+heroName)

img = Image.open('workbench_hero/' + heroName)  # read hero image again (now with button)
# generate medium and small version
img = img.resize((500, 130), Image.ANTIALIAS) # resize
img.save('hero/medium/'+heroName)
img = img.resize((300, 78), Image.ANTIALIAS) # resize
img.save('hero/small/'+heroName)
