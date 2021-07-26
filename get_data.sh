#!/bin/sh
DATASET="sameersmahajan/people-wikipedia-data"
DATA_DIR="data"
LINES=3000

cd ${DATA_DIR}
kaggle datasets download -d ${DATASET}
unzip people-wikipedia-data.zip
rm -f people-wikipedia-data.zip
mv people_wiki.csv input.csv