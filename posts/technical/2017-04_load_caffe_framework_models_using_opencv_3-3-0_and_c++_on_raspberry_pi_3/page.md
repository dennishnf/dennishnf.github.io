
## Load Caffe framework models using OpenCV 3.3.0 and C++ on Raspberry Pi 3 ##

### Connect to RPI with SSH and Xephyr ###

We will use Raspbian Jessie.

First, on Ubuntu:

```
$ Xephyr -ac -br -keybd ephyr,,,xkbmodel=pc105,xkblayout=es -noreset -screen 1280x720 :1
```

Then, on RPI:

```
$ DISPLAY=:1 ssh -Y pi@10.42.0.246
$ startlxde
```

### Load Caffe framework models using OpenCV ###

In this tutorial you will learn how to use opencv_dnn module for image classification by using GoogLeNet trained network from Caffe model zoo.

We will demonstrate results of this example on the following picture.

![image](/posts/technical/2017-04_load_caffe_framework_models_using_opencv_3-3-0_and_c++_on_raspberry_pi_3/space_shuttle.jpg)

### Source Code ###

We will be using the next code, that can be downloaded here: [[https://dennishnf.github.io/posts/technical/2017-04_load_caffe_framework_models_using_opencv_3-3-0_and_c++_on_raspberry_pi_3/caffe_googlenet.zip](link)!].

```
#include <<x>opencv2/dnn.hpp<x>>
#include <<x>opencv2/imgproc.hpp<x>>
#include <<x>opencv2/highgui.hpp<x>>
#include <<x>opencv2/core/utils/trace.hpp<x>>
using namespace cv;
using namespace cv::dnn;
     
#include <<x>fstream<x>>
#include <<x>iostream<x>>
#include <<x>cstdlib<x>>
using namespace std;
     
/* Find best class for the blob (i. e. class with maximal probability) */
static void getMaxClass(const Mat &probBlob, int *classId, double *classProb)
{
    Mat probMat = probBlob.reshape(1, 1); //reshape the blob to 1x1000 matrix
    Point classNumber;
    
    minMaxLoc(probMat, NULL, classProb, NULL, &classNumber);
    *classId = classNumber.x;
}
     
static std::vector<<x>String<x>> readClassNames(const char *filename = "synset_words.txt")
{
    std::vector<<x>String<x>> classNames;
    
    std::ifstream fp(filename);
    if (!fp.is_open())
    {
        std::cerr <<x><<x> "File with classes labels not found: " <<x><<x> filename <<x><<x> std::endl;
        exit(-1);
    }
    
    std::string name;
    while (!fp.eof())
    {
        std::getline(fp, name);
        if (name.length())
            classNames.push_back( name.substr(name.find(' ')+1) );
    }
    
    fp.close();
    return classNames;
}
     
int main(int argc, char **argv)
{
    CV_TRACE_FUNCTION();
     
    String modelTxt = "bvlc_googlenet.prototxt";
    String modelBin = "bvlc_googlenet.caffemodel";
    String imageFile = (argc <x>> 1) ? argv[1] : "space_shuttle.jpg";
     
    Net net;
    try {
        //! [Read and initialize network]
        net = dnn::readNetFromCaffe(modelTxt, modelBin);
        //! [Read and initialize network]
    }
    catch (cv::Exception& e) {
        std::cerr <<x><<x> "Exception: " <<x><<x> e.what() <<x><<x> std::endl;
        //! [Check that network was read successfully]
        if (net.empty())
        {
            std::cerr <<x><<x> "Can't load network by using the following files: " <<x><<x> std::endl;
            std::cerr <<x><<x> "prototxt:   " <<x><<x> modelTxt <<x><<x> std::endl;
            std::cerr <<x><<x> "caffemodel: " <<x><<x> modelBin <<x><<x> std::endl;
            std::cerr <<x><<x> "bvlc_googlenet.caffemodel can be downloaded here:" <<x><<x> std::endl;
            std::cerr <<x><<x> "http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel" <<x><<x> std::endl;
            exit(-1);
        }
        //! [Check that network was read successfully]
    }
     
    //! [Prepare blob]
    Mat img = imread(imageFile);
    if (img.empty())
    {
        std::cerr <<x><<x> "Can't read image from the file: " <<x><<x> imageFile <<x><<x> std::endl;
        exit(-1);
    }
     
    //GoogLeNet accepts only 224x224 BGR-images
    Mat inputBlob = blobFromImage(img, 1.0f, Size(224, 224),
                                  Scalar(104, 117, 123), false);   //Convert Mat to batch of images
    //! [Prepare blob]
     
    Mat prob;
    cv::TickMeter t;
    for (int i = 0; i <<x> 10; i++)
    {
        CV_TRACE_REGION("forward");
        //! [Set input blob]
        net.setInput(inputBlob, "data");        //set the network input
        //! [Set input blob]
        t.start();
        //! [Make forward pass]
        prob = net.forward("prob");                          //compute output
        //! [Make forward pass]
        t.stop();
    }
     
    //! [Gather output]
    int classId;
    double classProb;
    getMaxClass(prob, &classId, &classProb);//find the best class
    //! [Gather output]
     
    //! [Print results]
    std::vector<<x>String<x>> classNames = readClassNames();
    std::cout <<x><<x> "Best class: #" <<x><<x> classId <<x><<x> " '" <<x><<x> classNames.at(classId) <<x><<x> "'" <<x><<x> std::endl;
    std::cout <<x><<x> "Probability: " <<x><<x> classProb * 100 <<x><<x> "%" <<x><<x> std::endl;
    //! [Print results]
    std::cout <<x><<x> "Time: " <<x><<x> (double)t.getTimeMilli() / t.getCounter() <<x><<x> " ms (average from " <<x><<x> t.getCounter() <<x><<x> " iterations)" <<x><<x> std::endl;
     
    return 0;
} //main
```

### Explanation ###

1. Firstly:

Download GoogLeNet model files: bvlc_googlenet.prototxt and bvlc_googlenet.caffemodel.

Also you need file with names of ILSVRC2012 classes: synset_words.txt.

Put these files into working dir of this program example.

2. Read and initialize network using path to .prototxt and .caffemodel files:

```
Net net = dnn::readNetFromCaffe(modelTxt, modelBin);
```

3. Check that network was read successfully:

```
if (net.empty())
{
    std::cerr <<x><<x> "Can't load network by using the following files: " <<x><<x> std::endl;
    std::cerr <<x><<x> "prototxt:   " <<x><<x> modelTxt <<x><<x> std::endl;
    std::cerr <<x><<x> "caffemodel: " <<x><<x> modelBin <<x><<x> std::endl;
    std::cerr <<x><<x> "bvlc_googlenet.caffemodel can be downloaded here:" <<x><<x> std::endl;
    std::cerr <<x><<x> "http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel" <<x><<x> std::endl;
    exit(-1);
}
```

4. Read input image and convert to the blob, acceptable by GoogleNet:

```
Mat img = imread(imageFile);
if (img.empty())
{
    std::cerr <<x><<x> "Can't read image from the file: " <<x><<x> imageFile <<x><<x> std::endl;
    exit(-1);
}
    
//GoogLeNet accepts only 224x224 BGR-images
Mat inputBlob = blobFromImage(img, 1.0f, Size(224, 224),
                              Scalar(104, 117, 123), false);   //Convert Mat to batch of images
```

Firstly, we resize the image and change its channel sequence order.

Now image is actually a 3-dimensional array with 224x224x3 shape.

Next, we convert the image to 4-dimensional blob (so-called batch) with 1x3x224x224 shape by using special cv::dnn::Blob::fromImages constructor.

5. Pass the blob to the network:

```
net.setInput(inputBlob, "data");        //set the network input
```

In bvlc_googlenet.prototxt the network input blob named as "data", therefore this blob labeled as ".data" in opencv_dnn API.

Other blobs labeled as "name_of_layer.name_of_layer_output".

6. Make forward pass:

```
prob = net.forward("prob");                          //compute output
```

During the forward pass output of each network layer is computed, but in this example we need output from "prob" layer only.

7. Determine the best class:

```
int classId;
double classProb;
getMaxClass(prob, &classId, &classProb);//find the best class
```

We put the output of "prob" layer, which contain probabilities for each of 1000 ILSVRC2012 image classes, to the prob blob. And find the index of element with maximal value in this one. This index correspond to the class of the image.

8. Print results:

```
std::vector<<x>String<x>> classNames = readClassNames();
std::cout <<x><<x> "Best class: #" <<x><<x> classId <<x><<x> " '" <<x><<x> classNames.at(classId) <<x><<x> "'" <<x><<x> std::endl;
std::cout <<x><<x> "Probability: " <<x><<x> classProb * 100 <<x><<x> "%" <<x><<x> std::endl;
```

### Compile ###

Compile using the ```Makefile```:

```
CC = g++
CFLAGS = -g -Wall
SRCS = caffe_googlenet.cpp
PROG = caffe_googlenet
     
OPENCV_LIBS = /usr/local
     
OPENCV = -I$(OPENCV_LIBS)/include/opencv -I$(OPENCV_LIBS)/include \
$(OPENCV_LIBS)/lib/libopencv_calib3d.so $(OPENCV_LIBS)/lib/libopencv_core.so \
$(OPENCV_LIBS)/lib/libopencv_features2d.so $(OPENCV_LIBS)/lib/libopencv_flann.so \
$(OPENCV_LIBS)/lib/libopencv_highgui.so $(OPENCV_LIBS)/lib/libopencv_imgproc.so \
$(OPENCV_LIBS)/lib/libopencv_ml.so $(OPENCV_LIBS)/lib/libopencv_objdetect.so \
$(OPENCV_LIBS)/lib/libopencv_photo.so $(OPENCV_LIBS)/lib/libopencv_stitching.so \
$(OPENCV_LIBS)/lib/libopencv_superres.so $(OPENCV_LIBS)/lib/libopencv_video.so \
$(OPENCV_LIBS)/lib/libopencv_videostab.so $(OPENCV_LIBS)/lib/libopencv_dnn.so \
$(OPENCV_LIBS)/lib/libopencv_imgcodecs.so 
     
LIBS = $(OPENCV)
     
$(PROG):$(SRCS)
	$(CC) $(CFLAGS) -o $(PROG) $(SRCS) $(LIBS)
```

Then, compile:

```
$ make
```

### Run ###

Finally, run with:

```
$ ./caffe_googlenet
```

After run the program, this should show:

```
Best class: #812 'space shuttle'
Probability: 99.9935%
Time: 3259.15 ms (average from 10 iterations)
```

Also, you can use:

```
$ ./caffe_googlenet you_image_file.png
```

### Resources ###

- [https://docs.opencv.org/3.3.0/d5/de7/tutorial_dnn_googlenet.html](https://docs.opencv.org/3.3.0/d5/de7/tutorial_dnn_googlenet.html)!.

