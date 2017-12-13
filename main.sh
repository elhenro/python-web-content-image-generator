
# Start
# Content Image Generation Script

#!/bin/bash          
TITLE=$1
ITEMURL=$2
BASE_DIR='~/Dropbox/Sprachspielspass.de/#contentprocess/New/'
# Parameters: $ main.sh 'Title' URL

# cd $BASE_DIR;

#   0. Get Image Title
python3 py/generate_filename.py $TITLE   
#   
#   1. Get Link Info
# python3 py/get_url_info.py $ITEMURL
#   2. Grab Author and ID and put Info in XML
#   3. Generate filename and hero_filename and save it in XML
#   4. Download Image and save in workbench
#   5. Process Content Image
#   6. Render CTA from Title 
#   7. Process Hero images (only large, no compression)
#   8. merge CTA on large Hero image
#   9. process medium and small hero images
#  10. Log Title, URL, Author, ID, Heroname, Filename, Time in Log File 
