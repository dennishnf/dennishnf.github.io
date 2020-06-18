
## Train Haar and LBP cascades using OpenCV ##

### Step 1 : Data Collection ###

Before we begin a project, we always try to get the data right because a superior algorithm will never be able to fix a bad data problem. Our data collection team collected approximately 1000 images of human eyes. We also gathered around 7000 negative images randomly from the internet.

You can use [https://code.google.com/archive/p/imageclipper/](ImageClipper)! to cut the images.

Collect images of the object you want to detect, crop them to some fixed aspect ratio and put these images in the positive_images folder. For example, we collected 1000 images of eyes, cropped them into square images and put them in the positive_images directory. Similarly, collect a large set of negative examples, crop them in the same aspect ratio as the positive samples, and put them in a directory named negative_images.

There is no obvious rule for positive/negative ratio. Normally I add around twice as much negative samples than positive ones, but never less than that. And it makes sense because any classifier will give much more negative responses than positive ones on a common scenario.

### Step 2 : Create Training Data files ###

You need to create text files postives.txt and negatives.txt using the commands below:

```
$ find ./negative_images -iname "*.jpg" > negatives.txt
$ find ./positive_images -iname "*.jpg" > positives.txt
```

### Step 3: Create Samples ###

1st: Use createsamples.pl to create .vec file for each image:

```
$ perl bin/createsamples.pl positives.txt negatives.txt samples 5000 "opencv_createsamples -bgcolor 0 -bgthresh 0 -maxxangle 1.1 -maxyangle 1.1 maxzangle 0.5 -maxidev 40 -w 40 -h 40"
```

The script is a wrapper around opencv_createsamples. As mentioned in the OpenCV documentation.

opencv_createsamples is used to prepare a training dataset of positive and test samples. opencv_createsamples produces dataset of positive samples in a format that is supported by both opencv_haartraining and opencv_traincascade applications. The output is a file with *.vec extension, it is a binary format which contains images.

2nd: Use mergevec.py to merge .vec files into samples.vec like this:

```
$ python ./tools/mergevec.py -v samples/ -o samples.vec
```

### Step 4: Run Training Scripts ###

- LBP Cascades: are much faster than Haar but is less accurate. You can train using the following command:

```
$ opencv_traincascade -data lbp -vec samples.vec -bg negatives.txt -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 4000 -numNeg 7000 -w 40 -h 40 -mode ALL -precalcValBufSize 4096 -precalcIdxBufSize 4096 -featureType LBP
```

- Haar Cascades: take a long time to train, but are definitely more accurate. You can train a Haar cascade using the following command:

```
$ opencv_traincascade -data haar -vec samples.vec -bg negatives.txt -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 4000 -numNeg 7000 -w 40 -h 40 -mode ALL -precalcValBufSize 4096 -precalcIdxBufSize 4096
```



### Resources ###

- [https://www.learnopencv.com/training-better-haar-lbp-cascade-eye-detector-opencv/](https://www.learnopencv.com/training-better-haar-lbp-cascade-eye-detector-opencv/)! .

- [http://answers.opencv.org/question/98754/how-to-train-classifiers-the-best-way-possible/](http://answers.opencv.org/question/98754/how-to-train-classifiers-the-best-way-possible/)! .

- [https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html](https://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html)! .


