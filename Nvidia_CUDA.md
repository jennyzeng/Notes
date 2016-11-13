# How to solve the incompatible issue of new NVIDIA GPU and CUDA 8.0 on Ubuntu
I got a GTX 1070 GPU just right after it was released and got problems in installing CUDA 8.0 toolkit. The driver version in CUDA toolkit was too old that it did not support the new GPU. Hence, I was not able to login to my system on the interface, it only display the login again and again. Below is what I did to solve this problem.


1. remove all installed NIVIDA drivers ```sudo apt-get purge nvidia-*```
2. Download the latest version of NVIDIA-Linux-x86_64-[version].run runfile in http://www.nvidia.com/Download/index.aspx?lang=en-us
2. download CUDA 8.0 installer in runfile type in https://developer.nvidia.com/cuda-downloads
3. log out
4. use ```Ctrl+ Alt + F1``` and login using your credentials
5. kill current X server session by typing ```sudo service lightdm stop``` or ```sudo stop lightdm```
6. go to your directory of your installers e.g. ```cd Downloads```
7. ```chmod +x ./NVIDIA-Linux-x86_64-[version].run```
8. install Nvidia driver first ```sudo ./NVIDIA-Linux-x86_64-[version].run```
9. if it failed and shows x server is running, type ```sudo killall Xorg``` and do the step 8 again. 
10. Accept and continue installation. 
11. Now you can install CUDA 8.0 toolkit.
12.  ```chmod +x ./cuda_[version]_linux.run``` and ```sudo ./cuda_[version]_linux.run```
13.  accept the terms 
14.  Choose **no** for the question "Install NVIDIA Accelerated Graphic Driver for Linux-x86_64 367.48"
15.  you can now reboot. 
15. follow instructions in http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#post-installation-actions to add paths.

Last update: Sat Nov 12 20:52:21 PST 2016
