
## Avoid prompt password for sudo in Linux ##

You can use this to insert commands without write the password of the user each time, so "it's useful if you run a script" that should contain the password of the user.

```
$ echo 'YOUR-PASSWORD' | sudo -S COMMAND
```

The `-S` flag makes sudo read the password from the standard input. As explained in man sudo:

```
-S, --stdin
Write the prompt to the standard error and read the password from the standard input instead of using the terminal device. 
The password must be followed by a newline character.
```

So, to run ls with sudo privileges, you would do:

```
$ echo 'YOUR-PASSWORD' | sudo -S ls
```

Note that this will produce an error if your sudo access token is active, if you don't need to enter your password because you've already done so recently. To get around that, you could use -k to reset the access token:

```
$ echo 'YOUR-PASSWORD' | sudo -kS ls
```

I don't know of any way of getting you into an actual root shell (like su or sudo -i) do. This might be enough for what you need though.

### Resources ###

- [http://askubuntu.com/questions/470383/how-to-avoid-prompt-password-for-sudo](http://askubuntu.com/questions/470383/how-to-avoid-prompt-password-for-sudo)!

