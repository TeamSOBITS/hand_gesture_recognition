from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'hand_gesture_recognition'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, "launch"), glob('launch/*')),
        (os.path.join('share',package_name,'model/keypoint_classifier'),glob('model/keypoint_classifier/*')),
        (os.path.join('share',package_name,'model/point_history_classifier'),glob('model/point_history_classifier/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sobits',
    maintainer_email='adachidaichi0828@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    # tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "hand_gesture = hand_gesture_recognition.hand_sign_recognition_ros:main",
        ],
    },
)
