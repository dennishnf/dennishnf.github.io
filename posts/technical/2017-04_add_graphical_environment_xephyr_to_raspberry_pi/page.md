
## Add Graphical Environment with Xephyr Disp. Server to Raspberry Pi ##

Requirements: Ubuntu PC and Raspberry Board.

### Install Xephyr in your Ubuntu PC: ###

```
$ sudo apt-get install xserver-xephyr
```

### Running ###

Notice that my PC IP is 192.168.1.2, and Raspberry uses 10.42.0.50. Obviously you have to adjust those to your values.

Check your IP here if you are using Ubuntu: [https://sliceoflinux.wordpress.com/2010/04/02/como-averiguar-la-ip-de-un-ordenador-con-ubuntu/](https://sliceoflinux.wordpress.com/2010/04/02/como-averiguar-la-ip-de-un-ordenador-con-ubuntu/)!.

#### 1.Open Xephyr ####

Launch Xephyr Server in your Ubuntu PC. Open a terminal and type:

```
$ Xephyr -ac -br -keybd ephyr,,,xkbmodel=pc105,xkblayout=es -noreset -screen 1280x720 :1
```

You can change the value 1280x720 to: 640x489, 1280x720, 1366x768, ...

#### 2.Connect to Raspberry ####

Open a terminal in Ubuntu PC and type:

```
$ ssh -X pi@10.42.0.256
```

#### 3.Export Raspberry Display ####

In the terminal that you are connected to Raspberry, type:

```
$ export DISPLAY=192.168.1.2:1
```

You just tell that DISPLAY should be run to the remote machine with the IP (my PC IP is 192.168.1.2) and DISPLAY :1 which is the Xephyr Session. GNOME’s display should be :0, and is used.

#### 4.Run XServer ####

In ssh terminal, that you are connected to Raspberry, try to run your graphical environment. I have a default LXDE.

```
$ startlxde
```

#### Another option for steps 2, 3 and 4 ####

Instead of the points 2 and 3, in Ubuntu PC:

```
$ DISPLAY=:1 ssh -Y pi@10.42.0.246
```

Then continue with step 4, in ssh terminal connected to Raspberry Pi:

```
$ startlxde
```

### Result ###

Start with Xephyr Display Server:

![image](/posts/technical/2017-04_add_graphical_environment_xephyr_to_raspberry_pi/startlxde-DisplayServer.png)

### Resources ###

-[http://studiopentagon.info/?q=node/38](http://studiopentagon.info/?q=node/38)!.

