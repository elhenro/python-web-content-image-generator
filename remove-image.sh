#!/bin/bash
IMG_TITLE=$1
HERO_TITLE='hero_'${IMG_TITLE}
echo 'Starting to remove '${IMG_TITLE}'..'

# to make sure the location is correct
cd ~/web/python-web-content-image-generator/

rm data/large/${IMG_TITLE} 
rm data/medium/${IMG_TITLE} 
rm data/small/${IMG_TITLE} 
rm data/square/${IMG_TITLE}

rm hero/large/${HERO_TITLE}
rm hero/medium/${HERO_TITLE}
rm hero/small/${HERO_TITLE}

rm workbench/${IMG_TITLE}
rm workbench_hero/${HERO_TITLE}

echo 'Done, deleting '${IMG_TITLE}' and '${HERO_TITLE}'.'
