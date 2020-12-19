
## Useful commands ##

### Shortcuts using Terminator ###

- ```Ctrl+Shift+O```: vertical split.

- ```Ctrl+Shift+E```: horizontal split.

- ```Ctrl+Shift+I```: new terminal in new window.

- ```Ctrl+Shift+T```: new terminal in same window.

### Remove (base) from terminal prompt after updating conda ###

This can also be because ```auto_activate_base``` is set to True. You can check this using the following command:

```
conda config --show | grep auto_activate_base
```

To set it false:

```
conda config --set auto_activate_base False
```

### Restart Network Manager service ###

Insert the next commad on terminal:

```
sudo systemctl restart NetworkManager.service
```

### Simple commands to manage environemnts in Anaconda ###

Create environment with a specific version of Python:

```
conda create -n myenv python=3.6
```

To create an environment with a specific version of Python and multiple packages:

```
conda create -n myenv python=3.6 scipy=0.15.0 astroid babel
```

Delete environment:

```
conda remove --name myenv --all
```

To export packages from one environment to .yml file and then create another environment with such packages contained in the .yml file:

```
conda env export -n myenv -f myenv.yml
conda env create -f myenv.yml
```

To use pip in your environment, in your terminal window or an Anaconda Prompt, run:

```
conda install -n myenv pip
conda activate myenv
pip <<x>pip_subcommand<x>>
```

### Example syntax for Secure Copy (scp) ###

Copy the file "foobar.txt" from a remote host to the local host:

```
$ scp your_username@remotehost.edu:foobar.txt /some/local/directory
```

Copy the file "foobar.txt" from the local host to a remote host:

```
$ scp foobar.txt your_username@remotehost.edu:/some/remote/directory
```

Copy the directory "foo" from the local host to a remote host's directory "bar":

```
$ scp -r foo your_username@remotehost.edu:/some/remote/directory/bar
```

Copy the directory "bar" from the remote host to a local host's directory "foo":

```
$ scp -r your_username@remotehost.edu:/some/remote/directory/bar /some/local/directory/foo 
```

Copying the files "foo.txt" and "bar.txt" from the local host to your home directory on the remote host:

```
$ scp foo.txt bar.txt your_username@remotehost.edu:~
```

### Compress video with Avidemux ###

- Set video stream to MPEG-4 AVC. stream to “AAC (Faac)”.

- Click the "Configure" button in the Video section.

- Click the "Encoding Mode" drop-down box and select "Two Pass - Video Size" in the list.

- Type the size you want the compressed video to be in megabytes into the "Target Video Size (MB)" box.

