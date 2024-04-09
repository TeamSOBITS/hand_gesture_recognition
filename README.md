<a name="readme-top"></a>

[JA](README.md) | [EN](README.en.md)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![License][license-shield]][license-url]

# Hand Gesture Recognition

<!-- 目次 -->
<details>
  <summary>目次</summary>
  <ol>
    <li>
      <a href="#概要">概要</a>
    </li>
    <li>
      <a href="#環境構築">環境構築</a>
      <ul>
        <li><a href="#環境条件">環境条件</a></li>
        <li><a href="#インストール方法">インストール方法</a></li>
      </ul>
    </li>
    <li>
    　<a href="#実行操作方法">実行・操作方法</a>
    </li>
    <li><a href="#マイルストーン">マイルストーン</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <li><a href="#参考文献">参考文献</a></li>
  </ol>
</details>



<!-- レポジトリの概要 -->
## 概要

TBD

<details>
<summary>検出可能な骨格一覧</summary>

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

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


<!-- セットアップ -->
## セットアップ

ここで，本レポジトリのセットアップ方法について説明します．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


### 環境条件

まず，以下の環境を整えてから，次のインストール段階に進んでください．

| System  | Version |
| ------------- | ------------- |
| Ubuntu | 20.04 (Focal Fossa) |
| ROS | Noetic Ninjemys |
| Python | 3.9* |

> [!NOTE]
> `Ubuntu`や`ROS`のインストール方法に関しては，[SOBITS Manual](https://github.com/TeamSOBITS/sobits_manual#%E9%96%8B%E7%99%BA%E7%92%B0%E5%A2%83%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)に参照してください．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


### インストール方法

1. ROSの`src`フォルダに移動します．
   ```sh
   $ roscd
   # もしくは，"cd ~/catkin_ws/"へ移動．
   $ cd src/
   ```
2. 本レポジトリをcloneします．
   ```sh
   $ git clone https://github.com/TeamSOBITS/hand_gesture_recognition
   ```
3. レポジトリの中へ移動します．
   ```sh
   $ cd hand_gesture_recognition/
   ```
4. 依存パッケージをインストールします．
   ```sh
   $ bash install.sh
   ```
5. パッケージをコンパイルします．
   ```sh
   $ roscd
   # もしくは，"cd ~/catkin_ws/"へ移動．
   $ catkin_make
   ```

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


<!-- 実行・操作方法 -->
## 実行・操作方法

TBD

1. hand_gesture_recognitionの起動する機能をパラメタとして[minimal.launch](launch/minimal.launch)に設定します．
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
> 使用したい機能に応じて，`true`か`false`かに書き換えてください．

2. [minimal.launch](launch/minimal.launch)というlaunchファイルを実行します．
   ```sh
   $ roslaunch hand_gesture_recognition minimal.launch
   ```
3. [任意] デモプログラムを実行してみましょう．
   ```sh
   $ rosrun hand_gesture_recognition test_controll_wheel.py
   ```

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


<!-- マイルストーン -->
## マイルストーン

- [x] パラメタによるSOBIT PROと移動機構のみの切り替え
- [x] exampleファイルの修正
- [x] OSS
    - [x] ドキュメンテーションの充実
    - [x] コーディングスタイルの統一

現時点のバッグや新規機能の依頼を確認するために[Issueページ][issues-url] をご覧ください．

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>


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

<p align="right">(<a href="#readme-top">上に戻る</a>)</p> -->


<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more NOTErmation.

<p align="right">(<a href="#readme-top">上に戻る</a>)</p> -->


<!-- 参考文献 -->
## 参考文献

TBD
- [ROS Noetic](http://wiki.ros.org/noetic)
<!-- - [](/) -->

<p align="right">(<a href="#readme-top">上に戻る</a>)</p>



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