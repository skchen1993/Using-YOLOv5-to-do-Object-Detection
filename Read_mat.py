import numpy as np
import h5py

#利用這個把對應第index name object的內容組合出來 (ASCII -> string)
def get_img_name(f, idx=0):
    img_name = ''.join(map(chr, f[names[idx][0]][()].flatten()))
    return(img_name)


bbox_prop = ['height', 'left', 'top', 'width', 'label']
#利用這個把對應第index bbox object的內容可存到dict裡面
def get_img_boxes(f, idx=0):
    """
    get the 'height', 'left', 'top', 'width', 'label' of bounding boxes of an image
    :param f: h5py.File
    :param idx: index of the image
    :return: dictionary
    """
    meta = { key : [] for key in bbox_prop}

    box = f[bboxs[idx][0]]
    for key in box.keys():
        if box[key].shape[0] == 1:
            meta[key].append(int(box[key][0][0]))
        else:
            for i in range(box[key].shape[0]):
                meta[key].append(int(f[box[key][i][0]][()].item()))

    return meta


print("start")
f = h5py.File('./train/digitStruct.mat','r')
print("successfully load!!")

print(f.keys())
#<KeysViewHDF5 ['#refs#', 'digitStruct']>


print(f['digitStruct'].keys())
#<KeysViewHDF5 ['bbox', 'name']>

names = f['digitStruct/name']
bboxs = f['digitStruct/bbox']

print(names)
#<HDF5 dataset "name": shape (33402, 1), type "|O">
print(bboxs)
#<HDF5 dataset "bbox": shape (33402, 1), type "|O">

"""
It is worth to remember that each entry 
in both names or bboxs is an array of object references to the data file
"""
print(names[0])
# [<HDF5 object reference>]  => 裝著reference 的list
print(names[0][0])
#<HDF5 object reference> => reference 本人，指向實際裝資料obj

print(f[names[0][0]][()])
#[[ 49][ 46][112][110][103]]
# 下面會把這些數字去用ASCII 表做轉換 => 1.png 剛好對應到上面這些數字



print(get_img_boxes(f, idx=0))
#


names_list = []
bboxs_list = []

for i in range(33402):
	names_list.append(get_img_name(f, idx=i))
	bboxs_list.append(get_img_boxes(f, idx=i))
	print("i = ", i)

import pickle

with open("names_list", "wb") as fp:   #Pickling
	pickle.dump(names_list, fp)

with open("names_list", "wb") as fp:   #Pickling
	pickle.dump(bboxs_list , fp)