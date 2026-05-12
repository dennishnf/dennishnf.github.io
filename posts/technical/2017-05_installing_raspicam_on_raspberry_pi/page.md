
## Installing Raspicam on Raspberry Pi: C++ API for using Raspberry camera with/without OpenCV ##

IMPORTANT!! The Rasperry Pi camera is not an usb-webcam. Thus, OpenCV doesn’t work natively (forget cvCaptureFromCAM for example and all your wonderful apps you’ve thought up!). However, some nice apps (such as raspivid or raspistill) controls  the pi camera using MMAL functions. The idea is to modify source code of such apps, use buffer memory of the camera to feed OpenCV image objects. Pretty easy (said like that). You can find some examples at:

- [https://thinkrpi.wordpress.com/2013/05/22/opencv-and-camera-board-csi/](https://thinkrpi.wordpress.com/2013/05/22/opencv-and-camera-board-csi/)!.

- [https://thinkrpi.wordpress.com/2013/05/22/opencvpi-cam-step-5-basic-use-display-a-picture/](https://thinkrpi.wordpress.com/2013/05/22/opencvpi-cam-step-5-basic-use-display-a-picture/)!.

Another option to control the RPI camera is the Raspicam library, which allows to use the Raspberry Pi Camera under BSD License. Main Developer: Rafael Muñoz Salinas ( rmsalinas at uco dot es). Acknowledgement: thanks to Josh-Larson for his contribution.

Download at SourceForge:

- [https://sourceforge.net/projects/raspicam/files/?](https://sourceforge.net/projects/raspicam/files/?)!.

### Main features ###

- Provides  class RaspiCam for easy and full control of the camera.

- Provides class  RaspiCam_Still and RaspiCam_Still_Cv for controlling the camera in still mode.

- Provides class  RaspiCam_Cv for easy control of the camera with OpenCV.

- Provides class  RaspiCam_Still and RaspiCam_Still_Cv for controlling the camera in still mode.

- Provides class RaspiCam_Still and RaspiCam_Still_Cv for using the still camera mode.

- Easy compilation/installation using cmake.

- No need to install development file of userland. Implementation is hidden.

- Many examples.

### Connect to RPI with SSH and Xephyr ###

First, on Ubuntu:

```
$ Xephyr -ac -br -keybd ephyr,,,xkbmodel=pc105,xkblayout=es -noreset -screen 1280x720 :1
```

Then, on RPI:

```
$ DISPLAY=:1 ssh -Y pi@10.42.0.246
$ startlxde
```

### Compiling ###

Note: You should compile and install again after a new version of OpenCV is installed in your PC.

Download the file to your raspberry. Uncompress.

Then, compile:

```
$ cd raspicam-xx
$ mkdir build
$ cd build
$ cmake ..
```

At this point you'll see something like:

```
-- CREATE OPENCV MODULE=1
-- CMAKE_INSTALL_PREFIX=/usr/local
-- REQUIRED_LIBRARIES=/opt/vc/lib/libmmal_core.so;/opt/vc/lib/libmmal_util.so;/opt/vc/lib/libmmal.so
-- Change a value with: cmake -D<<x>Variable<x>>=<<x>Value<x>>
-- 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/pi/raspicam/trunk/build
```

If OpenCV development files are installed in your system, then  you see:

```
-- CREATE OPENCV MODULE=1
```

otherwise this option will be 0 and the opencv module of the library will not be compiled.
 
Finally compile, install and update the ldconfig:

```
$ make
$ sudo make install
$ sudo ldconfig
```

After that, you have the programs ```raspicam_test``` and ```raspicam_cv_test``` (if opencv was enabled), under ```raspicam-xx/build/utils/```. Run the programs to check that compilation is ok.

### Using it in your projects ###

You can learn how to use the library by taking a look at the examples in the utils directory and  by analyzing the header files. In addition, we provide a some simple examples on how to use the library.

First, create a directory for our own project. Then, go in and create a file with the name ```simpletest_raspicam.cpp``` and add the following code:

```
#include <<x>ctime>
#include <<x>fstream>
#include <<x>iostream>
#include <<x>raspicam/raspicam.h>
#include <<x>unistd.h>
    
using namespace std;
    
int main ( int argc,char **argv ) {
  raspicam::RaspiCam Camera; //Cmaera object
  //Open camera 
  cout<<x><<x>"Opening Camera..."<<x><<x>endl;
  if ( !Camera.open()) {cerr<<x><<x>"Error opening camera"<<x><<x>endl;return -1;}
  //wait a while until camera stabilizes
  cout<<x><<x>"Sleeping for 3 secs"<<x><<x>endl;
  sleep(3);
  //capture
  Camera.grab();
  //allocate memory
  unsigned char *data=new unsigned char[  Camera.getImageTypeSize ( raspicam::RASPICAM_FORMAT_RGB )];
  //extract the image in rgb format
  Camera.retrieve ( data,raspicam::RASPICAM_FORMAT_RGB );//get camera image
  //save
  std::ofstream outFile ( "raspicam_image.ppm",std::ios::binary );
  outFile<<x><<x>"P6\n"<<x><<x>Camera.getWidth() <<x><<x>" "<<x><<x>Camera.getHeight() <<x><<x>" 255\n";
  outFile.write ( ( char* ) data, Camera.getImageTypeSize ( raspicam::RASPICAM_FORMAT_RGB ) );
  cout<<x><<x>"Image saved at raspicam_image.ppm"<<x><<x>endl;
  //free resrources
  delete data;
  return 0;
}
```

Then, compile:

```
$ g++ -I/usr/local/include/ -L/opt/vc/lib -g -o binary simpletest_raspicam.cpp -lraspicam -lmmal -lmmal_core -lmmal_util -o simpletest_raspicam
```

Finally, run the program:

```
$ ./simpletest_raspicam
```

### OpenCV Interface ###

If the OpenCV is found when compiling the library, the libraspicam_cv.so module is created and the RaspiCam_Cv class available. Take a look at the examples in utils to see how to use the class. In addition, we show here how you can use the RaspiCam_Cv in your own project.

First, create a directory for our own project. Then, go in and create a file with the name ```simpletest_raspicam_cv.cpp``` and add the following code:

```
#include <<x>ctime<x>>
#include <<x>iostream<x>>
#include <<x>raspicam/raspicam_cv.h<x>>
    
using namespace std; 
    
int main ( int argc,char **argv ) {
  time_t timer_begin,timer_end;
  raspicam::RaspiCam_Cv Camera;
  cv::Mat image;
  int nCount=100;
  //set camera params, CV_8UC1 grayscale, CV_8UC3 colored
  Camera.set( CV_CAP_PROP_FORMAT, CV_8UC1 );
  //Open camera
  cout<<x><<x>"Opening Camera..."<<x><<x>endl;
  if (!Camera.open()) {cerr<<x><<x>"Error opening the camera"<<x><<x>endl;return -1;}
  //Start capture
  cout<<x><<x>"Capturing "<<x><<x>nCount<<x><<x>" frames ...."<<x><<x>endl;
  time ( &timer_begin );
  for ( int i=0; i<<x>nCount; i++ ) {
    Camera.grab();
    Camera.retrieve ( image);
    if ( i%5==0 )  cout<<x><<x>"\r captured "<<x><<x>i<<x><<x>" images"<<x><<x>std::flush;
  }
  cout<<x><<x>"Stop camera..."<<x><<x>endl;
  Camera.release();
  //show time statistics
  time ( &timer_end ); /* get current time; same as: timer = time(NULL)  */
  double secondsElapsed = difftime ( timer_end,timer_begin );
  cout<<x><<x> secondsElapsed<<x><<x>" seconds for "<<x><<x> nCount<<x><<x>"  frames : FPS = "<<x><<x>  ( float ) ( ( float ) ( nCount ) /secondsElapsed ) <<x><<x>endl;
  //save image 
  cv::imwrite("raspicam_cv_image.jpg",image);
  cout<<x><<x>"Image saved at raspicam_cv_image.jpg"<<x><<x>endl;
}
```

Then, compile:

```
$ g++ -I/usr/local/include/ -g -o binary simpletest_raspicam_cv.cpp -lopencv_core -lopencv_highgui -lraspicam -lraspicam_cv -o simpletest_raspicam_cv
```

Finally, run the program:

```
$ ./simpletest_raspicam_cv
```

### Resources ###

- [https://www.uco.es/investiga/grupos/ava/node/40](https://www.uco.es/investiga/grupos/ava/node/40)!.

- [https://thinkrpi.wordpress.com/2013/05/22/opencv-and-camera-board-csi/](https://thinkrpi.wordpress.com/2013/05/22/opencv-and-camera-board-csi/)!.

