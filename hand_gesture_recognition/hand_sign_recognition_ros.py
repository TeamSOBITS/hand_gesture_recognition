import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from std_srvs.srv import SetBool
from sensor_msgs.msg import Image
from sobits_interfaces.msg import KeyPoint
from sobits_interfaces.msg import KeyPointArray
from vision_msgs.msg import Detection2DArray
from vision_msgs.msg import Detection2D
from rclpy.qos import QoSProfile, QoSHistoryPolicy, QoSDurabilityPolicy, QoSReliabilityPolicy

from .hand_gesture_recognition import GestureRecognition
from cv_bridge import CvBridge
import cv2
import os


class HandSignRecognition(Node):
    def __init__(self):
        super().__init__("hand_gesture_recognition")
        self.declare_parameter("input_image_topic", "image_raw")
        self.declare_parameter("image_show",True)
        self.declare_parameter("execute_default",True)
        self.declare_parameter("gesture_classifier_label","/home/sobits/colcon_ws/src/hand_gesture_recognition/hand_gesture_recognition/model/keypoint_classifier/keypoint_classifier_label.csv")
        self.declare_parameter("gesture_classifier_model","/home/sobits/colcon_ws/src/hand_gesture_recognition/hand_gesture_recognition/model/keypoint_classifier/keypoint_classifier.tflite")
        self.gesture_classifier_label = self.get_parameter("gesture_classifier_label").get_parameter_value().string_value
        self.gesture_classifier_model = self.get_parameter("gesture_classifier_model").get_parameter_value().string_value
        self.image_topic_name = self.get_parameter("input_image_topic").get_parameter_value().string_value
        self.img_show_flag = self.get_parameter("image_show").get_parameter_value().bool_value
        self.detect = self.get_parameter("execute_default").get_parameter_value().bool_value

        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # self.gesture_classifier_label = os.path.join(current_dir, "model/keypoint_classifier", "keypoint_classifier_label.csv.")
        # self.gesture_classifier_model = os.path.join(current_dir, "model/keypoint_classifier", "keypoint_classifier.tflite.")

        self.gesture_detector = GestureRecognition(self.gesture_classifier_label,
                                                   self.gesture_classifier_model)

        self.image_qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            durability=QoSDurabilityPolicy.VOLATILE,
            depth=1,
        )
        self.cv_bridge = CvBridge()
        self.delay = 1
        self.keypoint_list=["wrist", 
                       "thumb_cmc",
                       "thumb_mcp",
                       "thumb_ip",
                       "thumb_tip" 
                       "index_finger_mcp",
                       "index_finger_pip",
                       "index_finger_dip",
                       "index_finger_tip",
                       "middle_finger_mcp",
                       "middle_finger_pip",
                       "middle_finger_dip",
                       "middle_finger_tip",
                       "ring_finger_mcp",
                       "ring_finger_pip",
                       "ring_finger_dip",
                       "ring_finger_tip",
                       "pinky_mcp",
                       "pinky_pip",
                       "pinky_dip",
                       "pinky_tip"]
        self.run_ctr_server_ = self.create_service(SetBool,'run_ctr',self.run_ctr_server)
        self.pub_result_img = self.create_publisher(Image, 'hand_pose_img',self.image_qos_profile)
        self.pub_result_array = self.create_publisher(KeyPointArray,'pose_array',1)
        self.pub_gesture = self.create_publisher(Detection2DArray,"gesture_name",1)
        self.sub_img = self.create_subscription(Image,self.image_topic_name,self.image_cb,self.image_qos_profile)

    def run_ctr_server(self,request,response):
        self.detect = request.data
        response.success = True
        return response

    def image_cb(self,msg):
        if not self.detect:
            return

        encoding = msg.encoding
        cv_image = self.cv_bridge.imgmsg_to_cv2(msg)

        if encoding == 'bgra8':
            cv_image     = cv2.cvtColor(cv_image, cv2.COLOR_RGBA2RGB)
        elif encoding == 'rgba8':
            cv_image     = cv2.cvtColor(cv_image, cv2.COLOR_BGRA2RGB)
        elif encoding == 'rgb8':
            cv_image     = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        else:
            self.get_logger().error(f"Unsupported encoding: {encoding}")
            return
        
        debug_image,gestures,hand_lms,hand_poss,confs,brects = self.gesture_detector.recognize(cv_image)

        if hand_lms is not None:
            keypoint_array_msg = KeyPointArray()
            gesture_array_msg = Detection2DArray()
            gesture_array_msg.header = msg.header
            keypoint_array_msg.header = msg.header
            for hand_idx, (hand_lm, hand_pos, gesture, conf,brect) in enumerate(zip(hand_lms, hand_poss, gestures, confs,brects)):
                gesture_msg = Detection2D()
                gesture_msg.id = gesture
                gesture_msg.bbox.center.position.x = (brect[0] + brect[2])/2
                gesture_msg.bbox.center.position.y = (brect[1] + brect[3])/2
                gesture_msg.bbox.size_x = float(brect[2] - brect[0])
                gesture_msg.bbox.size_y = float(brect[3] - brect[1])
                gesture_array_msg.detections.append(gesture_msg)
                for idx, keypoint in enumerate(self.keypoint_list):
                    if idx >= len(hand_lm):
                        break
                    keypoint_msg = KeyPoint()
                    p = Point()
                    p.x = float(hand_lm[idx][0])
                    p.y = float(hand_lm[idx][1])
                    p.z = 0.0
                    keypoint_msg.key_names = [f"hand{hand_idx}_{hand_pos}_{keypoint}"]
                    keypoint_msg.key_points = [p]
                    keypoint_msg.score = conf
                    keypoint_array_msg.key_points_array.append(keypoint_msg)

            result_img_msg = self.cv_bridge.cv2_to_imgmsg(debug_image, "bgr8")
            result_img_msg.header = msg.header
            

            if self.img_show_flag:
                cv2.imshow('Lightweight Human Pose Estimation', debug_image)
                key = cv2.waitKey(self.delay)

            self.pub_result_img.publish(result_img_msg)
            self.pub_gesture.publish(gesture_array_msg)
            self.pub_result_array.publish(keypoint_array_msg)

def main():
    rclpy.init()
    node = HandSignRecognition()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()