
## Set static IP on Ubuntu and enter through terminal or graphic mode using SSH ##

### Set static IP on Ubuntu ###

To get started, move your cursor to top-right corner network icon on panel. Click to expand the menu and choose "Edit Connections".

In next window, choose your wired connection or wifi network then click "Edit" button.

Then navigate to IPv4 Settings tab. Switch Method to "Manual" from the drop-down box. Click Add button and type in IP address, netmask and gateway. Finally click "Save" when everything’s done.

![image](/posts/technical/set_static_ip_on_ubuntu_and_enter_through_terminal_or_graphic_mode_with_ssh/change-to-static-ip.jpg)

When you’re ready, click “Save,” then go to the Terminal and type:

```
$ sudo service network-manager restart
```

### Enter through terminal or graphic mode using SSH ###

There are two ways to connect to the Ubuntu PC:

A. Enter terminal mode:

```
$ ssh bradford@192.168.1.127
```

B. Enter graphic mode:

Open in a first terminal:

```
$ Xephyr -ac -br -keybd ephyr,,,xkbmodel=pc105,xkblayout=es -noreset -screen 1280x720 :1
```

Open in a second terminal:

```
$ DISPLAY=:1 ssh -Y bradford@192.168.1.127
```

```
$ startlxde
```


