
## Real-time hand gesture recognition on a PC and Raspberry Pi using Deep Learning ##

### Introduction ###

Hand gesture recognition is a challenging topic of research due to the increasing demands for robotics in recent years. Gesture recognition based on visual perception has many advantages over devices such as sensors, or electronic gloves. Hand gesture recognition provides users with an intuitive means of directly using their hands to interact with a robot. In addition to this, hand gestures can be applied to virtual reality environments, image/video coding, content-based image/video retrieval, and video games.

### Haar cascade classifier ###

The Viola–Jones object detection algorithm is the first object detection algorithm to provide competitive object detection rates in real-time proposed in 2001 by Paul Viola and Michael Jones. Although it can be trained to detect a variety of object classes, it was motivated primarily by the problem of hand detection.

This approach to hand detecting combines four key concepts:

a. Haar-like features: simple rectangular features.

b. Integral image: for rapid features detection.

c. AdaBoost: machine-learning method.

d. Cascade classifier: to combine many features efficiently.

![image](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/steps_viola_jones.jpg)
<p style="text-align:center;"><i>Figure 1: Haar cascade classifier</i></p>

### Object tracking ###

In this project, the MIL (Multiple Instance Learning) algorithm will be used for hand tracking. The MIL algorithm trains a classifier in an online manner to separate the object from the background. Multiple Instance Learning avoids the drift problem for a robust tracking. So, MIL results in a more robust and stable tracker. The implementation is based on the paper "Visual Tracking with Online Multiple Instance Learning" by B Babenko, M-H Yang, and S Belongie. In addition, tracking algorithm comummes lees memory and computational resources than the Haar cascade classifier.

![image](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/mil_tracker.png)
<p style="text-align:center;"><i>Figure 2: Using one positive bag consisting of several image patches to update a MIL classifier</i></p>

### Convolutional Neural Networks ###

In machine learning, a convolutional neural network (CNN, or ConvNet) is a class of deep, feed-forward artificial neural networks that has successfully been applied to analyzing visual imagery.

CNNs use relatively little pre-processing compared to other image classification algorithms. This means that the network learns the filters that in traditional algorithms were hand-engineered. This independence from prior knowledge and human effort in feature design is a major advantage.

A CNN consists of an input and an output layer, as well as multiple hidden layers. The hidden layers of a CNN typically consist of convolutional layers, pooling layers, fully connected layers and normalization layers.

![image](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/cnn.jpg)
<p style="text-align:center;"><i>Figure 3: Convolutional Neural Network</i></p>

### Caffe Framework ####

Caffe is a deep learning framework made with expression, speed, and modularity in mind. It is developed by Berkeley AI Research (BAIR) and by community contributors. 	Yangqing Jia created the project during his PhD at UC Berkeley. Caffe is released under the BSD 2-Clause license.

The model used in this project is the GoogleNet neural network, whose parameters and weights were obtained after training step. The training phase is show in the Figure 4. This training is performed usig the Caffe framework. The design and layers of the GoogleNet networs is described in the ```.prototxt``` file and the parameters of this training is contained in the ```.caffemodel``` file.

![image](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/step1-training.jpg)
<p style="text-align:center;"><i>Figure 4: Training phase</i></p>

After training step, the ```.prototxt``` and ```.caffemodel``` files will be used on the Raspberry Pi in order to perform inference. The Figure 5 show the inference step.

![image](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/step2-inference.jpg)
<p style="text-align:center;"><i>Figure 5: Inference phase</i></p>


### Implementation ###

The systems is composed of three main steps: hand detection, hand region tracking and hand gesture recognition. In the first step the Haar cascades classifier detects a basic hand shape in order to have a good hand detection. Then, this hand region is tracked using the MIL (Multiple Instance Learning) tracking algorithm. Finally, hand gesture recognition is performed based on a trained Convolutional Neural Network. Since the steps described before are designed to consume few computational resources, the whole system will be implemented on a personal computer and Raspberry Pi board. Figure 6 shows the steps mentioned above.

![image](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/flowchart_project.png)
<p style="text-align:center;"><i>Figure 6: Basic scheme of the hand detection system</i></p>

Haar cascade classifier allows good detection of objects with static features such as ballons, boxes, faces, eyes, mounts, noise, etc. But hand has few static features because its shape and fingers can change as well as its orientations. So, Haar cascade classifier allows detection of basic hand shapes and is not a robust technique to recognise a hand with different poses.

Since hand detection using Haar cascades in not a robust method, this deficiency is compensated with a hand tracker based on wriste region. Furthermore, wrist region is proposed for tracking due this region keeps invariant when hand changes to different poses and shapes. In addition, hand  tracking allows the reduction of the processing time since tracking requieres less compotutional resources, this is showed in the results. Figure 7 shows the different hand region used, as figure shows the tracked hand region (blue) encloses the hand in different shapes and poses.  Therefore, the hand region inside the blue box will be used by the CNN to perform hand gesture recognition.

![image](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/tracking_region.jpg)
<p style="text-align:center;"><i>Figure 7: Wrist region (red) and tracked hand region (blue)</i></p>

The total number of classes used for classification will is five and are composed by simple hand gestures such as open hand or simple shapes formed with the fingers. These hand poses used for classification is showed in the Figure 8. Since hand region is usually exposed to different conditions such as luminance variations and skin tone, a pre-processing step is needed to extract the hand in order to perform correct classification of hand poses. So, a RGB-Binary conversion based on skin thresholding is used to extract hand features before to apply the convolutional neural network classifier.

![image](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/hand_poses.png)
<p style="text-align:center;"><i>Figure 8: RGB and binary images of the hand poses</i></p>

The architecture of the simple CNN used in this project is illustrated in the Figure 9. This architecture is similar to LeNet-5 architecture. This basic arhitecture was taken as reference due the ability to process higher resolution images requires larger and more convolutional layers, so this technique is constrained by the limited availability of computing resources. As the figure shows, this proposed architecture is composed of two convolutional layers, two sub-sampling layers and three simple full-conection layers.

![image](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/cnn.png)
<p style="text-align:center;"><i>Figure 9: Architecture of the Convolutional Neural Network used for Hand Pose Detection</i></p>

The total number of images is 41400 and is composed by 7 persons (from Person 1 to 7). These hand poses have different shapes, rotations, shiftings, and scales in order to obtain a robust model able to deal with different conditions for hand pose classification in real time. In this project person-independent testing will be performed. So, Person 3 will be used for testing and Person 1, 2, 4, 5, 6, 7 will be used for training. Therefore, 36000 images for training and 5400 for testing.

After training and testing prediction statistics are evaluated in order to analyse the correct classification of the trained model. As mentioned above, Person 3 is used to peform person-independent testing. The accuracy of the recognition system is the mean value of 10 iterations. This mean value and other parameters are show in the Figure 10. The performance of the recognition system shows an accuracy of 86.5% since the neural network is small and the binary images used for training does not give important information for feature extraction of the convolutional neural network.

![image](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/accuracy.png)
<p style="text-align:center;"><i>Figure 10: Accuracy using 10 iterations (10 tests)</i></p>

The implementation of the whole system was performed in C++ and using OpenCV 3.3.0 libraries since these allow the easy realization of haar cascade classifier, object tracking and load caffe models with a good performance. Also, these libraries can be used on a personal computer as well as on different embedded computers like Beglebone and Raspberry Pi. This hand detector will be implemented on two different computers, a personal computer and a Raspberry Pi 3 board.

The implementation of this hand gesture detector on a personal computer has no problems since its computational resources. However, when using the Raspberry Pi for hand detection and tracking we have two major pitfalls working against us: restricted memory (only 1GB) and limited processor speed (four ARM Cortex-A53 core running at 1.2GHz). So, this makes it difficult to use larger, complex algorithms on this platform. However, since Haar cascades, tracking algorithm and the convolutional neural network proposed in this project are designed to consume the less amount of computational resorces, the implementation on the Raspberry Pi is feasible. A basic scheme of the recognition system is presented in the Figure 11 and show the input and output signals.

![image](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/diagram.png)
<p style="text-align:center;"><i>Figure 11: Basic scheme of the hand detection system</i></p>

### Results ###

As the videos show, the recognition of hand poses is performed in real-time. The first step consists in hand detection, then the hand region is extracted and tracked. The binary image of the hand is used as input of the convolutional neural network to perform hand pose classification. The Video 1 shows the implementation of the recognition sytem on a personal computer. Also, the video demostrates the robustness of the recognition to small rotations and shiftings as well as stability. In addition, the time to single image classification is good and take about 32.35 miliseconds (average from 10 iterations).

![image](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/poses_reference.png)

![video](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/handgesture_detrack_PC.mp4)
<p style="text-align:center;"><i>Video 1: Hand pose recognition in real-time running on a personal computer</i></p>

The Video 2 shows the implementation of the recognition system on a Raspberry Pi 3 board. As expected, the processing time (about 354.21 miliseconds, average from 10 iterations) is higher than the implementation on the personal computer (about 32.35 miliseconds) since this embedded computer has less computational resources compared with the personal computer.

![image](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/poses_reference.png)

![video](/posts/projects/real-time-hand-gesture-recognition-on-a-pc-and-raspberry-pi-using-deep-learning/handgesture_detrack_RPI.mp4)
<p style="text-align:center;"><i>Video 2: Hand pose recognition in real-time running on a Raspberry Pi</i></p>

### Conclusions ###

To sum up, a hand pose detector was implemented in real-time on a Raspberry Pi platform. The testing phase show an accuracy of 86.5% for the classification of 5 hand poses. In addition to this, the time used to perform the image classification for each image is about 32.35 ms on a personal computer and 354.21 ms on a Raspberry Pi board. The accuracy can be improved by adding more training images, adding filters or image transormations in pre-processing step as well as adding mode convolutional layers and tunning the model. Also, additional techniques for skin detection can be added in order to have a better hand gesture classifier.


