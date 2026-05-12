
## Install Nvidia CUDA 9.0 and cuDNN 7.0 on Ubuntu 16.04 for Deep Learning ##

### 1. Install CUDA: ###

Go to: [https://developer.nvidia.com/cuda-90-download-archive](https://developer.nvidia.com/cuda-90-download-archive)!.

Select: LINUX --> x86_64 --> Ubuntu --> 16.04 --> deb (network).

Then:

```
sudo dpkg -i cuda-repo-ubuntu1604_9.0.176-1_amd64.deb
sudo apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/7fa2af80.pub
sudo apt-get update
sudo apt-get install cuda=9.0.176-1
```

Set up the development environment by modifying the PATH and LD_LIBRARY_PATH variables by adding them to the end of .bashrc file (``` sudo gedit .bashrc ```):

```
export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
```

### 2. Install cuDNN: ###

Go to: [https://developer.nvidia.com/rdp/cudnn-archive](https://developer.nvidia.com/cuda-90-download-archive)!.

Select: "Download cuDNN v7.0.5 (Dec 5, 2017), for CUDA 9.0" --> "cuDNN v7.0.5 Library for Linux".

Download the .tgz file.

Navigate to your <cudnnpath> directory containing the cuDNN Tar file (your cuDNN download path, usually ~/Downloads/):

```
cd ~/Downloads/
```

Unzip the cuDNN package:

```
tar -xzvf cudnn-10.2-linux-x64-v7.6.5.32.tgz
```

Copy the following files into the CUDA Toolkit directory, and change the file permissions:

```
sudo cp cuda/include/cudnn.h /usr/local/cuda/include
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
```

### References: ###

- [https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions)!.

- [https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html)!.

