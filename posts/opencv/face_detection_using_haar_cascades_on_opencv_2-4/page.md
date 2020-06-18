
## Face detection using Haar Cascades on OpenCV 2.4 ##

Create a folder ```facedetector```. In this folder open up a new file, name it ```facedetector.cpp```, and insert the following code (the files ```facedetector.cpp``` and ```haarcascade_frontalface_alt.xml``` are included in this [[https://dennishnf.bitbucket.io/posts/opencv/face_detection_using_haar_cascades_on_opencv_2-4/face_detector.zip](link)!]:

```
#include <<x>opencv2/opencv.hpp<x>>
#include <<x>opencv2/objdetect/objdetect.hpp<x>>
#include <<x>opencv2/highgui/highgui.hpp<x>>
#include <<x>opencv2/imgproc/imgproc.hpp<x>>
#include <<x>opencv2/legacy/legacy.hpp<x>>
#include <<x>iostream<x>>
#include <<x>stdio.h<x>>
     
using namespace std;
using namespace cv;
     
//global variables
String cascade_name = "haarcascade_frontalface_alt.xml";
CascadeClassifier cascade;
     
     
//main function
int main(int argc, const char** argv)
{
     
  CvCapture* capture;
  Mat frame;
  Mat frameout;
    
  //load the cascades
  if(!cascade.load(cascade_name)){
    printf("--(!)Error loading\n"); 
    return -1; 
  }
     
  //read the video stream
  capture = cvCaptureFromCAM(-1);
    
  if(capture)  {
     
    while(true)  {
       
      frame = cvQueryFrame(capture);
      
      if(!frame.empty()) {
      }
      else {
        printf(" --(!) No captured frame -- Break!"); 
        break;
      }
      
      //FACE DETECTION
      std::vector<<x>Rect<x>> faces;
      Mat frame_gray;
      
      cvtColor( frame, frame_gray, CV_BGR2GRAY );
      equalizeHist( frame_gray, frame_gray );
      
      cascade.detectMultiScale( frame_gray, faces, 1.1, 2, 0|CV_HAAR_SCALE_IMAGE, Size(30, 30) );
      
      for( size_t i = 0; i <<x> faces.size(); i++ ) {
        int point1x =  faces[i].x;
        int point1y = faces[i].y;
        int lengthxy = faces[i].width;
        rectangle(frame, Point(point1x,point1y), Point(point1x+lengthxy,point1y+lengthxy), Scalar(0,0,255), 1, 8, 0 );
        imshow("Face detection", frame );
      }
      
      int c = waitKey(10);
      if((char)c == 'q') { 
        break; 
      }
    
    }
  }
    
  return 0;
     
}
```

Then, compile:

```
g++ -I/usr/local/include/opencv -I/usr/local/include/opencv2 -L/usr/local/lib/ -g -o binary  facedetector.cpp -lopencv_core -lopencv_imgproc -lopencv_highgui -lopencv_ml -lopencv_imgproc -lopencv_video -lopencv_features2d -lopencv_calib3d -lopencv_objdetect -lopencv_contrib -lopencv_legacy -lopencv_stitching -o facedetector
```

Finally, run the program:

```
$ ./facedetector
```

The command above should show the next result:

![image](/posts/opencv/face_detection_using_haar_cascades_on_opencv_2-4/facedetector.png)


