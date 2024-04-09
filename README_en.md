<a name="readme-top"></a>

[JA](README.md) | [EN](README.en.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

# SOBIT PRO

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
    </li>
    <li><a href="#milestone">Milestone</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- INTRODUCTION -->
## Introduction

TBD

<p align="right">(<a href="#readme-top">back to top</a>)</p>


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
| Python | 3.9* |

> [!NOTE]
> If you need to install `Ubuntu` or `ROS`, please check our [SOBITS Manual](https://github.com/TeamSOBITS/sobits_manual#%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6).

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

TBD

1. Set the parameters inside [minimal.launch](launch/minimal.launch) and select the functions to launch with hand_gesture_recognition.
   ```xml
    <!-- Activate Mobile-Base (true), Arm (true), Head (true) -->
    <arg name="enable_mb"           default="true"/>
    <arg name="enable_arm"          default="true"/>
    <arg name="enable_head"         default="true"/>
    ...
    <arg name="open_rviz"           default="true"/>
    ...
   ```
> [!NOTE]
> Rewrite it as `true` or `false` depending on the functions you want to use.

2. Execute the launch file [minimal.launch](launch/minimal.launch).
   ```sh
   $ roslaunch hand_gesture_recognition minimal.launch
   ```
3. [Optional] Let's run the demo program.
   ```sh
   $ rosrun hand_gesture_recognition test_controll_wheel.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MILESTONE -->
## Milestone

- [x] Switching between SOBIT PRO and only the movement mechanism by parameter
- [x] Modification of example files
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

<!-- * []() -->
* [ROS Noetic](http://wiki.ros.org/noetic)

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