import time,os
import numpy as np
import math
import cv2
import rospy
import actionlib
import playsound
from rosgraph_msgs.msg import Clock
from actionlib_msgs.msg import GoalStatus
from sensor_msgs.msg import Image
from std_msgs.msg import Int8
from detect import main
from nav_msgs.msg import Odometry
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

#卧室：5，客厅：6，餐厅：7

def open_terminal(commands):
    cmd_list = []
    for cmd in commands:
        cmd_list.append(""" gnome-terminal --tab -e "bash -c '%s;exec bash'" >/dev/null  2>&1 """ %cmd)

    os.system(';'.join(cmd_list))

#各地点坐标
B = {
    "position": 
    {
        "x": 3.10,
        "y": 4.5,
        "z": 0.0
    },
    "orientation": 
    {
        "x": 0.0,
        "y": 0.0,
        "z": 0,
        "w": 1
    }
    }
    
C = {
    "position": 
    {
        "x": 3.54,
        "y": 2.79,
        "z": 0.0
    },
    "orientation": 
    {
        "x": 0.0,
        "y": 0.0,
        "z": 0,
        "w": 1
    }
    }
    
D = {
    "position": 
    {
        "x": 2.89,
        "y": 1.02,
        "z": 0.0
    },
    "orientation": 
    {
        "x": 0.0,
        "y": 0.0,
        "z": 0,
        "w": 1
    }
    }
    
target = {
    "position": 
    {
        "x": 0.964,
        "y": -0.11,
        "z": 0.0
    },
    "orientation": 
    {
        "x": 0.0,
        "y": 0.0,
        "z": -0.7,
        "w": 0.7
    }
    }

class Nav():
    def __init__(self):
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)#movebase的服务
        self.imgsub = rospy.Subscriber("/cam", Image, self.imgupdate)#图像
        self.yolosub = rospy.Subscriber('/yolo',Int8,self.yoloupdate)#识别的图片标签
        self.odomsub = rospy.Subscriber("/odom", Odometry, self.odomupdate)#里程计
        self.Bflag = 0
        self.Cflag = 0
        self.Dflag = 0
        self.odom = Odometry()
        self.img = None
        self.yolo = None
        
        self.client.wait_for_server()
        
    def odomupdate(self,data):
        self.odom = data
        
        
    def imgupdate(self,img_data):
        self.img = np.frombuffer(img_data.data, dtype=np.uint8).reshape(img_data.height, img_data.width, -1)
        
    def yoloupdate(self,data):
        self.yolo = data.data
        
    def get_pose(self,data):
        text = data.copy()
        self.pos_x = text['position']['x']
        self.pos_y = text['position']['y']
        self.pos_z = text['position']['z']
        self.ori_x = text['orientation']['x']
        self.ori_y = text['orientation']['y']
        self.ori_z = text['orientation']['z']
        self.ori_w = text['orientation']['w']
        
    def goal_pose(self):
        self.goal = MoveBaseGoal()
        self.goal.target_pose.header.frame_id = 'map'
        self.goal.target_pose.pose.position.x = self.pos_x
        self.goal.target_pose.pose.position.y = self.pos_y
        self.goal.target_pose.pose.position.z = self.pos_z
        self.goal.target_pose.pose.orientation.x = self.ori_x
        self.goal.target_pose.pose.orientation.y = self.ori_y
        self.goal.target_pose.pose.orientation.z = self.ori_z
        self.goal.target_pose.pose.orientation.w = self.ori_w
        
    def send_goal(self):
        self.goal_pose()
        print('send goal...')
        self.client.send_goal(self.goal)
        
    def get_state(self):
        state = self.client.get_state()
        if state == GoalStatus.SUCCEEDED:
            rospy.loginfo("reach")
            return True
        else:
            return False
    

if __name__ =='__main__':
    rospy.init_node('predict')
    nav = Nav()
    once = 0
    while not rospy.is_shutdown():
        if nav.Bflag == 0 and once == 0:
            once = 1
            nav.get_pose(B)
            nav.send_goal()
        if nav.Bflag == 0 and nav.get_state() and once == 1:
            once += 1
            print('reach B')
            cv2.imwrite('B/0.jpg',nav.img)
            open_terminal(['python detect.py --source B/'])#打开另一个终端，识别图片
            while nav.yolo is  None:
                pass
            nav.Bflag = nav.yolo
        if nav.Bflag != 0 and nav.Cflag == 0 and once == 2:
            once += 1
            nav.get_pose(C)
            nav.send_goal()
        if nav.Cflag == 0 and nav.get_state() and once == 3:
            once += 1
            print('reach C')
            cv2.imwrite('C/0.jpg',nav.img)
            open_terminal(['python detect.py --source C/'])
            while nav.yolo == nav.Bflag:
                pass
            nav.Cflag = nav.yolo
        if nav.Cflag != 0 and nav.Dflag == 0 and once ==4:
            once += 1
            nav.get_pose(D)
            nav.send_goal()
        if nav.Dflag == 0 and nav.get_state() and once ==5:
            once += 1
            print('reach D')
            cv2.imwrite('D/0.jpg',nav.img)
            open_terminal(['python detect.py --source D/'])
            while nav.yolo == nav.Cflag:
                pass
            nav.Dflag = nav.yolo
            print('result:',nav.Bflag,nav.Cflag,nav.Dflag)
        if nav.Dflag != 0 and once == 6:
            once += 1
            nav.get_pose(target)
            nav.send_goal()
        if once == 7 and nav.get_state():
            once += 1
            if nav.Bflag ==5 and nav.Cflag == 6 and nav.Dflag == 7:
                playsound.playsound('mp3/567.mp3') 
            if nav.Bflag ==5 and nav.Cflag == 7 and nav.Dflag == 6:
                playsound.playsound('mp3/576.mp3')   
            if nav.Bflag ==6 and nav.Cflag == 5 and nav.Dflag == 7:
                playsound.playsound('mp3/657.mp3')   
            if nav.Bflag ==6 and nav.Cflag == 7 and nav.Dflag == 5:
                playsound.playsound('mp3/675.mp3')   
            if nav.Bflag ==7 and nav.Cflag == 6 and nav.Dflag == 5:
                playsound.playsound('mp3/765.mp3')   
            if nav.Bflag ==7 and nav.Cflag == 5 and nav.Dflag == 6:
                playsound.playsound('mp3/756.mp3')   

                
                
                
                
                

    
