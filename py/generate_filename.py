# Example test input: $ python3 generate_filename.py 'Das Schwein' -->
# das-schwein.jpg
import sys
import datetime
TimeNow = (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
item_title = (sys.argv[1])
kleinb = item_title.lower()

kleinbdash = kleinb.replace(' ', '-').lower()
#noUmlaut = kleinbdash(
jpegFileName = kleinbdash + '.jpg'
print (jpegFileName)

f = open('log/main-log', 'w')
f.write(TimeNow + ' generating filename: '+ jpegFileName + ' from title: ' + item_title + '\n')
f.close() 

