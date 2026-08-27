
## Build and install multiple versions of OpenCV on Linux ##

Before installation, during CMAKE, you should specify different install paths using ```-D CMAKE_INSTALL_PREFIX= flag``` (I'll create the folder ```libraries``` in the path ```/home/dennis/opencv-2.4.9/```).

For example, for opencv 2.4.9:

```
-D CMAKE_INSTALL_PREFIX=/home/dennis/opencv-2.4.9/libraries
```

while for opencv 3.3.0:

```
-D CMAKE_INSTALL_PREFIX=/home/dennis/opencv-3.3.0/libraries
```

Do not confuse this path with source path.

-----------------.

Note: Also, maybe building static libs is a good idea then (cmake ```-D BUILD_SHARED_LIBS=OFF), since you won't be allowed to install the so's to system path either.

-----------------.

Also, add the next lines to the .bashrc file:

```
# For OpenCV 2.4.9
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/dennis/opencv-2.4.9/libraries/lib 
     
# For OpenCV 3.3.0
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/dennis/opencv-3.3.0/libraries/lib 
```

Finally, the real "magic" is in the makefile to compile your own code. Linking path and include paths have to be specified as per the opencv version you want.


For example : You have opencv 2.4.9 installed in ```/path/to/opencv2.4.9/lib/``` and opencv 3.3.0 install in ```/path/to/opencv3.3.0/lib/``` as per mentioned in that link, you will have makefile as per below:

### Compile using OpenCV 2.4.9 and C++ ###

Compile using the ```Makefile```:

```
CC = g++
CFLAGS = -g -Wall
SRCS = example.cpp
PROG = example
     
OPENCV_LIBS = /home/dennis/opencv-2.4.9/libraries
     
OPENCV = -I$(OPENCV_LIBS)/include/opencv -I$(OPENCV_LIBS)/include \
$(OPENCV_LIBS)/lib/libopencv_calib3d.so $(OPENCV_LIBS)/lib/libopencv_core.so \
$(OPENCV_LIBS)/lib/libopencv_highgui.so $(OPENCV_LIBS)/lib/libopencv_imgproc.so
     
LIBS = $(OPENCV)
     
$(PROG):$(SRCS)
	$(CC) $(CFLAGS) -o $(PROG) $(SRCS) $(LIBS)
```

Compile:

```
$ make
```

### Compile using OpenCV 3.3.0 and C++ ###

Compile using the ```Makefile```:

```
CC = g++
CFLAGS = -g -Wall
SRCS = example.cpp
PROG = example
     
OPENCV_LIBS = /home/dennis/opencv-3.3.0/libraries
     
OPENCV = -I$(OPENCV_LIBS)/include/opencv -I$(OPENCV_LIBS)/include \
$(OPENCV_LIBS)/lib/libopencv_calib3d.so $(OPENCV_LIBS)/lib/libopencv_core.so \
$(OPENCV_LIBS)/lib/libopencv_highgui.so $(OPENCV_LIBS)/lib/libopencv_imgproc.so 
     
LIBS = $(OPENCV)
     
$(PROG):$(SRCS)
	$(CC) $(CFLAGS) -o $(PROG) $(SRCS) $(LIBS)
```

Compile:

```
$ make
```

### Using different OpenCV's versions with Python ###

Since the cv2.so is the file to import cv2 to python. In OpenCV 2.4.9, this file is located at:

- ```/home/dennis/opencv-2.4.9/libraries/lib/python2.7/dist-packages/cv2.so``` for Python 2.7.

- ```/home/dennis/opencv-2.4.9/libraries/lib/python3.4/dist-packages/cv2.so``` for Python 3.4.

Since the cv2.so is the file to import cv2 to python. In OpenCV 3.3.0, this file is located at:

- ```/home/dennis/opencv-3.3.0/libraries/lib/python2.7/dist-packages/cv2.so``` for Python 2.7.

- ```/home/dennis/opencv-3.3.0/libraries/lib/python3.4/dist-packages/cv2.so``` for Python 3.4.

So, to use OpenCV 3.3.0 in Python 2.7 insert the next command before start working with cv2 library:

```
In [1]: import sys
      
In [2]: sys.path.insert(0,'/home/dennis/opencv-3.3.0/libraries/lib/python2.7/dist-packages')
      
In [3]: import cv2
```

You can check with:

```
In [4]: cv2.__version__
Out[4]: '3.3.0'
      
In [5]: cv2.__file__
Out[5]: '/home/dennis/opencv-3.3.0/libraries/lib/python2.7/dist-packages/cv2.so'
```

-----------------.

Trick: You can copy the ```cv2.so``` from ```/home/dennis/opencv-3.3.0/libraries/lib/python2.7/dist-packages/cv2.so``` to your project directory ```~/Desktop/example``` in order to ```import cv2``` using OpenCV 3.3.0 (for Python) in your example.

-----------------.

### Resources ###

- [http://answers.opencv.org/question/65178/install-multiple-versions-of-opencv-on-ubuntu/](http://answers.opencv.org/question/65178/install-multiple-versions-of-opencv-on-ubuntu/)!.

- [https://stackoverflow.com/questions/43051470/install-opencv3-on-ubuntu-installation-without-remove-opencv2-package](https://stackoverflow.com/questions/43051470/install-opencv3-on-ubuntu-installation-without-remove-opencv2-package)!.

- [http://answers.opencv.org/question/98580/how-to-set-up-a-side-opencv-set-path-to-another-opencv/](http://answers.opencv.org/question/98580/how-to-set-up-a-side-opencv-set-path-to-another-opencv/)!.


