
## Add basic graphical environment to Parallella Board ##

Demo video: [https://www.youtube.com/watch?v=6gpM57qB-I8](https://www.youtube.com/watch?v=6gpM57qB-I8)!.

Requirements: Ubuntu PC and Parallella Board.

The following steps should be performed in Parallella Board.

### Install LXDE ###

```
$ sudo apt-get install alsa-base alsa-utils libasound2-plugins lxde x11-xserver-utils xserver-xorg xserver-xorg-video-fbdev xserver-xorg-video-modesetting feh xinit
```

### Disable PCManFM Desktop mode (for faster displaying) ###

```
$ sudo nano /etc/xdg/lxsession/LXDE/autostart
```

Delete the line ```@pcmanfm --desktop --profile LXDE``` and save.

### Xorg configuration ###

Insert:

```
$ sudo nano /etc/X11/xorg.conf
```

The last command should show something like:

```
Section "Device"
  Identifier "Card0"
  Driver "modesetting"
  Option "ShadowFB" "True"
  Option "SWCursor" "True"
  Option "HWCursor" "False"
EndSection
Section "Screen"
  Identifier "Screen0"
  Device "Card0"
  SubSection "Display"
    #---- Uncomment your preferred mode ----
    #Modes "1920x1200"
    #Modes "1920x1080"
    Modes "1280x720"
    #Modes "640x480"
  EndSubSection
EndSection
```

### ALSA configuration ###

```
$ nano ~/.asoundrc
```

Copy, paste and save:

```
pcm.!default {
 type rate
 slave {
  pcm "hw:0"
  rate 48000
 }
 converter "samplerate"
}
```

Then:

```
$ sync
$ sudo reboot
```

### Start X environment ###

On Ubuntu PC, connect to Parallella Board with (we add -X to enable remote execution of applications):

```
$ ssh -X parallella@192.168.1.110
```

And then enter the graphical environment:

```
$ startlxde
```

Note: Correct some problem "/usr/bin/xauth:  file /home/parallella/.Xauthority does not exist".

Exit from SSH and reconnect to SSH, this can solve this problem.

Note: Correct some problem "Error: X11 connection rejected because of wrong authentication", according to [http://www.cyberciti.biz/faq/x11-connection-rejected-because-of-wrong-authentication/](http://www.cyberciti.biz/faq/x11-connection-rejected-because-of-wrong-authentication/)!:

Make sure ~/.Xauthority owned by you.- Run following command to find ownweship:

```
$ ls -l ~/.Xauthority 
```

Run chown and chmod to fix permission problems (replace user:group with your actual username and groupname):

```
$ chown user:group ~/.Xauthority 
$ chmod 0600 ~/.Xauthority
```

Make sure X11 SSHD Forwarding Enabled.- Make sure following line exists in sshd_config file:

```
$ grep X11Forwarding /etc/ssh/sshd_config 
```

Sample output:

```
X11Forwarding yes 
```

### Install media player ###

Insert the command:

```
$ sudo apt-get install smplayer
```

Launch smplayer, then:

Options->Preferences->Video->Output driver: x11.

Options->Preferences->Audio->Output driver: alsa.

Note: If appear the next message "libqtgui4", solve with: [http://answers.ros.org/question/203610/ubuntu-14042-unmet-dependencies-similar-for-14043/](http://answers.ros.org/question/203610/ubuntu-14042-unmet-dependencies-similar-for-14043/)!:

```
$ sudo apt-get install libgl1-mesa-dev-lts-utopic 
```

### Logout and exit from LXDE ###

To exit, logout and reconnect with SSH, or only Ctrl+C.

### Result ###

Start with graphical environment:

![image](/posts/technical/add_basic_graphical_environment_to_parallella_board/startlxde.png)

### Resources ###

- [http://elinux.org/Parallella_Linaro_Nano#How_to_Install_lightweight_X_environment](http://elinux.org/Parallella_Linaro_Nano#How_to_Install_lightweight_X_environment)!.

- [http://www.cyberciti.biz/faq/x11-connection-rejected-because-of-wrong-authentication/](http://www.cyberciti.biz/faq/x11-connection-rejected-because-of-wrong-authentication/)!.


