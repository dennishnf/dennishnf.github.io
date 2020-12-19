
## Accessing to Raspberry Pi camera with OpenCV 2 and Raspicam ##

Once installed Raspicam ([https://dennishnf.bitbucket.io/posts/raspberry/installing_raspicam_on_raspberry_pi/home.html](Installing Raspicam)!), now we can finally start writing some code!.

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

### Image capturing OpenCV and Raspicam ###

Open up a new file, name it ```example0.cpp```, and insert the following code:

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
  cout<<x><<x> secondsElapsed<<x><<x>" seconds for "<<x><<x> nCount<<x><<x>" frames : FPS = "<<x><<x>  ( float ) ( ( float ) ( nCount ) /secondsElapsed ) <<x><<x>endl;
  //save image 
  cv::imwrite("raspicam_cv_image.jpg",image);
  cout<<x><<x>"Image saved at raspicam_cv_image.jpg"<<x><<x>endl;
}
```

Compile:

```
$ g++ -I/usr/local/include/ -g -o binary  example0.cpp -lopencv_core -lopencv_highgui -lraspicam -lraspicam_cv -o example0
```

Then, run the program:

```
$ ./example0
```

If all goes as expected you should save an image in the current folder.

### Display video stream using OpenCV and Raspicam ###

Open up a new file, name it ```example1.cpp```, and insert the following code:

```
#include <<x>ctime<x>>
#include <<x>iostream<x>>
#include <<x>raspicam/raspicam_cv.h<x>>
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
    
using namespace cv;
using namespace std;
    
int main(int argc, char **argv)
{
  raspicam::RaspiCam_Cv cam;
  Mat image;
  //set camera params, CV_8UC1 grayscale, CV_8UC3 colored
  cam.set(CV_CAP_PROP_FORMAT, CV_8UC1);
  if (!cam.open())
    return 1;
    
  const char szSourceWindow[] = "Source";
  namedWindow(szSourceWindow, WINDOW_AUTOSIZE);
    
  for (;;)
  {
    cam.grab();
    cam.retrieve(image);
    resize(image, image, Size(), 0.5, 0.5);
    imshow(szSourceWindow, image);
    int c = waitKey(100);
    if((char)c == 'q') { 
      break; 
    }
  }
    
  cam.release();
  return 0;
}
```

Compile:

```
$ g++ -I/usr/local/include/ -g -o binary  example1.cpp -lopencv_core -lopencv_highgui -lopencv_imgproc -lraspicam -lraspicam_cv -o example1
```

Then, run the program:

```
$ ./example1
```

If all goes as expected you should have an image displayed on your screen.

### Canny detector using OpenCV and Raspicam ###

Open up a new file, name it ```example2.cpp```, and insert the following code:

```
#include <<x>ctime<x>>
#include <<x>iostream<x>>
#include <<x>raspicam/raspicam_cv.h<x>>
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
     
using namespace cv;
using namespace std;
     
int main(int argc, char **argv)
{
  int threshold = 100;
  const int frameDelay = 100, maxContours = 500;
      
  raspicam::RaspiCam_Cv cam;
  Mat image;
  //set camera params, CV_8UC1 grayscale, CV_8UC3 colored
  cam.set(CV_CAP_PROP_FORMAT, CV_8UC1);
  if (!cam.open())
    return 1;
     
  const char szSourceWindow[] = "Source", szContoursWindow[] = "Contours";
  namedWindow(szSourceWindow, WINDOW_AUTOSIZE);
  namedWindow(szContoursWindow, WINDOW_AUTOSIZE);
  createTrackbar("Threshold:", szSourceWindow, &threshold, 255, NULL);
    
  for (;;)
  {
    RNG rng(12345);
    cam.grab();
    cam.retrieve(image);
    Mat smallImage;
    resize(image, smallImage, Size(), 0.5, 0.5);
    imshow(szSourceWindow, smallImage);
    
    Mat canny_output;
    vector<<x>vector<<x>Point<x>> <x>> contours;
    vector<<x>Vec4i<x>> hierarchy;
    Canny(smallImage, canny_output, threshold, threshold * 2, 3);
    findContours(canny_output, contours, hierarchy, RETR_TREE, CHAIN_APPROX_SIMPLE, Point(0, 0));
    
    Mat drawing = Mat::zeros(canny_output.size(), CV_8UC3);
    for (size_t i = 0; i <<x> std::min(contours.size(), (size_t)maxContours); i++)
    {
      Scalar color = Scalar(rng.uniform(0, 255), rng.uniform(0, 255), rng.uniform(0, 255));
      drawContours(drawing, contours, (int)i, color, 2, 8, hierarchy, 0, Point());
    }
    
    imshow(szContoursWindow, drawing);
    int c = waitKey(frameDelay);
    if((char)c == 'q') { 
      break; 
    }
  }
  cam.release();
}
```

Compile:

```
$ g++ -I/usr/local/include/ -g -o binary  example2.cpp -lopencv_core -lopencv_highgui -lopencv_imgproc -lraspicam -lraspicam_cv -o example2
```

Then, run the program:

```
$ ./example2
```

If all goes as expected you should have an Canny image displayed on your screen.

### Resources ###

- [https://visualgdb.com/tutorials/raspberry/opencv/camera/](https://visualgdb.com/tutorials/raspberry/opencv/camera/)!.

