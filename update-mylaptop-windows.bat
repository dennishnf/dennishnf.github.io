@ECHO OFF
REM
REM Usage:
REM   update-mylaptop-windows.bat          -^> build + amend commit + force push (daily)
REM   update-mylaptop-windows.bat clear    -^> same, but wipes history and shrinks .git
REM   update-mylaptop-windows.bat sync     -^> pull remote state, DISCARDS local changes
REM
REM Run "sync" first when switching machines, before editing anything.
REM History is rewritten on every run: the remote keeps only one commit.
REM

SET REPO=C:\Users\Dennis\Documents\dennishnf.github.io
CD /D "%REPO%"

IF "%~1"=="sync" GOTO SYNC
IF "%~1"=="clear" GOTO CLEAR
GOTO UPDATE

:SYNC
git fetch origin
git reset --hard origin/main
git clean -fd
GOTO END

:UPDATE
python "md2html.py" "%REPO%"
git add -A
git commit --amend -m "making website"
git push --force origin main
GOTO END

:CLEAR
python "md2html.py" "%REPO%"
git checkout --orphan tmp-clean
git add -A
git commit -m "making website"
git branch -D main
git branch -m main
git push --force origin main
git reflog expire --expire=now --expire-unreachable=now --all
git gc --prune=now --aggressive
GOTO END

:END