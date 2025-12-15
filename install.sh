#!/bin/bash

echo "╔══╣ Install: hand_gesture_recognition (STARTING) ╠══╗"


# Install dependencies
cd ..
git clone -b $ROS_DISTRO-devel https://github.com/TeamSOBITS/sobits_interfaces.git
git clone -b ${ROS_DISTRO}-devel https://github.com/TeamSOBITS/image_to_position.git
cd imaget_to_position/
bash install.sh
cd ..

sudo apt-get update
sudo apt-get install -y \
    ros-${ROS_DISTRO}-sensor-msgs \
    ros-${ROS_DISTRO}-cv-bridge \
    ros-${ROS_DISTRO}-geometry-msgs \
    ros-${ROS_DISTRO}-vision-msgs \



python3 -m pip install --upgrade pip
python3 -m pip install mediapipe
python3 -m pip install "numpy<2"
python3 -m pip install tensorflow

echo "╚══╣ Install: hand_gesture_recognition (FINISHED) ╠══╝"