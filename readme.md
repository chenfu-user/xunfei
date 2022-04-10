```shell
src
    ├── CMakeLists.txt 
    ├── gazebo_pkg
    │   ├── CMakeLists.txt
    │   ├── launch
    │   │   ├── race.launch
    │   ├── meshes
    │   ├── package.xml
    │   ├── scripts
    │   │   └── temp.py
    │   ├── urdf
    │   │   └── waking_robot.xacro
    │   └── world#存放各类模型
    │       ├── arch3d-model.dae
    │       ├── dog.dae
    │       ├── food.dae
    │       ├── person.dae
    │       ├── race_with_cone.world
    │       ├── sofa.dae
    │       ├── tableware.dae
    │       ├── television.dae
    │       ├── wall.world
    │       └── world.world
    ├── navigation
    │   ├── CMakeLists.txt
    │   ├── launch#导航文件
    │   │   ├── amcl.launch
    │   │   ├── amcl_official.launch
    │   │   ├── ifly_navigation.launch
    │   │   └── move_base.launch
    │   ├── maps#地图
    │   │   ├── map.pgm
    │   │   └── map.yaml
    │   ├── move_base#导航参数
    │   │   ├── costmap_common_params.yaml
    │   │   ├── costmap_converter_params.yaml
    │   │   ├── global_costmap_params.yaml
    │   │   ├── global_planner_params.yaml
    │   │   ├── local_costmap_params.yaml
    │   │   └── teb_local_planner_params.yaml
    │   ├── package.xml    │   │   ├── bot.dae
    │   │   └── hokuyo.dae
    │   ├── rviz
    │   │   ├── ifly_navigation_dwa_rviz.rviz
    │   │   ├── ifly_navigation_eband_rviz.rviz
    │   │   └── ifly_navitation_teb_rviz.rviz
    │   └── scripts
    │       ├── img#存放拍的图片
    │       ├── imgsave.py#简单的拍照程序
    │       ├── label
    │       │   └── classes.txt
    │       └── test.py
    ├── xf_gmapping
    │   ├── CMakeLists.txt
    │   ├── config#建图参数
    │   │   ├── frontier_exploration.yaml
    │   │   ├── gmapping_params.yaml
    │   │   ├── ifly_lds_2d_gazebo.lua
    │   │   ├── ifly_lds_2d.lua
    │   │   └── karto_mapper_params.yaml
    │   ├── launch
    │   │   └── xf_gmapping.launch
    │   ├── package.xml
    │   └── rviz
    │       └── ifly_gmapping.rviz
    └── yolo#yolov5，制作成了一个功能包
        ├── B
        │   └── 0.jpg#到达B区拍的图片
        ├── best.pt
        ├── C
        │   └── 0.jpg
        ├── CMakeLists.txt
        ├── CONTRIBUTING.md
        ├── D
        │   └── 0.jpg
        ├── datasets
        │   └── xunfeidata#自制的数据集
        │       ├── images
        │       │   ├── labels
        │       │   │   ├── train
        │       │   │   └── train.cache
        │       │   ├── train
        │       │   ├── train.cache
        │       │   └── val
        │       ├── img_test.txt
        │       ├── img_train.txt
        │       ├── labels
        │       │   ├── train
        │       │   ├── train.cache
        │       │   ├── val
        │       │   └── val.cache
        ├── detect.py#识别
        ├── Dockerfile
        ├── export.py
        ├── hubconf.py
        ├── LICENSE
        ├── models
        │   ├── common.py
        │   ├── experimental.py
        │   ├── hub
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── common.cpython-38.pyc
        │   │   ├── experimental.cpython-38.pyc
        │   │   ├── __init__.cpython-38.pyc
        │   │   └── yolo.cpython-38.pyc
        │   ├── tf.py
        ├── mp3
        ├── msg
        ├── package.xml
        ├── pre.py#导航启动及识别读取
        ├── __pycache__
        │   ├── detect.cpython-38.pyc
        │   ├── export.cpython-38.pyc
        │   └── val.cpython-38.pyc
        ├── README.md
        ├── requirements.txt
        ├── runs
        │   ├── detect
        │   └── train
        ├── setup.cfg
        ├── train.py
        ├── tutorial.ipynb
        ├── utils
        │   ├── activations.py
        │   ├── augmentations.py
        │   ├── autoanchor.py
        │   ├── autobatch.py
        │   ├── aws
        │   │   ├── __init__.py
        │   │   ├── mime.sh
        │   │   ├── resume.py
        │   │   └── userdata.sh
        │   ├── benchmarks.py
        │   ├── callbacks.py
        │   ├── datasets.py
        │   ├── downloads.py
        │   ├── flask_rest_api
        │   │   ├── example_request.py
        │   │   ├── README.md
        │   │   └── restapi.py
        │   ├── general.py
        │   ├── google_app_engine
        │   │   ├── additional_requirements.txt
        │   │   ├── app.yaml
        │   │   └── Dockerfile
        │   ├── __init__.py
        │   ├── loggers
        │   │   ├── __init__.py
        │   │   ├── __pycache__
        │   │   │   └── __init__.cpython-38.pyc
        │   │   └── wandb
        │   │       ├── __init__.py
        │   │       ├── log_dataset.py
        │   │       ├── __pycache__
        │   │       │   ├── __init__.cpython-38.pyc
        │   │       │   └── wandb_utils.cpython-38.pyc
        │   │       ├── README.md
        │   │       ├── sweep.py
        │   │       ├── sweep.yaml
        │   │       └── wandb_utils.py
        │   ├── loss.py
        │   ├── metrics.py
        │   ├── plots.py
        │   ├── __pycache__
        │   │   ├── activations.cpython-38.pyc
        │   │   ├── augmentations.cpython-38.pyc
        │   │   ├── autoanchor.cpython-38.pyc
        │   │   ├── autobatch.cpython-38.pyc
        │   │   ├── callbacks.cpython-38.pyc
        │   │   ├── datasets.cpython-38.pyc
        │   │   ├── downloads.cpython-38.pyc
        │   │   ├── general.cpython-38.pyc
        │   │   ├── __init__.cpython-38.pyc
        │   │   ├── loss.cpython-38.pyc
        │   │   ├── metrics.cpython-38.pyc
        │   │   ├── plots.cpython-38.pyc
        │   │   └── torch_utils.cpython-38.pyc
        │   └── torch_utils.py
        ├── val.py
        └── weights
            ├── best.pt#权重
            └── yolov5s.pt
```

#### 一、使用环境

```shell
#ubuntu18.04 python3.7 torch>=1.7 ros(melodic) cuda>=10.2
```

#### 二、准备工作

1、gedit打开gazebo_pkg/world/world.world将所有带有绝对路径全部改成自己的绝对路径

```
比如将/home/cf/ai_ws/src/gazebo_pkg/world/person.dae改为/home/xxx/ai_ws/src/gazebo_pkg/world/person.dae
```

2、将ai_ws放入主目录进行catkin_make编译

3、进入主目录.bashrc中将功能包的环境source进去

4、命令行进入yolo文件目录下

```shell
pip install -r requirements.txt
```

5、将table，end_plane和start_plane复制到.gazebo/models



#### 三、运行

1、一次运行

```shell
roslaunch gazebo_pkg race.launch
```

```shell
roslaunch navigation ifly_navigation.launch
```

```shell
cd ~/ai_ws/src/yolo 
python3 pre.py
```

2、建图

```shell
roslaunch gazebo_pkg race.launch
```

```shell
roslaunch xf_gmapping xf_gmapping.launch
```

```shell
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

3、yolo训练

进入yolo文件目录下

```shell
python train.py --img 640 --batch 16 --epochs 100 --data ./data/xunfei.yaml --cfg ./models/yolov5s.yaml --weights ./weights/yolov5s.pt
```

​    如果想训练自己的图片就将自己的图片和标签放进datasets/xunfeidata/images/train和datasets/xunfeidata/labels/train即可，标签可以使用github上的LabelImg来标，这里我的标签的顺序在data/xunfei.yaml中有写。

# chenfu-user
