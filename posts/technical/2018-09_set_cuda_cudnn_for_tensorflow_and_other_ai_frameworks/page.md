
## Set CUDA and cuDNN for Tensorflow and other AI frameworks ##

### Notes: ###

- Recommended versions: tensorflow-gpu 1.10, CUDA 9, cuDNN 7.

- Review CUDA versions and Driver versions requirements:

![image](/posts/technical/2018-09_set_cuda_cudnn_for_tensorflow_and_other_ai_frameworks/img1_drivers_versions.png){400}!

- Review tensorflow versions and CUDA/cuDNN versions requirements:

![image](/posts/technical/2018-09_set_cuda_cudnn_for_tensorflow_and_other_ai_frameworks/img2_python_cuda_cudnn_versions.png){500}!

- All versions of cuDNN only support GPUs with capability >= 3.0, therefore tensorflow-gpu only support GPUs with capability >= 3.0 . Check GPUs and capabilities: [[https://developer.nvidia.com/cuda-gpus](https://developer.nvidia.com/cuda-gpus)!].


### Steps: ###

0. Check and install the correct Driver.

1. Install CUDA: [[https://developer.nvidia.com/cuda-toolkit-archive](https://developer.nvidia.com/cuda-toolkit-archive)!].

2. Install cuDNN: [[https://developer.nvidia.com/rdp/cudnn-archive](https://developer.nvidia.com/rdp/cudnn-archive)!].

3. Install Ancaconda 3.

4. Create an environment called 'tf-gpu' which uses python 3.5.

5. Install Tensorflow with Conda: ```(env)$ conda install -c anaconda tensorflow-gpu=1.XX``` .

6. Verify if tensorflow-gpu works properly and using GPU.


### Verify Driver, CUDA and cuDNN: ###

- Check cuda driver version: ```~$ nvidia-smi``` or ```~$ cat /proc/driver/nvidia/version``` .

- Check local cuda version: ```~$ nvcc --version``` or ```~$ cat /usr/local/cuda/version.txt``` .

- Check local cudnn version: ```~$ cat /usr/local/cuda/include/cudnn.h | grep CUDNN_MAJOR -A 2``` .


### Verify Tensorflow: ###

- Acticate environment:

```
$ conda activate tf-gpu
```

- Open python and test Tensorflow:

```
(tf-gpu) $ python
```

```
>>> import tensorflow as tf
>>> sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
```

- Then you should obtain:

```
Device mapping:
/job:localhost/replica:0/task:0/gpu:0 -> device: 0, name: GeForce GTX 1050 Ti, pci bus id: 0000:01:00.0
2019-04-27 13:30:50.350374: I tensorflow/core/common_runtime/direct_session.cc:300] Device mapping:
/job:localhost/replica:0/task:0/gpu:0 -> device: 0, name: GeForce GTX 1050 Ti, pci bus id: 0000:01:00.0
```

### References: ###

- [https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html](Link 1)!.

- [https://stackoverflow.com/questions/41409842/ubuntu-16-04-cuda-8-cuda-driver-version-is-insufficient-for-cuda-runtime-vers](Link 2)!.

- [https://stackoverflow.com/questions/38009682/how-to-tell-if-tensorflow-is-using-gpu-acceleration-from-inside-python-shell](Link 3)!.

