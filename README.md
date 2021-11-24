NYCU VRDL hw2 : try to used YOLOv5 to do the Object detection

# YOLOv5 for object detection
-Street View House Numbers detection.   
-SVHN dataset contains 33,402 trianing images, 13,068 test images.  
-Aim to train an accurate and fast digit detector  

## Environment
- Python 3.7.3
- Pytorch 1.7.0
- CUDA 10.2  

## step for producing submission
1. Download requirement
2. Data preprocessing
3. Model config setting
4. Training
5. Detect(inference)
6. Convert to Coco result format

### Download requirement
-Download project, required package and dataset  
 `git clone https://github.com/skchen1993/VRDL_2_YOLOv5.git`   
 `cd yolov5`   
 `pip install -r requirements.txt` 
   
     
-For data preposses (.mat file)  
 `pip install h5py`  
 
   
Download the SVHN dataset and place them into `VRDL_2_YOLOv5/datasets/images/train/`

### Data preprocessing
1. use `/VRDL_2_YOLOv5/datasets/mat_to_yolo.py` to convert SHVN .mat file to yolov5 label format, and saved in `VRDL_2_YOLOv5/datasets/labels/train/`
2. split training and validation data (have to do it in image and label)
3. folder structure looks like:  
```
-datasets
   |--images----|--train
   |            |--val
   |            |--test
   |
   |--labels----|--train
   |            |--val

-yolov5 (parallel to datasets)
```
### Model config setting
- prepare `svhn.yaml` in `VRDL_2_YOLOv5/yolov5/data/` 
```
# train and val data as 1) directory: path/images/, 2) file: path/images.txt, or 3) list: [path1/images/, path2/images/]
train: /home/skchen/ML_practice/DL_CV/HW2/datasets/images/train/  # 31402 images, change it to your path
val: /home/skchen/ML_practice/DL_CV/HW2/datasets/images/val/  # 3000 images, change it to your path

# number of classes
nc: 10

# class names
names: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
```
### Training
use the following command to train the yolov5 model on your custom dataset:  
`CUDA_VISIBLE_DEVICES=0,1,2,3 python train.py --img 320 --batch 256 --epochs 50 --data svhn.yaml --weights yolov5m.pt`
- weights: choose the model structure you want
- data: config of your dataset

### Detect(inference)
use the following command to do the inference on the testing dataset:  
`python detect.py --source /home/skchen/ML_practice/DL_CV/HW2/datasets/images/test/ --weights /home/skchen/ML_practice/DL_CV/HW2/yolov5/runs/train/exp9/weights/best.pt --conf 0.20 --name exp9_yolo_road_det_ --save-txt --save-conf`  
- source: path of testing data
- weight: path of your trained model parameter
- conf: confidence score
- name path to save the result

### Convert to Coco result format
After the inference, the label of testing image would be saved in `/home/skchen/ML_practice/DL_CV/HW2/yolov5/runs/detect/{your exp}`.  
For submission, we have to convert the yolov5 label format to coco result format.  
use `To_submission.py` to do the convert, then the `answer.txt` would be saved.  
Note: remember to modified the parameter(some path) in the `To_submission.py`. ex: testing image and label path.


# Reference
[chia56028/Street-View-House-Numbers-Detection](https://github.com/chia56028/Street-View-House-Numbers-Detection#install-packages)  
[ultralytics/yolov5](https://github.com/ultralytics/yolov5)  
