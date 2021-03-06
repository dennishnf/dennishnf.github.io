
## Object tracking using OpenCV 3.3.0 and C++/Python ##

OpenCV 3 comes with a new tracking API that contains implementations of many single object tracking algorithms. There are 6 different trackers available in OpenCV 3.2 — BOOSTING, MIL, KCF, TLD, MEDIANFLOW, and GOTURN. as mentioned before, OpenCV 3.x has tracking libraries and is easy to implement object tracking using several approaches. The code shows as follow is included here: [[https://dennishnf.github.io/posts/technical/2017-12_object_tracking_using_opencv_3-3-0_and_cpp_pyhon/example_tracking.zip](link)!].

We then open a video and grab a frame. We define a bounding box containing the object for the first frame and initialize the tracker with the first frame and the bounding box. Finally, we read frames from the video and just update the tracker in a loop to obtain a new bounding box for the current frame. Results are subsequently displayed.

### C++ ###

```
#include <<x>opencv2/opencv.hpp<x>>
#include <<x>opencv2/tracking.hpp<x>>
#include <<x>opencv2/core/ocl.hpp<x>>
       
using namespace cv;
using namespace std;
        
// Convert to string
#define SSTR( x ) static_cast<<x> std::ostringstream & <x>>( \
( std::ostringstream() <<x><<x> std::dec <<x><<x> x ) ).str()
     
int main(int argc, char **argv)
{
    // List of tracker types in OpenCV 3.2
    // NOTE : GOTURN implementation is buggy and does not work.
    string trackerTypes[6] = {"BOOSTING", "MIL", "KCF", "TLD","MEDIANFLOW", "GOTURN"};
    // vector <<x>string<x>> trackerTypes(types, std::end(types));
        
    // Create a tracker
    string trackerType = trackerTypes[2];
        
    Ptr<<x>Tracker<x>> tracker;
        
    #if (CV_MINOR_VERSION <<x> 3)
    {
        tracker = Tracker::create(trackerType);
    }
    #else
    {
        if (trackerType == "BOOSTING")
            tracker = TrackerBoosting::create();
        if (trackerType == "MIL")
            tracker = TrackerMIL::create();
        if (trackerType == "KCF")
            tracker = TrackerKCF::create();
        if (trackerType == "TLD")
            tracker = TrackerTLD::create();
        if (trackerType == "MEDIANFLOW")
            tracker = TrackerMedianFlow::create();
        if (trackerType == "GOTURN")
            tracker = TrackerGOTURN::create();
    }
    #endif
    // Read video
    VideoCapture video("videos/chaplin.mp4");
     
    // Exit if video is not opened
    if(!video.isOpened())
    {
        cout <<x><<x> "Could not read video file" <<x><<x> endl;
        return 1;
                
    }
            
    // Read first frame
    Mat frame;
    bool ok = video.read(frame);
            
    // Define initial boundibg box
    Rect2d bbox(287, 23, 86, 320);
     
    // Uncomment the line below to select a different bounding box
    bbox = selectROI(frame, false);
        
    // Display bounding box.
    rectangle(frame, bbox, Scalar( 255, 0, 0 ), 2, 1 );
    imshow("Tracking", frame);
     
    tracker-<x>>init(frame, bbox);
     
    while(video.read(frame))
    {
        // Start timer
        double timer = (double)getTickCount();
         
        // Update the tracking result
        bool ok = tracker-<x>>update(frame, bbox);
         
        // Calculate Frames per second (FPS)
        float fps = getTickFrequency() / ((double)getTickCount() - timer);
         
        if (ok)
        {
            // Tracking success : Draw the tracked object
            rectangle(frame, bbox, Scalar( 255, 0, 0 ), 2, 1 );
        }
        else
        {
            // Tracking failure detected.
            putText(frame, "Tracking failure detected", Point(100,80), FONT_HERSHEY_SIMPLEX, 0.75, Scalar(0,0,255),2);
        }
         
        // Display tracker type on frame
        putText(frame, trackerType + " Tracker", Point(100,20), FONT_HERSHEY_SIMPLEX, 0.75, Scalar(50,170,50),2);
         
        // Display FPS on frame
        putText(frame, "FPS : " + SSTR(int(fps)), Point(100,50), FONT_HERSHEY_SIMPLEX, 0.75, Scalar(50,170,50), 2);
        
        // Display frame.
        imshow("Tracking", frame);
         
        // Exit if ESC pressed.
        int k = waitKey(1);
        if(k == 27)
        {
            break;
        }
     
    }
}
```

### Python ###

```
import cv2
import sys
     
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
      
if __name__ == '__main__' :
    
    # Set up tracker.
    # Instead of MIL, you can also use
    
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN']
    tracker_type = tracker_types[2]
    
    if int(minor_ver) <<x> 3:
        tracker = cv2.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()
      
    # Read video
    video = cv2.VideoCapture("videos/chaplin.mp4")
    
    # Exit if video not opened.
    if not video.isOpened():
        print "Could not open video"
        sys.exit()
     
    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print 'Cannot read video file'
        sys.exit()
      
    # Define an initial bounding box
    bbox = (287, 23, 86, 320)
    
    # Uncomment the line below to select a different bounding box
    bbox = cv2.selectROI(frame, False)
    
    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)
    
    while True:
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break
         
        # Start timer
        timer = cv2.getTickCount()
        
        # Update tracker
        ok, bbox = tracker.update(frame)
        
        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
        
        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
            
        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
        
        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        
        # Display result
        cv2.imshow("Tracking", frame)
        
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
        
```

### Results in C++ and Python ###

![image](/posts/technical/2017-12_object_tracking_using_opencv_3-3-0_and_cpp_pyhon/tracking.gif)

### Resources ###

- [https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/](https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/)!.

