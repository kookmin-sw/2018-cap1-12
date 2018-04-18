# -*- coding: utf-8 -*-
import cv2
import argparse
import os
import glob # 특정 디렉토리에 있는 파일을 유용하게 사용하게 도와줌



parser = argparse.ArgumentParser(description='image rotation')
parser.add_argument('--src', dest='src_dir', required=True, help='path of the source img')
parser.add_argument('--dst', dest='dst_dir', required=True, help='path of the target img')
parser.add_argument('--degree', dest='degree', required=True, help='Degree of leaning')
args = parser.parse_args()


def rotation(p, degree):
	imgBGR = cv2.imread(p)
	imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

	height, width = imgRGB.shape[:2]
	
	diagonal = int(((width*width + height*height)**0.5)) 
	rotation_center = float(width/2), float(height/2)
		
	rotation_degree = int(degree)
	new_height, new_width = height, width

	img_rotation = cv2.getRotationMatrix2D(rotation_center, rotation_degree, 1.0) 
	rotation_result = cv2.warpAffine(imgRGB, img_rotation, (new_height, new_width),flags=cv2.INTER_LINEAR,borderMode=cv2.BORDER_REFLECT_101)

	return rotation_result


if __name__=="__main__":
	dst_dir = args.dst_dir
	src_dir = args.src_dir
	degree = args.degree

	if not os.path.exists(dst_dir):
		os.makedirs(dst_dir)

	paths = glob.glob(os.path.join(src_dir, "*.jpg"))
	
	for p in paths:
		label = os.path.basename(p).split("_")
		name=""
		for a in label:
			name+=str(a)

		name = name.split('.')[0]

		result_img = rotation(p, degree)

		if dst_dir[-1] != '/':
			dst_dir += '/'
		
		cv2.imwrite(str(dst_dir)+name+'_rotation_'+degree+'.jpg',result_img)


