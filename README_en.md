<a name="readme-top"></a>

[JA](README.md) | [EN](README_en.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

# Hand Gesture Recognition

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
    　<a href="#launch-and-usage">Launch and Usage</a>
      <ul>
        <li><a href="#subscribers--publishers">Subscribers and Publishers</a></li>
        <li><a href="#services">Services</a></li>
      </ul>
    </li>
    <li>
    <li><a href="#milestone">Milestone</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- INTRODUCTION -->
## Introduction

This repository allows the 2D pose estimation of two hands of a person.

> [!WARNING]
> Hand traking or person identification is not available.
The maximum number of hands are 2 (two) currently.

<details>
<summary>Detectable hand parts</summary>

| ID | Varible | Hand Part
| --- | --- | --- |
| 0  | wrist             | wrist |
| 1  | thumb_cmc         | thumb carpometacarpal |
| 2  | thumb_mcp         | thumb metacarpophalangeal |
| 3  | thumb_ip          | thumb interphalangeal |
| 4  | thumb_tip         | thumb tip |
| 5  | index_finger_mcp  | index finger metacarpophalangeal |
| 6  | index_finger_pip  | index finger proximal inter-phalangeal |
| 7  | index_finger_dip  | index finger distal interphalangeal |
| 8  | index_finger_tip  | index finger tip |
| 9  | middle_finger_mcp | middle finger metacarpophalangeal |
| 10 | middle_finger_pip | middle finger proximal inter-phalangeal |
| 11 | middle_finger_dip | middle finger distal interphalangeal |
| 12 | middle_finger_tip | middle finger tip |
| 13 | ring_finger_mcp   | ring finger metacarpophalangeal |
| 14 | ring_finger_pip   | ring finger proximal inter-phalangeal |
| 15 | ring_finger_dip   | ring finger distal interphalangeal |
| 16 | ring_finger_tip   | ring finger tip |
| 17 | pinky_mcp         | pinky metacarpophalangeal |
| 18 | pinky_pip         | pinky proximal inter-phalangeal |
| 19 | pinky_dip         | pinky distal interphalangeal |
| 20 | pinky_tip         | pinky tip |

![MediaPipe Hand landmark](https://developers.google.com/static/mediapipe/images/solutions/hand-landmarks.png)

</details>


<!-- GETTING STARTED -->
## Getting Started

This section describes how to set up this repository.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Prerequisites

First, please set up the following environment before proceeding to the next installation stage.

| System  | Version |
| ------------- | ------------- |
| Ubuntu | 22.04 (Jammy Jellyfish) |
| ROS | Humble Hawksbill |
| OpenCV | 4.9.0 (Tested) |
| Python | >=3.10 |

> [!NOTE]
> If you need to install `Ubuntu` or `ROS`, please check our [SOBITS Manual](https://github.com/TeamSOBITS/sobits_manual#%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6).


<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


### Installation

1. Go to the `src` folder of ROS.
   ```sh
   cd ~/colcon_ws/src/
   ```
2. Clone this repository.
   ```sh
   git clone -b humble-devel https://github.com/TeamSOBITS/hand_gesture_recognition
   ```
3. Navigate into the repository.
   ```sh
   cd hand_gesture_recognition/
   ```
4. Install the dependent packages.
   ```sh
   bash install.sh
   ```
5. Compile the package.
   ```sh
   cd ~/colcon_ws/
   ```
   ```sh
   colcon build --symlink-install
   ```
   ```sh
   source ~/colcon_ws/install/setup.sh
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LAUNCH AND USAGE EXAMPLES -->
## Launch and Usage

1. Start the camera and change image_topic_name in [hand_gesture_recognition.launch.py](launch/hand_gesture_recognition.launch.py) to the topic name of the camera you are using.
   ```sh
   default_value="/camera/color/image_raw"          # orbbec_series
   ```

2. Execute the launch file [hand_gesture_recognition.launch](launch/hand_gesture_recognition.launch.py).
   ```sh
   ros2 launch hand_gesture_recognition hand_gesture_recognition.launch
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Subscribers & Publishers

- Subscribers:

| Topic | Type | Meaning |
| --- | --- | --- |
| /camera/rgb/image_raw | sensor_msgs/Image | Camera Image |

- Publishers:

| Topic | Type | Meaning |
| --- | --- | --- |
| /hand_gesture/pose_array | sobits_interfaces/KeyPointArray | 2D Pose result information |
| /hand_gesture/hand_pose_img  | sensor_msgs/Image                        | 2D Pose result image |
| /hand_gesture/gesture_name    | sobits_interfaces/StringArray                                   | Hand Gesture result  |


### Services

| Service | Type | Meaning |
| --- | --- | --- |
| /hand_gesture/run_ctr | std_msgs/SetBool  | 2D Pose Detection toogle (ON:`true`, OFF:`false`) |


<!-- MILESTONE -->
## Milestone

- [ ] Allow more than 2 (two) hand detection
- [ ] Implement hand identification
- [x] OSS
    - [x] Improved documentation
    - [x] Unified coding style

See the [open issues][issues-url] for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->


<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- [ros_hand_gesture_recognition](https://github.com/TrinhNC/ros_hand_gesture_recognition)
- [Hand Gesture Recognition in ROS](https://robodev.blog/hand-gesture-recognition-in-ros)
- [ROS Noetic](http://wiki.ros.org/noetic)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/TeamSOBITS/hand_gesture_recognition.svg?style=for-the-badge
[contributors-url]: https://github.com/TeamSOBITS/hand_gesture_recognition/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/TeamSOBITS/hand_gesture_recognition.svg?style=for-the-badge
[forks-url]: https://github.com/TeamSOBITS/hand_gesture_recognition/network/members
[stars-shield]: https://img.shields.io/github/stars/TeamSOBITS/hand_gesture_recognition.svg?style=for-the-badge
[stars-url]: https://github.com/TeamSOBITS/hand_gesture_recognition/stargazers
[issues-shield]: https://img.shields.io/github/issues/TeamSOBITS/hand_gesture_recognition.svg?style=for-the-badge
[issues-url]: https://github.com/TeamSOBITS/hand_gesture_recognition/issues
[license-shield]: https://img.shields.io/github/license/TeamSOBITS/hand_gesture_recognition.svg?style=for-the-badge
[license-url]: LICENSE