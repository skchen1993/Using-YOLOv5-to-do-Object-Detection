#follow PEP8 guidelines

import os
import cv2
import json

# Use the results from your model to generate the output json file
data_listdir = os.listdir("/home/skchen/ML_practice/DL_CV/HW2/datasets/images/test/")
data_listdir.sort(key=lambda x: int(x[:-4]))
filepath = '/home/skchen/ML_practice/DL_CV/HW2/yolov5/runs/detect/exp7_yolo_road_det/labels/'

data = []
fail_detect_image = []

for i in data_listdir:
    i = i.replace('.png', '')
    if not os.path.isfile(filepath+str(i)+'.txt'):
        fail_detect_image.append(i)
        a = {"bbox": [(1, 1, 1, 1)], "score": [0.5], "label": [0]}
        a = {"image_id": int(i), "bbox": [1, 1, 1, 1], 'score': 0.5, 'category_id': 0}
        data.append(a)
    else:
        f = open(filepath+str(i)+'.txt', 'r')
        print("open txt: ", filepath+str(i)+'.txt')

        contents = f.readlines()

        img_name = str(i)+'.png'
        im = cv2.imread('/home/skchen/ML_practice/DL_CV/HW2/datasets/images/test/'+img_name)
        h, w, c = im.shape
        for content in contents:
            a = {"image_id": int(i), "bbox": []}
            content = content.replace('\n', '')
            c = content.split(' ')
            print(c)

            w_center = w*float(c[1])
            h_center = h*float(c[2])
            width = w*float(c[3])
            height = h*float(c[4])
            left = float(w_center - width/2)
            right = float(w_center + width/2)
            top = float(h_center - height/2)
            bottom = float(h_center + height/2)

            a['bbox'].append(left)
            a['bbox'].append(top)
            a['bbox'].append(width)
            a['bbox'].append(height)

            a['score'] = float(c[5])
            a['category_id'] = int(c[0])

            data.append(a)


f.close()
print(fail_detect_image)
ret = json.dumps(data)

with open('answer.json', 'w') as fp:
    fp.write(ret)