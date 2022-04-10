import time
import numpy as np
import cv2
import rospy
from sensor_msgs.msg import Image


def callback(img_data):
    global img
    img = np.frombuffer(img_data.data, dtype=np.uint8).reshape(img_data.height, img_data.width, -1)
    print(img)
    cv2.imwrite('img/27.jpg',img)

    
    
sub = rospy.Subscriber("/cam", Image, callback)

if __name__ =='__main__':
    rospy.init_node('save')
    while not rospy.is_shutdown():
        rospy.spin()
    
