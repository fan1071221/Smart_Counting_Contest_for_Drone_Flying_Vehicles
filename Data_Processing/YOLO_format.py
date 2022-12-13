# -*- coding: utf-8 -*-

import os
from os import walk, getcwd
import numpy as np
import cv2


def convert(size, box):

    x = (box[0] + box[1])/2.0/size[0]
    y = (box[2] + box[3])/2.0/size[1]
    w = max(box[1] - box[0], box[0] - box[1])/size[0]
    h = max(box[2] - box[3], box[3] - box[2])/size[1]

    return (x, y, w, h)


"""-------------------------------------------------------------------"""

""" Configure Paths"""
mypath = "train/"
outpath = "result/"

wd = getcwd()

""" Get yolo txt file list """
txt_list = []
for file in os.listdir(mypath):
    if file.endswith(".txt"):
        txt_list.append(file)


""" Process """
for txt_name in txt_list:
    with open(outpath+txt_name, 'w') as fw:
        img_filename = txt_name.rstrip(".txt") + ".png"
        img_path = mypath + txt_name.rstrip(".txt") + ".png"
        img = cv2.imread(img_path)
        print(img_path)

        """ Open input text files """
        txt_path = mypath + txt_name
        print("Input:" + txt_path)
        txt_file = open(txt_path, "r")

        img_outpath = outpath + img_filename
        print("Output:" + img_outpath)

        """ Convert YOLO format to get xmin,ymin,xmax,ymax """

        lines = txt_file.read().splitlines()

        for idx, line in enumerate(lines):
            value = line.split(',')
            g_id = int(value[0])
            xmin = int(value[1])
            xmax = int(value[1])+int(value[3])
            ymin = int(value[2])
            ymax = int(value[2])+int(value[4])
            box = [xmin, xmax, ymin, ymax]
            img_h, img_w = img.shape[:2]
            bb = convert((img_w, img_h), box)
            print(bb)
            fw.write(f"{g_id} {bb[0]} {bb[1]} {bb[2]} {bb[3]}\n")
            # cv2.rectangle(img, (int(round(bb[0])), int(round(bb[2]))), (int(
            # round(bb[1])), int(round(bb[3]))), (0, 0, 255), 1)
            # uncomment to show label index
            #cv2.putText(img, cls, (int(round(bb[0])),int(round(bb[2]))-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255),2,cv2.LINE_AA)
            #cv2.imwrite(img_outpath, img)
