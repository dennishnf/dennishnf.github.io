
## Accessing to Raspberry Pi camera with Python 2.7 and OpenCV 2 ##

Once installed Python 2.7 and Opencv 2, now we can finally start writing some code!.

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

### Accessing a single image of your Raspberry Pi using Python and OpenCV ###

Open up a new file, name it ```test_image.py```, and insert the following code:

```
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
     
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
     
# allow the camera to warmup
time.sleep(0.1)
     
# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
     
# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)
```

We’ll start by importing our necessary packages on Lines 2-5.

From there, we initialize our PiCamera object on Line 8 and grab a reference to the raw capture component on Line 9. This rawCapture  object is especially useful since it (1) gives us direct access to the camera stream and (2) avoids the expensive compression to JPEG format, which we would then have to take and decode to OpenCV format anyway. I highly recommend that you use PiRGBArray  whenever you need to access the Raspberry Pi camera — the performance gains are well worth it.

From there, we sleep for a tenth of a second on Line 12 — this allows the camera sensor to warm up.

Finally, we grab the actual photo from the rawCapture  object on Line 15 where we take special care to ensure our image is in BGR format rather than RGB. OpenCV represents images as NumPy arrays in BGR order rather than RGB — this little nuisance is subtle, but very important to remember as it can lead to some confusing bugs in your code down the line.

Finally, we display our image to screen on Lines 19 and 20.

To execute this example, open up a terminal, navigate to your test_image.py  file, and issue the following command:

```
$ python test_image.py
```

If all goes as expected you should have an image displayed on your screen.

### Accessing the video stream of your Raspberry Pi using Python and OpenCV ###

Alright, so we’ve learned how to grab a single image from the Raspberry Pi camera. But what about a video stream?.

You might guess that we are going to use the cv2.VideoCapture  function here — but I actually recommend against this. Getting cv2.VideoCapture  to play nice with your Raspberry Pi is not a nice experience (you’ll need to install extra drivers) and something you should generally avoid.

And besides, why would we use the cv2.VideoCapture  function when we can easily access the raw video stream using the picamera  module?.

Let’s go ahead and take a look on how we can access the video stream. Open up a new file, name it ```test_video.py```, and insert the following code:

```
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
     
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
     
# allow the camera to warmup
time.sleep(0.1)
     
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
  # grab the raw NumPy array representing the image, then initialize the timestamp
  # and occupied/unoccupied text
  image = frame.array
     
  # show the frame
  cv2.imshow("Frame", image)
  key = cv2.waitKey(1) & 0xFF
     
  # clear the stream in preparation for the next frame
  rawCapture.truncate(0)
     
  # if the `q` key was pressed, break from the loop
  if key == ord("q"):
    break
```

This example starts off similarly to the previous one. We start off by importing our necessary packages on Lines 2-5.

And from there we construct our camera  object on Line 8 which allows us to interface with the Raspberry Pi camera. However, we also take the time to set the resolution of our camera (640 x 480 pixels) on Line 9 and the frame rate (i.e. frames per second, or simply FPS) on Line 10. We also initialize our PiRGBArray  object on Line 11, but we also take care to specify the same resolution as on Line 9.

Accessing the actual video stream is handled on Line 17 by making a call to the capture_continuous  method of our camera  object.

This method returns a frame  from the video stream. The frame then has an array  property, which corresponds to the frame  in NumPy array format — all the hard work is done for us on Lines 17 and 20!.

We then take the frame of the video and display on screen on Lines 23 and 24.

An important line to pay attention to is Line 27: You must clear the current frame before you move on to the next one!.

If you fail to clear the frame, your Python script will throw an error — so be sure to pay close attention to this when implementing your own applications!.

Finally, if the user presses the q  key, we break form the loop and exit the program.

To execute our script, just open a terminal (making sure you are in the cv  virtual environment, of course) and issue the following command:

```
$ python test_video.py
```

If all goes as expected you should have a video stream displayed on your screen.

### Resources ###

- [https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/](https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/)!.

