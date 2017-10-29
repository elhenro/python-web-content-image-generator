# $ python3 main.py 'Der Titel' https://url.com
import sys
import os
from lxml import html
import requests
import datetime
from PIL import Image, ImageOps

TimeNow = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
item_title = (sys.argv[1])
item_url = (sys.argv[2])
kleinb = item_title.lower()

kleinbdash = kleinb.replace(' ', '-').lower()
jpegFileName = kleinbdash + '.jpg'
print (jpegFileName)

# log function
def logger ( entry ) :
    f = open('log/log.txt', 'r+')
    f.read()
    f.write(entry + "\n")
    f.close()
    return

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
logfile = open('workbench/'+jpegFileName, 'wb')
logfile.write(requests.get(imagelink).content)
logfile.close()
print('Download successful.')
# TODO: Log download

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
# TODO: Log resized and cropped


