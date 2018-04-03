#!/bin/bash

INITIAL_DIR=`pwd`
LOCATION=./data/large

[[ -d $LOCATION ]] || mkdir $LOCATION
cd $LOCATION
wget http://biofunctionprediction.org/cafa-targets/targetFiles.zip
unzip targetFiles.zip
rm targetFiles.zip

cd $INITIAL_DIR