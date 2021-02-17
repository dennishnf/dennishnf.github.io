
## Set Parallella Board for SSH connection using Ethernet ##

Note: ParallellaBoard-Laptop connection can be done without router (router only gives Internet access).

Scheme of the connection:

![image](/posts/technical/set_parallella_board_for_ssh_connection_using_ethernet/scheme_directly_by_ethernet.png)

### On laptop: ###

1.) Run a recent Ubuntu on PC (I run 14.04).

2.) Set the network-manager on PC.

2.1.) On the computer connected to the Internet, click the network icon in the panel and go to "Edit Connections..." at the bottom of the menu.

![image](/posts/technical/set_parallella_board_for_ssh_connection_using_ethernet/SetInter0.png)

2.2.) Clinc on "Add" to add new Wired Connection and select "Ethernet" (Leave your wireless connection untouched, the one connected to Internet and the one you want to share, as I understand).

![image](/posts/technical/set_parallella_board_for_ssh_connection_using_ethernet/SetInter1.png)

2.3.) In "Ethernet tab", select the correct "Device Mac address". In the "IPv4 Settings tab", select Method: "Shared to other computers".

![image](/posts/technical/set_parallella_board_for_ssh_connection_using_ethernet/SetInter2.png)

2.4.) Reconnect clicking on the Wired Network so it gets its new IP address. (The two computers must be connected by an ethernet cable for this step, so connect them now if you have not already).

2.5.) Click on "Connection Information" in the network menu and write down the IP address and network mask (in my case it was assigned 10.42.0.1/255.255.255.0 but I do not know if that will always be the case).

![image](/posts/technical/set_parallella_board_for_ssh_connection_using_ethernet/SetInter3.png)

3.) Connect an ethernet cable from your computer to the Parallella.

4.) After being connected to the internet using wifi, clock on your new "shared wifi connection to Parallella".

### On Parallella Board: ###

#### 1.) Set a static IP ####

Start Ubuntu and insert the microSD card into the PC (the ext2 format is read by Linux), launch the terminal and open the 'eth0' file with:

```
$ sudo nano /media/dennis/rootfs/etc/network/interfaces.d/eth0
```

In the code above, be careful with "user" and "networks" or "network".

Then copy the following code into the open file 'eth0': (change IP's Parallella according to ethernet network, in my case it's 10.42.0.50).

```
auto eth0 
iface eth0 inet static 
address 10.42.0.50 
netmask 255.255.255.0 
gateway 10.42.0.1 
```

In the code above, 10.42.0.50 is the IP's Parallella.

After, press Ctrl+X and save, then write into terminal:

```
$ sync
```

#### 2.) Connect through SSH ####

Then ejected microSD card memory and insert into the Parallella Board.

Write into the terminal:

```
$ ssh parallella@10.42.0.50 
```

Note: You may also need to remove the following file and reboot: ```/etc/udev/rules.d/74-parallella-persistent-net.rules``` .

and press Enter, then it will connect and write the password, which is ```parallella```.

then, a question will appear [yes/no], select yes.

Done!, Now we are connected to the Parallella Board through SSH.

#### 3.) verify the connection to Internet ####

In addition, to verify that you can connect to the Internet, update the OS:

```
parallella@parallella:~$ sudo apt-get update
```

Note: If you have problem to connect to Internet through ```$ ping -c 3 google.com```, then you should check if the DNS resolver is set correctly, write this to check: ```$ sudo nano /etc/resolv.conf``` and this should show ```nameserver 10.42.0.1```, change this value if isn't set correctly, then ```$ /etc/init.d/networking restart```.

### Resources ###

- [http://parallella.org/forums/viewtopic.php?f=48&t=1043](http://parallella.org/forums/viewtopic.php?f=48&t=1043)!.

- [http://askubuntu.com/questions/359856/share-wireless-internet-connection-through-ethernet](http://askubuntu.com/questions/359856/share-wireless-internet-connection-through-ethernet)!.


