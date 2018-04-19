# -*- coding: utf-8 -*- 
import cv2
import numpy as np
import argparse
import os
import glob




parser = argparse.ArgumentParser(description='image rotation')
parser.add_argument('--src', dest='src_dir', required=True, help='path of the source img')
parser.add_argument('--dst', dest='dst_dir', required=True, help='path of the target img')
parser.add_argument('--scale', dest='scale', required=True, help='Degree of scale')
args = parser.parse_args()

if __name__=="__main__":
	dst_dir = args.dst_dir
	src_dir = args.src_dir
	scale_degree = args.scale

	if not os.path.exists(dst_dir):
		os.makedirs(dst_dir)

	paths = glob.glob(os.path.join(src_dir, "*.jpg"))

	for p in paths:
		label = os.path.basename(p).split("_")
		name=""

		for a in label:
			name+=str(a)

		name = name.split('.')[0]
		img = cv2.imread(p)
		height, width = img.shape[:2]

		scale_img = cv2.resize(img, None, fx=float(scale_degree), fy=float(scale_degree), interpolation=cv2.INTER_AREA)
		
		if dst_dir[-1] !='/':
			dst_dir+='/'

		cv2.imwrite(str(dst_dir)+name+'_scale_'+scale_degree+'.jpg',scale_img)

