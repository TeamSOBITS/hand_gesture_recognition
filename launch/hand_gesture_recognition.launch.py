import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription, LaunchContext
from launch.actions import DeclareLaunchArgument, OpaqueFunction, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch.conditions import IfCondition


def generate_launch_description():

    input_image_topic = LaunchConfiguration("input_image_topic")
    input_image_topic_cmd = DeclareLaunchArgument(
        "input_image_topic",
        description="ROS Topic Name of sensor_msgs/msg/Image message. (sensor_msgs/msg/Image)",
        # default_value="/camera/color/image_raw",            ## realsense
        # default_value="/rgb/image_raw",                   ## azure_kinect
        # default_value="/camera/color/image_raw",          ## orbbec_series ##
        default_value="/camera/rgb/image_raw",            ## xtion
    )

    execute_default = LaunchConfiguration("execute_default")
    execute_default_cmd = DeclareLaunchArgument(
        "execute_default", default_value="True", description="Whether to start Human Pose Estimation enabled"
    )


    image_show = LaunchConfiguration("image_show")
    image_show_cmd = DeclareLaunchArgument(
        "image_show",
        default_value="False",
        description="image show flag",
    )

    # keypoint_dictionary = os.path.join(
    #     get_package_share_directory("lightweight_human_pose_estimation"),
    #     "keypoints",
    #     "key_point_dictionary.yaml"
    #     )

    namespace = LaunchConfiguration("namespace")
    namespace_cmd = DeclareLaunchArgument(
        "namespace", default_value="hand_gesture", description="Namespace for the nodes"
    )

    hand_gesture_cmd = Node(
        package="hand_gesture_recognition",
        executable="hand_gesture",
        name="hand_gesture_recognition",
        namespace=namespace,
        parameters=[
            {
                "input_image_topic": input_image_topic,
                "execute_default": execute_default,
                "image_show": image_show,
            },
        ],
        output="screen"
    )

    return LaunchDescription(
        [
            input_image_topic_cmd,
            execute_default_cmd,
            image_show_cmd,
            namespace_cmd,
            hand_gesture_cmd,
        ]
    )