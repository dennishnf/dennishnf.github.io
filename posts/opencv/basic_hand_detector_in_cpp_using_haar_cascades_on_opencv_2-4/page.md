
## Basic hand detector in C++ using Haar cascades on OpenCV 2.4 ##

Implemented in OpenCV 2.4.x and 3.x. In the next link you can find the pre trained .xml file (created after training the Haar cascades classifier) that will be used to implement the hand detector: [[https://dennishnf.bitbucket.io/posts/technical/opencv/basic_hand_detector_in_cpp_using_haar_cascades_on_opencv_2-4/hand_detector.zip](link)!].

### Code ###

Create a the ```hand_detectop.cpp``` and fill in with the next content:

```
#include <<x>opencv2/imgproc/imgproc.hpp<x>>
#include <<x>opencv2/highgui/highgui.hpp<x>>
#include <<x>opencv2/objdetect/objdetect.hpp<x>>
#include <<x>iostream<x>>
#include <<x>stdio.h<x>>
     
using namespace cv;
using namespace std;
      
Mat img;
     
vector<<x>Rect<x>> hands;
     
CascadeClassifier Hand;
     
int main()
{
  VideoCapture cap(0);
  char ch;
  namedWindow("Hand detection",CV_WINDOW_NORMAL);
  Hand.load("hand.xml");
  while(true)
  {
    cap<x>><x>>img;
    Hand.detectMultiScale(img,hands,1.1,3,0|CV_HAAR_FIND_BIGGEST_OBJECT,Size(30,30));
    for(size_t  i=0; i <<x> hands.size() ; i++)
    {
       int point1x =  hands[i].x;
       int point1y = hands[i].y;
       int lengthxy = hands[i].width;
       rectangle(img, Point(point1x,point1y), Point(point1x+lengthxy,point1y+lengthxy), Scalar(0,0,255), 1, 8, 0 );
       imshow("Hand detection", img );
     }  
    imshow("Hand detection",img);
    ch=waitKey(1);
    if(ch==27)
    { break; }  
  }
return 0;
}
```

### Compilation and execution ###

Create the ```Makefile``` and fill in with the next content:

```
CC = g++
CFLAGS = -g -Wall
SRCS = hand_detector.cpp
PROG = hand_detector
          
OPENCV_LIBS = /usr/local
      
OPENCV = -I$(OPENCV_LIBS)/include/opencv -I$(OPENCV_LIBS)/include \
$(OPENCV_LIBS)/lib/libopencv_calib3d.so $(OPENCV_LIBS)/lib/libopencv_core.so \
$(OPENCV_LIBS)/lib/libopencv_features2d.so $(OPENCV_LIBS)/lib/libopencv_flann.so \
$(OPENCV_LIBS)/lib/libopencv_highgui.so $(OPENCV_LIBS)/lib/libopencv_imgproc.so \
$(OPENCV_LIBS)/lib/libopencv_ml.so $(OPENCV_LIBS)/lib/libopencv_objdetect.so \
$(OPENCV_LIBS)/lib/libopencv_photo.so $(OPENCV_LIBS)/lib/libopencv_stitching.so \
$(OPENCV_LIBS)/lib/libopencv_superres.so $(OPENCV_LIBS)/lib/libopencv_video.so \
$(OPENCV_LIBS)/lib/libopencv_videostab.so
      
LIBS = $(OPENCV)
      
$(PROG):$(SRCS)
	$(CC) $(CFLAGS) -o $(PROG) $(SRCS) $(LIBS)
```

Then, compile with:

```
$ make
```

FInally, execute the created file with:

```
$ ./hand_detectop
```



