
## Run basic tests on Parallella Board ##

### Test Xtemp ###

This tool allows you to view temperature Zynq with integrated on-chip sensors Zynq. Write the following command:

Fist clone the repository "parallella-utils" from github:

```
$ git clone  https://github.com/parallella/parallella-utils
```

Then, go into the folder:

```
$ cd parallella-utils/xterm
```

Afet, build:

```
$ gcc -o xtemp xtemp.c -pthread -lX11 -Wall
```

After, look the files with ```$ ls``` and you will look the file **xtemp**, don't confuse with xtemp.c. Then execute:

```
$ ./xtemp
```

With the command above you will appreciate the graph of the temperature. (to viwe the graph you should connect through SSH with ```$ ssh -X parallella@192.168.1.110```).

#### Resources ####

- [https://github.com/parallella/parallella-utils/blob/master/xtemp/xtemp.c](https://github.com/parallella/parallella-utils/blob/master/xtemp/xtemp.c)!.

### Test Mandelbrot (only on Parallella with HDMI image SD card) ###

Some of the examples will not run on the Parallella’s Linux X Window desktop. Instead, TTY (teletype) mode is required. This is the case of "mandelbrot".

Go into the folder:

```
$ cd parallella-examples/mandelbrot/
```

Build:

```
$ make
```

Run:

```
$ ./run.sh
```

### Other Parallella Examples ###

As of this writing, the other programs in the parallella-examples repo can be run in a similar fashion. ```$ cd``` into the directory, run ```$ make```, and then ```$ ./run.sh```.


