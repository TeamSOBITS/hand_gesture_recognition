<a name="readme-top"></a>

[JA](README.md) | [EN](README.en.md)

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
    　<a href="#subscribers--publishers">Subscribers and Publishers</a>
    　<a href="#services">Services</a>
    </li>
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
| Ubuntu | 20.04 (Focal Fossa) |
| ROS | Noetic Ninjemys |
| OpenCV | 4.9.0 (Tested) |
| Python | 3.9* |

> [!NOTE]
> If you need to install `Ubuntu` or `ROS`, please check our [SOBITS Manual](https://github.com/TeamSOBITS/sobits_manual#%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6).

> [!WARNING]
> Python 3.9 is installed within `install.sh`.
Please, use at your own risk if you are installing it in a local environment.

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


### Installation

1. Go to the `src` folder of ROS.
   ```sh
   $ roscd
   # Or just use "cd ~/catkin_ws/" and change directory.
   $ cd src/
   ```
2. Clone this repository.
   ```sh
   $ git clone https://github.com/TeamSOBITS/hand_gesture_recognition
   ```
3. Navigate into the repository.
   ```sh
   $ cd hand_gesture_recognition/
   ```
4. Install the dependent packages.
   ```sh
   $ bash install.sh
   ```
5. Compile the package.
   ```sh
   $ roscd
   # Or just use "cd ~/catkin_ws/" and change directory.
   $ catkin_make
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LAUNCH AND USAGE EXAMPLES -->
## Launch and Usage

1. Set the parameters inside [hand_sign.launch](launch/hand_sign.launch) and select the functions to launch with hand_gesture_recognition.
   ```xml
   <!-- Allow 2D pose detection (true) -->
   <arg name="pose_2d_detect"            default="true"/>

   <!-- Show 2D pose detection result as a log (true) -->
   <arg name="pose_2d_log_show"          default="true"/>
   <!-- Show 2D pose detection result as an image (true) -->
   <arg name="pose_2d_img_show"          default="true"/>
   <!-- Publish 2D pose detection result as an image (true) -->
   <arg name="pose_2d_img_pub"           default="true"/>

   <!-- Subscribe to camera topic -->
   <arg name="sub_img_topic_name"        default="/camera/rgb/image_raw"/>
   ```
> [!NOTE]
> Rewrite it as `true` or `false` depending on the functions you want to use.

2. Execute the launch file [hand_sign.launch](launch/hand_sign.launch).
   ```sh
   $ roslaunch hand_gesture_recognition hand_sign.launch
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
| /hand_gesture_recognition/pose_array | hand_gesture_recognition/KeyPoint2DArray | 2D Pose result information |
| /hand_gesture_recognition/pose_img   | sensor_msgs/Image                        | 2D Pose result image |
| /hand_gesture_recognition/gesture    | string                                   | Hand Gesture result  |


### Services

| Service | Type | Meaning |
| --- | --- | --- |
| /hand_gesture_recognition/run_ctr | sobits_msgs/RunCtrl | 2D Pose Detection toogle (ON:`true`, OFF:`false`) |


<!-- MILESTONE -->
## Milestone

- [] Allow more than 2 (two) hand detection
- [] Implement hand identification
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