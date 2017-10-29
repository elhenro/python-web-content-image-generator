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
print ('Downloading...')
f = open('workbench/'+jpegFileName, 'wb')
f.write(requests.get(imagelink).content)
f.close()
print('Download successful.')
# crop image
print ('Generating Images...')
import PIL  # import python-imaging
from PIL import Image
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
from PIL import Image, ImageOps
thumb = ImageOps.fit(img, (100, 100), Image.ANTIALIAS)
# img = ImageOps.fit((100, 100), Image.ANTIALIAS)
thumb.save('data/square/'+jpegFileName)  # save down large image
print ('Images generated successful.')

#
# img = img.resize((large, hsize), PIL.Image.ANTIALIAS)
# img.save('data/large/'+jpegFileName)  # save down small image
# #medium image
# wpercent = (medium / float(img.size[0]))
# hsize = int((float(img.size[1]) * float(wpercent)))
# img = img.resize((medium, hsize), PIL.Image.ANTIALIAS)
# img.save('data/medium/'+jpegFileName)  # save down small image
# # small image
# wpercent = (small / float(img.size[0]))
# hsize = int((float(img.size[1]) * float(wpercent)))
# img = img.resize((small, hsize), PIL.Image.ANTIALIAS)
# img.save('data/small/'+jpegFileName)  # save down small image
#
