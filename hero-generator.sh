#!/usr/bin/env bash
# automatic hero image producer
# usage: hnr@hnr-b:~/web/CI-generator$ sh hero-generation-script.sh blank_hero.jpg 'Test Titel' script-res
# --> $ sh hero-generation-script.sh hero-bg.jpg 'CTA TEXT' final-name.jpg
# args
INPUT="$1"
TITLE="$2"
FILENAME="$3"
# put title text in html
sed -i "s/TEXT/${TITLE}/" button.html
# render CTA from button.html
phantomjs /usr/local/share/phantomjs/examples/rasterize.js /home/hnr/web/python-web-content-image-generator/button.html exp.png
# merge images southeast - put CTA on image
composite -gravity southeast exp.png $INPUT $FILENAME
# End
# replace CTA text back
sed -i "s/${TITLE}/TEXT/" button.html
echo "hero-generator.sh successful."
export LANG=C.UTF-8
