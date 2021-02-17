#!/bin/bash

#update
git pull;

#create html files
conda activate base
python md2html-ubuntu.py
conda deactivate base

#upload
git add -A;
git commit -m "making website";
git push -u origin master;


