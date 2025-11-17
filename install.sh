#!/bin/bash

echo "╔══╣ Install: hand_gesture_recognition (STARTING) ╠══╗"


# Install dependencies
DIR = $(pwd)
cd ..
git clone -b $ROS_DISTRO-devel https://github.com/TeamSOBITS/sobits_interfaces.git

cd $DIR

sudo apt-get update
sudo apt-get install -y \
    ros-${ROS_DISTRO}-sensor-msgs \
    ros-${ROS_DISTRO}-cv-bridge \
    ros-${ROS_DISTRO}-geometry-msgs \


python3 -m pip install --upgrade pip
python3 -m pip install mediapipe
python3 -m pip install "numpy<2"
python3 -m pip install tensorflow

echo "╚══╣ Install: hand_gesture_recognition (FINISHED) ╠══╝"