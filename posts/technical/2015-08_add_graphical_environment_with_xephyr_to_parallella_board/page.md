
## Add graphical environment with Xephyr Disp. Server to Parallella Board ##

Requirements: Ubuntu PC and Parallella Board.

First you should to set all configurations of the previous post Add Graphical Environment ([https://dennishnf.github.io/posts/technical/2015-08_add_graphical_environment.html](https://dennishnf.github.io/posts/technical/parallella_board/add_graphical_environment.html)!).

### Install Xephyr in your Ubuntu PC: ###

```
$ sudo apt-get install xserver-xephyr
```

### Able or Disable PCManFM Desktop mode: ###

I recommend to disable 'PCManFM Desktop mode' for faster displaying. Edit the next files (On Parallella Board):

```
$ sudo nano /etc/xdg/lxsession/LXDE/autostart
```

```
$ sudo nano ~/.config/lxsession/LXDE/autostart
```

, to able or disable 'PCManFM Desktop mode', in both files add or delete respectively the next line, and save:

```
@pcmanfm --desktop --profile LXDE
```

### Set a background image: ###

Put a background image file in your home directory ( e.g. /home/technical/lxde_wallpaper.png ). Then edit the next files (On Parallella Board):

```
$ sudo nano /etc/xdg/lxsession/LXDE/autostart
```

```
$ sudo nano ~/.config/lxsession/LXDE/autostart
```

, add this line to the bottom of the both files:

```
@feh --bg-fill /home/technical/lxde_wallpaper.png
```

### After set PCManFM Desktop mode and background image: ###

On Parallella Board:

```
$ sync
$ sudo reboot
```

### Running ###

Notice that my PC IP is 192.168.1.101, and Parallella uses 192.168.1.110. Obviously you have to adjust those to your values.

Check your IP here if you are using Ubuntu: [https://sliceoflinux.wordpress.com/2010/04/02/como-averiguar-la-ip-de-un-ordenador-con-ubuntu/](https://sliceoflinux.wordpress.com/2010/04/02/como-averiguar-la-ip-de-un-ordenador-con-ubuntu/)!.

#### 1.Open Xephyr ####

Launch Xephyr Server in your Ubuntu PC. Open a terminal and type:

```
$ Xephyr -ac -br -keybd ephyr,,,xkbmodel=pc105,xkblayout=es -noreset -screen 1280x720 :1
```

You can change the value 1280x720 to: 640x489, 1280x720, 1366x768, ...

#### 2.Connect to Parallella ####

Open a terminal in Ubuntu PC and type:

```
$ ssh -X parallella@10.42.0.50
```

#### 3.Export Parallella Display ####

In the terminal that you are connected to Parallella, type:

```
$ export DISPLAY=192.168.1.101:1
```

You just tell that DISPLAY should be run to the remote machine with the IP (my PC IP is 192.168.1.101) and DISPLAY :1 which is the Xephyr Session. GNOME’s display should be :0, and is used.

#### 4.Run XServer ####

In ssh terminal, that you are connected to Parallella, try to run your graphical environment. I have a default LXDE.

```
$ startlxde
```

#### Another option for steps 2, 3 and 4 ####

Instead of the points 2 and 3, in Ubuntu PC:

```
$ DISPLAY=:1 ssh -Y parallella@10.42.0.50
```

Then continue with step 4, in ssh terminal connected to Parallella:

```
$ startlxde
```

### Result ###

Start with Xephyr Display Server and disable 'PCManFM Desktop mode' and set a background image:

![image](/posts/technical/2015-08_add_graphical_environment_with_xephyr_to_parallella_board/startlxde-DisplayServer.png)

### Resources ###

- [http://worldofgnome.org/howto-export-rpi-display-to-gnome/](http://worldofgnome.org/howto-export-rpi-display-to-gnome/)!.

- [http://elinux.org/Parallella_Linaro_Nano#How_to_Install_lightweight_X_environment](http://elinux.org/Parallella_Linaro_Nano#How_to_Install_lightweight_X_environment)!.


