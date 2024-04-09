#!/bin/bash

echo "╔══╣ Install: hand_gesture_recognition (STARTING) ╠══╗"


# Install dependencies
DIR = $(pwd)
cd ..
git clone https://github.com/TeamSOBITS/sobits_msgs

cd $DIR

sudo apt-get update
sudo apt-get install -y \
    python3.9 \
    python3.9-dev

python3.9 -m pip install --upgrade pip
python3.9 -m pip install mediapipe
python3.9 -m pip install tensorflow

echo "╚══╣ Install: hand_gesture_recognition (FINISHED) ╠══╝"