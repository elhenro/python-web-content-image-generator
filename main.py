# $ python3 main.py 'Der Titel' https://url.com
import sys
from lxml import html
import requests
import datetime
TimeNow = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
item_title = (sys.argv[1])
item_url = (sys.argv[2])
kleinb = item_title.lower()

kleinbdash = kleinb.replace(' ', '-').lower()
jpegFileName = kleinbdash + '.jpg'
print (jpegFileName)

f = open('log/main-log', 'w')
f.write(TimeNow + ' generating filename: '+ jpegFileName + ' from title: ' + item_title)
f.write("\n")
f.close() 
# read website
page = requests.get(item_url)
tree = html.fromstring(page.content)
author = ''.join(tree.xpath('//h3[@class="mini-profile__name"]//a/text()'))
print ('Author: ', author)
# write author to log
f = open('log/main-log', 'w')
f.write(TimeNow + ' got Author: ' + author + "\n")
f.write("\n")
f.close()
# get download link
page = requests.get(item_url)
webpage = html.fromstring(page.content)
downloadurl = webpage.xpath('//div[@class="image-section__sidebar"]//div[@class="box box--no-margin-bottom"]//div[@class="btn-primary btn--lg btn--splitted"]/a/@href')
imagelink = ''.join(downloadurl)
print ('Image Download Link: ' + imagelink)
# download image
f = open('workbench/'+jpegFileName, 'wb')
f.write(requests.get(imagelink).content)
f.close()
# crop image
import PIL  # import python-imaging
from PIL import Image
large = 999
medium = 600
small = 300
img = Image.open('workbench/'+jpegFileName)  # read image
# large image
wpercent = (small / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((small, hsize), PIL.Image.ANTIALIAS)
img.save('data/small/'+jpegFileName)  # save down small image

# small image
wpercent = (small / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((small, hsize), PIL.Image.ANTIALIAS)
img.save('data/small/'+jpegFileName)  # save down small image

