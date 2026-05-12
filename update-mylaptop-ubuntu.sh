#!/bin/bash

#update
git pull;

#create html files
python3 md2html.py "/home/dennishnf/Desktop/dennishnf.github.io"

#upload
git add -A;
git commit -m "making website";
git push -u origin main;


