@ECHO.
git pull
@ECHO.
conda activate base
py "md2html-windows.py" 
conda deactivate base
@ECHO.
git add -A
git commit -m "making website"
git push -u origin master
@ECHO.
