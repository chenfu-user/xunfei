import os
import random
import shutil

# 改成自己的路径
root_path = ''
txtfilepath = root_path + 'label/'
imgfilepath = root_path + 'img/'
txtsavepath = root_path + 'label/'
yolo_root_path = root_path 
yolo_images_train_path = yolo_root_path + 'image/train/'
yolo_images_val_path = yolo_root_path + 'image/val/'
yolo_images_test_path = yolo_root_path + 'image/test/'

yolo_labels_train_path = yolo_root_path + 'anna/train/'
yolo_labels_val_path = yolo_root_path + 'anna/val/'
yolo_labels_test_path = yolo_root_path + 'anna/test/'

if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)


if not os.path.exists(yolo_images_train_path):
    os.makedirs(yolo_images_train_path)

if not os.path.exists(yolo_images_val_path):
    os.makedirs(yolo_images_val_path)

if not os.path.exists(yolo_images_test_path):
    os.makedirs(yolo_images_test_path)

if not os.path.exists(yolo_labels_train_path):
    os.makedirs(yolo_labels_train_path)

if not os.path.exists(yolo_labels_val_path):
    os.makedirs(yolo_labels_val_path)

if not os.path.exists(yolo_labels_test_path):
    os.makedirs(yolo_labels_test_path)

def copyfile(imgname,name,imgpath,labelpath):
    image_copy_to = os.path.join(imgpath,imgname[:-1])
    if os.path.exists(image_copy_to) is False:
        shutil.copyfile(imgfilepath +imgname[:-1] , image_copy_to)
    label_copy_to = os.path.join(labelpath,name[:-1])
    if os.path.exists(label_copy_to) is False:
        shutil.copyfile(txtfilepath + name[:-1] , label_copy_to)

def main():
    train_test_percent = 1  # (训练集+验证集)/(训练集+验证集+测试集)
    train_valid_percent = 1  # 训练集/(训练集+验证集)

    total_xml = os.listdir(txtfilepath)
    num = len(total_xml)
    list = range(num)
    tv = int(num * train_test_percent)   # 训练集+验证集数量
    ts = int(num-tv)   # 测试集数量
    tr = int(tv * train_valid_percent)  # 验证集数量
    tz = int(tv-tr)   # 训练集数量
    trainval = random.sample(list, tv)
    train = random.sample(trainval, tr)

    print("train and valid size:", tv)
    print("train size:", tz)
    print("test size:", ts)
    print("valid size:", tr)
    ftest = open(txtsavepath + '/test.txt', 'w')
    ftrain = open(txtsavepath + '/train.txt', 'w')
    fvalid = open(txtsavepath + '/valid.txt', 'w')

    ftestimg = open(txtsavepath + '/img_test.txt', 'w')
    ftrainimg = open(txtsavepath + '/img_train.txt', 'w')
    fvalidimg = open(txtsavepath + '/img_valid.txt', 'w')

    for i in list:
        name = total_xml[i][:-4] + '.txt' + '\n'
        imgname = total_xml[i][:-4] + '.jpg' + '\n'
        if i in trainval:
            if i in train:
                ftrain.write(name)
                ftrainimg.write(imgname)
                copyfile(imgname,name,yolo_images_train_path,yolo_labels_train_path)
            else:
                fvalid.write(name)
                fvalidimg.write(imgname)
                copyfile(imgname,name,yolo_images_val_path,yolo_labels_val_path)
        else:
            ftest.write(name)
            ftestimg.write(imgname)
            copyfile(imgname,name,yolo_images_test_path,yolo_labels_test_path)

    ftrain.close()
    fvalid.close()
    ftest.close()

    ftrainimg.close()
    fvalidimg.close()
    ftestimg.close()

    print("finished!")

if __name__ == "__main__":
    main()

