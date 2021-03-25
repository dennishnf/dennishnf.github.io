
## Basic hand pose recognition system on a Raspberry Pi using CNNs ##

### Introduction ###

Hand gesture recognition is a challenging topic of research due to the increasing demands for robotics in recent years. Gesture recognition based on visual perception has many advantages over devices such as sensors, or electronic gloves. Hand gesture recognition provides users with an intuitive means of directly using their hands to interact with a robot. In addition to this, hand gestures can be applied to virtual reality environments, image/video coding, content-based image/video retrieval, and video games.

In machine learning, a convolutional neural network (CNN, or ConvNet) is a class of deep, feed-forward artificial neural networks that has successfully been applied to analyzing visual imagery. CNNs use relatively little pre-processing compared to other image classification algorithms. This means that the network learns the filters that in traditional algorithms were hand-engineered. This independence from prior knowledge and human effort in feature design is a major advantage.

### Implementation ###

The model for hand pose classification that will be used in this project is a trained convolutional neural network, whose parameters and weights were obtained after training step. The training phase is show in the Figure 1. This training is performed usig the Caffe framework. The design and layers of the trained model is described in the ```.prototxt``` file and the parameters of this training is contained in the ```.caffemodel``` file.

![image](/posts/projects/2017-05_basic-hand-pose-recognition-system-on-a-raspberry-pi-using-cnns/step1-training.jpg)
<p style="text-align:center;"><i>Figure 1: Training phase</i></p>

After training step, the ```.prototxt``` and ```.caffemodel``` files will be used on the Raspberry Pi in order to perform inference. The Figure 2 shows the inference step.

![image](/posts/projects/2017-05_basic-hand-pose-recognition-system-on-a-raspberry-pi-using-cnns/step2-inference.jpg)
<p style="text-align:center;"><i>Figure 2: Inference phase</i></p>

Since hand region is usually exposed to different conditions such as luminance variations and skin tone, a pre-processing step is needed to extract the hand in order to perform correct classification of hand poses. So, a RGB-Binary conversion based on skin thresholding is used to extract hand region. This pre-processing step will be applied to the RGB images (captured from camera) before going through the convolutional neural network. The procedure described above is showed in the Figure 3.

![image](/posts/projects/2017-05_basic-hand-pose-recognition-system-on-a-raspberry-pi-using-cnns/schema.png)
<p style="text-align:center;"><i>Figure 3: Basic schema of pre-processing step and classification</i></p>

The total number of classes used for classification will be five and are composed by simple hand gestures such as open hand or simple shapes formed with the fingers. These hand poses used for classification is showed in the Figure 4. Furthermore, binary images will be used as input of the convolutional neural network for training, testing and inference.

![image](/posts/projects/2017-05_basic-hand-pose-recognition-system-on-a-raspberry-pi-using-cnns/hand_poses.png)
<p style="text-align:center;"><i>Figure 4: RGB and binary images of the hand poses</i></p>

The architecture of the simple CNN used in this project is illustrated in the Figure 5. This architecture is similar to LeNet-5 architecture. This basic arhitecture was taken as reference due the ability to process higher resolution images requires larger and more convolutional layers, so this technique is constrained by the limited availability of computing resources. As the figure shows, this proposed architecture is composed of two convolutional layers, two sub-sampling layers and three simple full-conection layers.

![image](/posts/projects/2017-05_basic-hand-pose-recognition-system-on-a-raspberry-pi-using-cnns/cnn.png)
<p style="text-align:center;"><i>Figure 5: Architecture of the Convolutional Neural Network used for Hand Pose Detection</i></p>

The total number of images is 41400 and is composed by 7 persons (from Person 1 to 7). These hand poses have different shapes, rotations, shiftings, and scales in order to obtain a robust model able to deal with different conditions for hand pose classification in real time. In this project person-independent testing will be performed. So, Person 3 will be used for testing and Person 1, 2, 4, 5, 6, 7 will be used for training. Therefore, 36000 images for training and 5400 for testing.

After training and testing prediction statistics are evaluated in order to analyse the correct classification of the trained model. As mentioned above, Person 3 is used to peform person-independent testing. The accuracy of the recognition system is the mean value of 10 iterations. This mean value and other parameters are show in the Figure 6. The performance of the recognition system shows an accuracy of 86.5% since the neural network is small and the binary images used for training does not give important information for feature extraction of the convolutional neural network.

![image](/posts/projects/2017-05_basic-hand-pose-recognition-system-on-a-raspberry-pi-using-cnns/accuracy.png)
<p style="text-align:center;"><i>Figure 6: Accuracy using 10 iterations (10 tests)</i></p>

Despite the wrong classification of the trained model for some classes, the accuracy is high and allows the correct classification of hand poses. In addition to this, testing phase shows good processing time, wich is about 2.6 ms for a single image. It should be noted that it was implemented on a laptop machine with good computational resources (8 cores @ 2.80GHz). So, this allows the implementation in real-time. However, when using the Raspberry Pi for deep learning we have two major pitfalls working against us:

- Restricted memory (only 1GB on the Raspberry Pi 3).

- Limited processor speed (four ARM Cortex-A53 core running at 1.2GHz on the Raspberry Pi 3).

This makes it difficult to use larger, deeper neural networks on this platform such as GoogleNet network. On the other hand, the model used in this project for hand pose classification is simple and composed only by 2 convolutional layers. Furthermore, the testing step shows 2.6 ms for classification of a single image. Therefore, implementation of the model on the Raspberry Pi can be performed in real-time.

The stream video is obtained using the Pi Camera module and using the Raspicam library. Then, the Raspberry Pi platforms classification using the trained model. This classification for each captured image is realized using the deep neuronal libraries of OpenCV 3.3.0, which alllows the inference of trained caffe models. In addition, this implementation was performed completely in C++. A basic scheme of the recognition system is presented in the Figure 7 and show the input and output signals:

![image](/posts/projects/2017-05_basic-hand-pose-recognition-system-on-a-raspberry-pi-using-cnns/diagram.png)
<p style="text-align:center;"><i>Figure 7: Basic scheme of the recognition system</i></p>

Figure 8 shows the scenario to perform hand pose classification which is composed by Raspberry Pi 3 and the Raspberry Camera as well as a well-lit environment.

![image](/posts/projects/2017-05_basic-hand-pose-recognition-system-on-a-raspberry-pi-using-cnns/photo_raspberry.jpg)
<p style="text-align:center;"><i>Figure 8: Photo of the recognition system</i></p>

### Results ###

As the video shows, the recognition of hand poses is performed in real-time. The hand should be put inside the red square and the wrist position should be around the small red circle (located inside the red square). Then, hand region is extracted using a simple skin detector and this hand region is show in the "Hand" window. The binary image of the hand is used as input of the convolutional neural network to perform hand pose classification. This video shows robustness of the trained model to small rotations and shiftings as well as stability. In addition, the time to single image classification is good and take about 5.6 miliseconds (average from 10 iterations).

![image](/posts/projects/2017-05_basic-hand-pose-recognition-system-on-a-raspberry-pi-using-cnns/poses_reference.png)
<p style="text-align:center;"><i>Figure 9: Hand poses and labels</i></p>

![video](/posts/projects/2017-05_basic-hand-pose-recognition-system-on-a-raspberry-pi-using-cnns/gesturedetector.mp4)
<p style="text-align:center;"><i>Hand pose recognition in real-time running on a Raspberry Pi</i></p>

### Conclusions ###

To sum up, a hand pose detector was implemented in real-time on a Raspberry Pi platform. The testing phase show an accuracy of 86.5% for the classification of 5 hand poses. In addition to this, the time used to perform the image classification for each image is about 5.6 ms. The accuracy can be improved by adding more training images, adding filters or image transormations in pre-processing step as well as adding mode convolutional layers and tunning the model. Also, additional techniques for skin detection can be added in order to have a better hand pose detector.


