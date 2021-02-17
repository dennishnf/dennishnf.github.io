
## Set dual boot in Ubuntu ##

With a bit of command line trickery, you can get the default of grub to always be a particular grub entry - for example Windows - no matter when a new kernel is installed.

In a terminal type:

```
$ fgrep menuentry /boot/grub/grub.cfg
```

This will display all your grub entries - for example:

```
menuentry 'Ubuntu, with Linux 2.6.38-generic' --class ubuntu --class gnu-linux --class gnu --class os { 
menuentry 'Ubuntu, with Linux 2.6.38-generic (recovery mode)' --class ubuntu --class gnu-linux --class gnu --class os { 
menuentry 'Ubuntu, with Linux 2.6.38-generic' --class ubuntu --class gnu-linux --class gnu --class os {
menuentry 'Ubuntu, with Linux 2.6.38-generic (recovery mode)' --class ubuntu --class gnu-linux --class gnu --class os { 
menuentry "Memory test (memtest86+)" { 
menuentry "Memory test (memtest86+, serial console 115200)" { 
menuentry "Windows Recovery Environment (loader) (on /dev/sda1)" --class windows --class os { 
menuentry "Windows 7 (loader) (on /dev/sda2)" --class windows --class os { 
```

Highlight the entry you want to default to - for example: ``` "Windows 7 (loader) (on /dev/sda2)" ```.

Right click and choose copy.

Type:

```
$ gksu gedit /etc/default/grub
```

Change the entry ```GRUB_DEFAULT=0``` to ```GRUB_DEFAULT="Windows 7 (loader) (on /dev/sda2)"```.

i.e. paste the entry you want (including the quotes).

Save, then type:

```
$ sudo update-grub
```

### Resources ###

- [http://askubuntu.com/questions/52963/how-do-i-set-windows-to-boot-as-the-default-in-the-boot-loader](http://askubuntu.com/questions/52963/how-do-i-set-windows-to-boot-as-the-default-in-the-boot-loader)!.


