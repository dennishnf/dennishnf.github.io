
## Repair or Reinstall GRUB2 ##

Grub 2 typically gets overridden when you install Windows or another Operating System. To make Ubuntu control the boot process, you need Reinstall (Repair/Restore) Grub using a Ubuntu Live CD.

### Warning ###

Using the sudo command, especially from a Live CD can do serious damage to your system. Read all instructions and confirm you understand before executing any commands. When pasting into the Terminal, use Ctrl+Shift+V, NOT Ctrl+V.

### Terminal Commands ###

Mount the partition your Ubuntu Installation is on. If you are not sure which it is, launch GParted (included in the Live CD) and find out. It is usually a EXT4 Partition. Replace the XY with the drive letter, and partition number, for example: sudo mount /dev/sda3 /mnt.

```
$ sudo mount /dev/sdXY /mnt
```

Now bind the directories that grub needs access to to detect other operating systems, like so.

```
$ sudo mount --bind /dev /mnt/dev &&
$ sudo mount --bind /dev/pts /mnt/dev/pts &&
$ sudo mount --bind /proc /mnt/proc &&
$ sudo mount --bind /sys /mnt/sys
```

Now we jump into that using chroot.

```
$ sudo chroot /mnt
```

Now install, check, and update grub.

This time you only need to add the drive letter (usually a) to replace X, for example: grub-install /dev/sda, grub-install –recheck /dev/sda.

```
$ grub-install /dev/sdX
$ grub-install --recheck /dev/sdX
$ update-grub
```

Now grub is back, all that is left is to exit the chrooted system and unmount everything.

```
$ exit &&
$ sudo umount /mnt/sys &&
$ sudo umount /mnt/proc &&
$ sudo umount /mnt/dev/pts &&
$ sudo umount /mnt/dev &&
$ sudo umount /mnt
```

Shut down and turn your computer back on, and you will be met with the default Grub2 screen.

You may want to update grub or re-install burg however you like it.

Congratulations, you have just Repaired/Restored/Reinstalled Grub 2 with a Ubuntu Live CD!.

Ojo: If appear this warning: sector 32 is already in use by flexnet, write:

```
$ sudo dd if=/dev/zero of=/dev/sda bs=512 count=1 seek=32
```

Then, you shuld realise all steps again.

### Resources ###

- [http://howtoubuntu.org/how-to-repair-restore-reinstall-grub-2-with-a-ubuntu-live-cd](http://howtoubuntu.org/how-to-repair-restore-reinstall-grub-2-with-a-ubuntu-live-cd)!.

- [http://askubuntu.com/questions/195390/grub-gives-messages-about-the-boot-sector-being-used-by-other-software-what-sho](http://askubuntu.com/questions/195390/grub-gives-messages-about-the-boot-sector-being-used-by-other-software-what-sho)!.

