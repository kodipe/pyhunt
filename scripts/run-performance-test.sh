#!/bin/bash

DATASET_DIRECTORY="test/performance/__dataset__"
DATASET_URL="http://mlg.ucd.ie/files/datasets/bbc-fulltext.zip"

if [ ! -d "$DATASET_DIRECTORY" ];
then
  mkdir "$DATASET_DIRECTORY"
fi

DATASET_SIZE=$(du -s "$DATASET_DIRECTORY" | cut -f1)

if [ $(($DATASET_SIZE + 0)) -eq 0 ];
then
  printf "Dataset is empty - downloading $DATASET_URL\n\n"
  curl -X GET "$DATASET_URL" --output bbc.zip
  printf "\nUnzipping dataset..."
  unzip -q -o bbc.zip -d "$DATASET_DIRECTORY"
  rm -rf bbc.zip
else
  printf "You dataset directory is not empty - there is no need to download dataset"
fi;

printf "\nPerformance test start\n"

time python ./test/performance/performance-test.py > result.txt