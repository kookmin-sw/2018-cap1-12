# -*- coding: utf-8 -*-
import cv2
import argparse
import os
import glob # 특정 디렉토리에 있는 파일을 유용하게 사용하게 도와줌
import numpy as np

parser = argparse.ArgumentParser(description='image rotation')
parser.add_argument('--src1', dest='src_dir1', required=True, help='path of the source img')
parser.add_argument('--src2', dest='src_dir2', required=True, help='path of the source img')
parser.add_argument('--dst', dest='dst_dir', required=True, help='path of the target img')
args = parser.parse_args()

def merge(p1, p2):
	image1 = cv2.imread(p1)
	image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
				
	image2 = cv2.imread(p2)
	image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

	height1, width1 = image1.shape[:2]
	height2, width2 = image2.shape[:2]

	result = np.concatenate((image1, image2), axis=1)

	return result

def path2file_name(p):
	label = os.path.basename(p).split("_")
	file_name=""
	for a in label:
		file_name+=str(a)
	file_name = file_name.split('.')[0]

	return file_name
	
if __name__=="__main__":
	dst_dir = args.dst_dir
	src_dir1 = args.src_dir1
	src_dir2 = args.src_dir2

	if not os.path.exists(dst_dir):
		os.makedirs(dst_dir)

	paths1 = glob.glob(os.path.join(src_dir1, "*.jpg"))
	paths2 = glob.glob(os.path.join(src_dir2, "*.jpg"))
	
	for p1 in paths1:
		name1 = path2file_name(p1)

		for p2 in paths2:
			name2 = path2file_name(p2)

			if name1 == name2:
				if dst_dir[-1] != '/':
					dst_dir += '/'
				cv2.imwrite(str(dst_dir)+name1+'_merge.jpg',merge(p1,p2))

		


