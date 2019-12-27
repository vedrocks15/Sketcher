# Sketcher
**OpenCV on Rpi3B+** 
## Requirements
The following repository contains the code for running an OpenCv code for converting live stream video to a sketchy video.
The following items have been used :
- Rpi 3B+
- Raspi cam V2 ( can use any other version, even NoIR version works fine)

## OpenCV Setup
For getting the opencv library to setup on raspberry buster (latest while I comitted this project) follow the steps in [OpenCV setup](https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/). The setup can take almost take more than 8 hours and you must constantly look for errors of missing libraries and sometimes when the make command crashes try running it with lower number of threads on pi as it helps reduce the strain.**Do Remember** to reduce the conf swap_space back to the default or else the sd card could get corrupted due to heavy read and writes.
#
The code is a simple sketch and all the functions used in it our explained in the readme file attched in the master directory.

## Sample Output
Sample 1
![Sample 1 ](https://github.com/vedrocks15/Sketcher/blob/master/Output/IMG_20191227_162325__01.jpg)
Sample 2
![Sample 2 ](https://github.com/vedrocks15/Sketcher/blob/master/Output/IMG_20191227_162407__01.jpg)
