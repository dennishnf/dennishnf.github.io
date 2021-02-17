
## Shorten command line (bash) prompt in Linux ##

Permanentemente:

```
$ sudo nano .bashrc
```

Por defecto es así:

```
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
```

Modificar los siguientes simbolos: \u, @, \h, :, \w, \W.

Quedándo:

```
if [ "$color_prompt" = yes ]; then
    PS1='[${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\] \[\033[01;34m\]\W\[\033[00m\]]\$ '
else
    PS1='[${debian_chroot:+($debian_chroot)}\u@\h \W]\$ '
fi
```

Y va a quedar de la forma:

```
[user@hostname dirname]$
```

### Resources ###

- [http://askubuntu.com/questions/145618/how-can-i-shorten-my-command-line-bash-prompt](http://askubuntu.com/questions/145618/how-can-i-shorten-my-command-line-bash-prompt)!.

