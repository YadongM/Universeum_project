# SSY340_project



### Project Introduction

This Chalmers SSY 340 deep machine learning project.

It's a project about classify animals in Universeum.



### Author

Jiapeng Sun 

Yadong Mao



### Data Description

We took 1,115 photos from the perspective of tourists at Universeum, with 19 classes.

About 19 classes, please check [classes](https://github.com/maodreamer/SSY340_project/blob/master/Classes_describe.md).

maodreamer/SSY340_project

We use [labelImg](https://github.com/tzutalin/labelImg) for data annotation, make two datasets through [roboflow](https://roboflow.com/).






Universeum_no_data_augmentation:
1115 pictures, modified picture size to 640×640, no data enhancement.



Universeum_with_data_augmentation:
On the basis of Universeum_no_data_augmentation, the training set part is doubled by the following data augmentation method.

* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down
* Random brigthness adjustment of between 0 and +30 percent
* Random Gaussian blur of between 0 and 1.5 pixels



The dataset is stored in [Yolo v5](https://github.com/ultralytics/yolov5) format. Images are stored in images folder, and label information is stored in labels folder.

```
─Universeum_with_data_augmentation
    ├─test
    │  ├─images
    │  └─labels
    ├─train
    │  ├─images
    │  └─labels
    └─valid
        ├─images
        └─labels
```



You can download the dataset from [here](https://chalmersuniversity.box.com/s/4olr9s4ga0ls73qokb17iukodlldvzt0).



### Yolo_v5 Environment



```shell
# python>=3.6
# torch>=1.3.0
# torchvision>=0.4.1

# Create a virtual environment
conda create -n py36 python=3.6
conda activate py36

# git clone yolo v5 repo
git clone https://github.com/ultralytics/yolov5

# Install dependencies
cd yolov5
pip3 install -U -r requirements.txt
```















































