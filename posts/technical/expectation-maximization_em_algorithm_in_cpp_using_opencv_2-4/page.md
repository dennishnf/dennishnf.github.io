
## Using the Expectation Maximization (EM) algorithm in C++ using OpenCV 2.4 ##

The Expectation Maximization(EM) algorithm estimates the parameters of the multivariate probability density function in the form of a Gaussian mixture distribution with a specified number of mixtures.

### Background extraction using EM algorithm ###

OpenCV 2.4.9 will be used in this example. The next image will be classify in foreground and background using the EM algorithm.

![image](/posts/technical/expectation-maximization_em_algorithm_in_cpp_using_opencv_2-4/test-example_em.jpg)

Create a file ```example_em.cpp```:

```
#include <<x>opencv2/opencv.hpp<x>>
#include <<x>opencv2/legacy/legacy.hpp<x>>
    
int main(int argc, char** argv) {
    
    cv::Mat source = cv::imread("12_test-example_em.jpg");
    
    //ouput images
    cv::Mat meanImg(source.rows, source.cols, CV_32FC3);
    cv::Mat fgImg(source.rows, source.cols, CV_8UC3);
    cv::Mat bgImg(source.rows, source.cols, CV_8UC3);
    
    //convert the input image to float
    cv::Mat floatSource;
    source.convertTo(floatSource, CV_32F);
    
    //now convert the float image to column vector
    cv::Mat samples(source.rows * source.cols, 3, CV_32FC1);
    int idx = 0;
    for (int y = 0; y <<x> source.rows; y++) {
        cv::Vec3f* row = floatSource.ptr<<x>cv::Vec3f <x>> (y);
        for (int x = 0; x <<x> source.cols; x++) {
            samples.at<<x>cv::Vec3f <x>> (idx++, 0) = row[x];
        }
    }
    
    //we need just 2 clusters
    cv::EMParams params(2);
    cv::ExpectationMaximization em(samples, cv::Mat(), params);
    
    //the two dominating colors
    cv::Mat means = em.getMeans();
    //the weights of the two dominant colors
    cv::Mat weights = em.getWeights();
    
    //we define the foreground as the dominant color with the largest weight
    const int fgId = weights.at<<x>float<x>>(0) <x>> weights.at<<x>float<x>>(1) ? 0 : 1;
    
    //now classify each of the source pixels
    idx = 0;
    for (int y = 0; y <<x> source.rows; y++) {
        for (int x = 0; x <<x> source.cols; x++) {
            
            //classify
            const int result = cvRound(em.predict(samples.row(idx++), NULL));
            //get the according mean (dominant color)
            const double* ps = means.ptr<<x>double<x>>(result, 0);
            
            //set the according mean value to the mean image
            float* pd = meanImg.ptr<<x>float<x>>(y, x);
            //float images need to be in [0..1] range
            pd[0] = ps[0] / 255.0;
            pd[1] = ps[1] / 255.0;
            pd[2] = ps[2] / 255.0;
            
            //set either foreground or background
            if (result == fgId) {
                fgImg.at<<x>cv::Point3_<<x>uchar<x>> <x>>(y, x, 0) = source.at<<x>cv::Point3_<<x>uchar<x>> <x>>(y, x, 0);
            } else {
                bgImg.at<<x>cv::Point3_<<x>uchar<x>> <x>>(y, x, 0) = source.at<<x>cv::Point3_<<x>uchar<x>> <x>>(y, x, 0);
            }
        }
    }
     
    cv::imshow("Means", meanImg);
    cv::imshow("Foreground", fgImg);
    cv::imshow("Background", bgImg);
    cv::waitKey(0);
     
    return 0;
}
```

Then, compile using:

```
g++ -I/usr/local/include/opencv -I/usr/local/include/opencv2 -L/usr/local/lib/ -g -o binary  example_em.cpp -lopencv_core -lopencv_imgproc -lopencv_highgui -lopencv_legacy -o example_em
```

Finally, run using:

```
./example_em
```

The command above should show the next result:

![image](/posts/technical/expectation-maximization_em_algorithm_in_cpp_using_opencv_2-4/result-example_em.png)

### Resources ###

- [https://docs.opencv.org/2.4/modules/ml/doc/expectation_maximization.html](https://docs.opencv.org/2.4/modules/ml/doc/expectation_maximization.html)!.
