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
#noUmlaut = kleinbdash(
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


