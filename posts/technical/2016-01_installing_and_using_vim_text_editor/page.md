
## Installing and Using Vim text editor ##

### Introduction ###

The vi editor is a very powerful tool and has a very extensive built-in manual, which you can activate using the ```:help``` command when the program is started (instead of using man or info, which don't contain nearly as much information). We will only discuss the very basics here to get you started.

What makes vi confusing to the beginner is that it can operate in two modes: "command mode" and "insert mode". The editor always starts in command mode. Commands move you through the text, search, replace, mark blocks and perform other editing tasks, and some of them switch the editor to insert mode. This means that each key has not one, but likely two meanings: it can either represent a command for the editor when in command mode, or a character that you want in a text when in insert mode.

### Installing on Linux ###

First, check if you have Vim.

```
$ vim
```

, and you should see something like this:

```
~                                                                                    
~                                 VIM - Vi IMproved                                  
~                                                                                    
~                                  version 7.4.52                                    
~                             by Bram Moolenaar et al.                               
~              Modified by pkg-vim-maintainers@lists.alioth.debian.org               
~                    Vim is open source and freely distributable                     
~                                                                                    
```

If not, you should install Vim:

```
$ sudo apt-ge update
$ sudo apt-get install vim
```

You can check the default Vim tutorial with:

```
$ vimtutor
```

### Starting ###

Similar to another editors, you can create or open a new file in the current directory with:

```
$ vim file.txt
```

As I mentioned in the introduction, Vim has two modes "command mode" and "insert mode". The editor always starts in command mode. So, commands move you through the text, search, replace, mark blocks and perform other editing tasks, and some of them switch the editor to insert mode. This means that each key has not one, but likely two meanings: it can either represent a command for the editor when in command mode, or a character that you want in a text when in insert mode.

After the file.txt is open:

-Insert ```i``` to switch the editor from command mode (not able to edit the file) to insert mode (able to edit the file).

-Insert ESC buttom to switch the editor from insert mode (able to edit the file) to command mode (not able to edit the file).

NOTE: Instead of ```i```, you can Insert other keys to switch from command mode to insert mode:

- ```i```: insert before the cursor.

- ```I```: insert at the beginning of the line.

- ```a```: insert (append) after the cursor.

- ```A```: insert (append) at the end of the line.

- ```o```: append (open) a new line below the current line.

- ```O```: append (open) a new line above the current line.

### Saving and Quitting ###

In command mode:

Insert ```:w``` to save the file. If you don't have a filename or want to write out to a different filename, use ```:w filename```.

Insert ```:wq``` to save and exit.

Insert ```:q``` to exit (this fails when changes have been made), ```:q!``` to quit without writing.

### Default VIM setting in .vimrc ###

In command mode:

Insert ```:set ruler``` to have the line and column number indicator.

Insert ```:set laststatus=2``` to have the status bat at the bottom with the current file name and the ruler.

Insert ```:set number``` to show the number of each line.

Insert ```:set title``` to show the name of the file.

Insert ```:set hlsearch``` to highlight search words.

Insert ```:syntax on``` to show the syntax of the file.

But if the file is closed with ```:q``` and open again, all last settings dissapear. So, to solve this we should to docked them in our home directory with:

```
$ cd 
$ vim .vimrc 
```

Then edit with Vim using ```i``` and inserting:

```
set ruler laststatus=2 number title hlsearch
syntax on
```

Then save and exit with ```:wq```.

### Setting Indent in .vimrc  ###

In command mode:

Add the following lines in your .vimrc:

```
filetype plugin indent on
" show existing tab with 2 spaces width
set tabstop=2
" when indenting with '>', use 2 spaces width
set shiftwidth=2
```

### Indent several lines ###

Press ```V``` to switch to VISUAL LINE mode and highlight the lines you want to indent by pressing ```j``` (or ↓ button). Then press ```>``` to indent them. So the complete command would be ```Vjjj>```.

### Editing files ###

In command mode:

Insert ```u``` to undo.

Insert Ctrl + ```r``` to redo.

Insert ```.``` to repeat last command.

### Copy/cut and paste into Vim ###

Position the cursor where you want to begin cutting.

Insert ```v``` to select characters (or uppercase ```V``` to select whole lines).

Move the cursor to the end of what you want to cut.

Insert ```y``` to copy (or ```d``` to cut).

Move to where you would like to paste.

Insert ```p``` to paste after the cursor, or ```P``` to paste before.

### Copy/cut and paste to external ###

-Copy from Vim to external:

Position the cursor where you want to begin cutting.

Insert ```v``` to select characters (or uppercase ```V``` to select whole lines).

Move the cursor to the end of what you want to cut.

Insert ```"+y``` to copy (or ```"+d``` to cut).

Move to where you would like and paste.

-Copy from external to Vim:

Select manually the text and copy.

Insert ```"+p``` to paste after the cursor, or ```"+P``` to paste before.

### Search and replace ###

In command mode:

Insert ```/pattern``` to search for pattern.

Insert ```?pattern``` to search backward for pattern.

Insert ```n``` to repeat search in same direction, or ```N``` to repeat search in opposite direction.

Insert ```:%s/old/new/g``` to replace all old with new throughout file.

Insert ```:%s/old/new/gc``` to replace all old with new throughout file with confirmations.

Insert ```:noh``` to remove highlighting of search matches.

### Opening different files ###

When starting Vim, the -p option opens each specified file in a separate tab.

```
$ vim -p first.txt second.txt
```

Insert ```{i}gt``` to go to tab in position i.

In the opened file, insert ```:tabnew``` or ```:tabnew file``` to open a file in a new tab.

### Cursor movement ####

List of commands to insert in command mode:

- ```H```: move to top of screen.

- ```M```: move to middle of screen.

- ```L```: move to bottom of screen.

- ```w```: jump forwards to the start of a word.

- ```W```: jump forwards to the start of a word (words can contain punctuation).

- ```e```: jump forwards to the end of a word.

- ```E```: jump forwards to the end of a word (words can contain punctuation).

- ```b```: jump backwards to the start of a word.

- ```B```: jump backwards to the start of a word (words can contain punctuation).

- ```$```: jump to the end of the line.

- ```gg```: go to the first line of the document.

- ```G```: go to the last line of the document.

- ```5G```: go to line 5.

- ```}```: jump to next paragraph (or function/block, when editing code).

- ```{```: jump to previous paragraph (or function/block, when editing code).

- ```zz```: center cursor on screen.

- Ctrl + ```b```: move back one full screen.

- Ctrl + ```f```: move forward one full screen.

- Ctrl + ```d```: move forward 1/2 a screen.

- Ctrl + ```u```: move back 1/2 a screen.

### Resoures ###

- Home site of Vim: [https://vim.sourceforge.io/](https://vim.sourceforge.io/)!.

- Vim Cheat Sheet: [https://vim.rtorr.com/](https://vim.rtorr.com/)!.


