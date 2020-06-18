
## Enter to Parallella Board with SSH and first settings ##

Start typing in the terminal:

```
$ ssh [user@]hostname
```

In my case: (I use 192.168.1.110 to connect through a router, or 10.42.0.50 to connect directly by ethernet).

```
$ ssh parallella@192.168.1.110
```

The command above starts the remote control of Parallella Board.

After, write the password ```parallella```:

```
parallella@192.168.1.110's password: parallella
```

Then, the mext message will appear:

```
Welcome to Linaro 14.04 (GNU/Linux 3.14.12-parallella-xilinx-g40a90c3 armv7l)
 ' Documentation:  https://wiki.linaro.org/
Last login: Wed Jul 15 01:08:59 2015 from 192.168.1.110
parallella@parallella:~$ 
```

Then, if is the first time you connect to Parallella Board with SSH, you can:

#### Set or Change User Password ####

Type passwd command as follows to change your own password:

```
$ passwd
```

#### Upgrade an Update ####

```
parallella@parallella:~$ sudo apt-get update
parallella@parallella:~$ sudo apt-get upgrade
```

#### Set correctly timezone ####

To change the timezone on Ubuntu/Debian distros you can use this command:

```
$ sudo dpkg-reconfigure tzdata
```

#### Correct issue: "perl: warning: Setting locale failed." ####

If you run ```$ sudo dpkg-reconfigure locales``` and it shows the next message:

```
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
	LANGUAGE = (unset),
	LC_ALL = (unset),
	LC_PAPER = "es_PE.UTF-8",
	LC_ADDRESS = "es_PE.UTF-8",
	LC_MONETARY = "es_PE.UTF-8",
	LC_NUMERIC = "es_PE.UTF-8",
	LC_TELEPHONE = "es_PE.UTF-8",
	LC_IDENTIFICATION = "es_PE.UTF-8",
	LC_MEASUREMENT = "es_PE.UTF-8",
	LC_TIME = "es_PE.UTF-8",
	LC_NAME = "es_PE.UTF-8",
	LANG = "C.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
```

Simply add 'es_PE.UTF-8' to 'local' file:

```
$ sudo locale-gen es_PE.UTF-8
```

If you have the same issue but it shows 'en_US.UTF-8' instead of 'es_PE.UTF-8', so in the previous command replace 'es_PE.UTF-8' by 'en_US.UTF-8'.

#### Run some Tests ####

Now you can browse folders and run some tests with:

```
$ ./test.sh
```

#### Shutdown the Parallella Board ####

To shutdown the Board Parallella not forget to insert the following command, and then disconnect the power supply:

```
$ sudo shutdown -h now
```


