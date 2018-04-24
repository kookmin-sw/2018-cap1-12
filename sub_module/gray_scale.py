# -*- coding: utf-8 -*-
import cv2
import argparse
import os
import glob # 특정 디렉토리에 있는 파일을 유용하게 사용하게 도와줌



parser = argparse.ArgumentParser(description='image rotation')
parser.add_argument('--src', dest='src_dir', required=True, help='path of the source img')
parser.add_argument('--dst', dest='dst_dir', required=True, help='path of the target img')

args = parser.parse_args()


def gray_scale(p):
	imgBGR = cv2.imread(p)
	imgGRAY = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
	return imgGRAY


if __name__=="__main__":
	dst_dir = args.dst_dir
	src_dir = args.src_dir

	if not os.path.exists(dst_dir):
		os.makedirs(dst_dir)

	paths = glob.glob(os.path.join(src_dir, "*.jpg"))
	
	if paths == []:
		print("Source directory does not exist.")

	for p in paths:
		label = os.path.basename(p).split("_")
		name=""
		for a in label:
			name+=str(a)

		name = name.split('.')[0]

		result_img = gray_scale(p)

		if dst_dir[-1] != '/':
			dst_dir += '/'
		
		cv2.imwrite(str(dst_dir)+name+'_gray.jpg',result_img)


