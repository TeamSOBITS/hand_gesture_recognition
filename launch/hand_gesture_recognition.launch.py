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

    gesture_label = os.path.join(
        get_package_share_directory("hand_gesture_recognition"),
        "model/keypoint_classifier",
        "keypoint_classifier_label.csv"
        )
    gesrure_model = os.path.join(
        get_package_share_directory("hand_gesture_recognition"),
        "model/keypoint_classifier",
        "keypoint_classifier.tflite"
        )
    
    gesture_classifier_label = LaunchConfiguration("gesture_classifier_label")
    gesture_classifier_label_cmd = DeclareLaunchArgument(
        "gesture_classifier_label", default_value=gesture_label, description="gesture_classifier_label"
    )
    gesture_classifier_model = LaunchConfiguration("gesture_classifier_model")
    gesture_classifier_model_cmd = DeclareLaunchArgument(
        "gesture_classifier_model", default_value=gesrure_model, description="gesture_classifier_model"
    )

    point_cloud_topic = LaunchConfiguration("point_cloud_topic")
    point_cloud_topic_cmd = DeclareLaunchArgument(
        "point_cloud_topic",
        description="Detection 3D Pose from 2D Pose (sensor_msgs/msg/PointCloud2). if you select the 'point_cloud' in 'positioning_detection_mode'.",
        # default_value="/camera/depth/color/points",            ## realsense
        # default_value="/points2",                            ## azure_kinect
        # default_value="/camera/depth_registered/points",     ## orbbec_series ##
        default_value="/camera/depth_registered/points",     ## xtion
    )

    depth_image_topic_name = LaunchConfiguration("depth_image_topic_name")
    depth_image_topic_name_cmd = DeclareLaunchArgument(
        "depth_image_topic_name",
        description="Detection 3D Pose from 2D Pose (sensor_msgs/msg/Image). if you select the 'depth_image' in 'positioning_detection_mode'.",
        # default_value="/camera/depth/image_rect_raw", ## realsense
        # default_value="/depth_to_rgb/image_raw", ## azure_kinect
        # default_value="", ## orbbec_series ##
        default_value="/camera/depth/image_raw",    ## xtion
    )

    info_topic_name = LaunchConfiguration("info_topic_name")
    info_topic_name_cmd = DeclareLaunchArgument(
        "info_topic_name",
        description="Setup the camera info topic name. (sensor_msgs/msg/CameraInfo)",
        # default_value="/camera/color/camera_info", ## realsense
        # default_value="/rgb/camera_info", ## azure_kinect
        # default_value="", ## orbbec_series ##
        default_value="/camera/rgb/camera_info", ## xtion
    )

    positioning_detection_mode = LaunchConfiguration("positioning_detection_mode")
    positioning_detection_mode_cmd = DeclareLaunchArgument(
        "positioning_detection_mode",
        description="Select the 3D Pose Detection mode. Choose of ['point_cloud', 'depth_image']",
        default_value="point_cloud",
    )

    base_frame_name = LaunchConfiguration("base_frame_name")
    base_frame_name_cmd = DeclareLaunchArgument(
        "base_frame_name", description="Base frame name for the node. (String)",
        default_value="base_footprint",
    )

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
                "gesture_classifier_model":gesture_classifier_model,
                "gesture_classifier_label":gesture_classifier_label,
            },
        ],
        output="screen"
    )
    use_3d = LaunchConfiguration("use_3d")
    use_3d_cmd = DeclareLaunchArgument(
        "use_3d", default_value="False", description="Whether to activate 3D detections"
    )

    hand_pose_3d_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("image_to_position"),
                "launch",
                "keypoint_to_3d.launch.py",
            )
        ),
        launch_arguments={
            "namespace": namespace,
            "base_frame_name": base_frame_name,
            "keypoints_topic_name": "/hand_gesture/pose_array",
            "cloud_topic_name": point_cloud_topic,
            "depth_image_topic_name": depth_image_topic_name,
            "info_topic_name": info_topic_name,
            "execute_default": execute_default,
            "enable_id": "False",
            "positioning_detection_mode": positioning_detection_mode
        }.items(),
        condition=IfCondition(use_3d),  # use_3dがTrueのときのみ実行
    )


    return LaunchDescription(
        [
            use_3d_cmd,
            input_image_topic_cmd,
            point_cloud_topic_cmd,
            depth_image_topic_name_cmd,
            info_topic_name_cmd,
            base_frame_name_cmd,
            positioning_detection_mode_cmd,
            gesture_classifier_label_cmd,
            gesture_classifier_model_cmd,
            input_image_topic_cmd,
            execute_default_cmd,
            image_show_cmd,
            namespace_cmd,
            hand_gesture_cmd,
            hand_pose_3d_cmd,

        ]
    )