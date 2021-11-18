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
   
Download the SVHN dataset and place them into `VRDL_2_YOLOv5/datasets/images/train/`

### Data preprocessing
1. use `/VRDL_2_YOLOv5/datasets/mat_to_yolo.py` to convert SHVN .mat file to yolov5 label format, and saved in `VRDL_2_YOLOv5/datasets/labels/train/`
2. 





# Reference
[chia56028/Street-View-House-Numbers-Detection](https://github.com/chia56028/Street-View-House-Numbers-Detection#install-packages)
[ultralytics/yolov5](https://github.com/ultralytics/yolov5)
