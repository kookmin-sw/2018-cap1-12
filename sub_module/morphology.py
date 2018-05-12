# -*- coding: utf-8 -*-
import cv2
import argparse
import os
import glob # 특정 디렉토리에 있는 파일을 유용하게 사용하게 도와줌
from PIL import Image
import numpy as np

parser = argparse.ArgumentParser(description='image rotation')
parser.add_argument('--src', dest = 'src_dir', required = True, help = 'path of the source img')
parser.add_argument('--dst', dest = 'dst_dir', required = True, help = 'path of the target img')
parser.add_argument('--mode', dest = 'mode', required = True, help = 'mode : dilation / erotion')
parser.add_argument('--repeat', dest = 'repeat', required = False, help = 'how many times will you repeat?', default = 1)
args = parser.parse_args()

if __name__=="__main__":
	dst_dir = args.dst_dir
	src_dir = args.src_dir
	mode = args.mode
	repeat = args.repeat

	if not os.path.exists(dst_dir):
		os.makedirs(dst_dir)

	paths1 = glob.glob(os.path.join(src_dir, "*.jpg"))
	
	for p1 in paths1:
		try:
			label = os.path.basename(p1).split('.')[0]
			img = cv2.imread(p1)
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

			if dst_dir[-1] != '/':
				dst_dir += '/'

			kernel = np.ones((3, 3), np.uint8)

			if mode == "dilation":
				result = cv2.dilate(img, kernel, iterations = int(repeat))
			elif mode == "erosion":
				result = cv2.erode(img, kernel, iterations = int(repeat))

			cv2.imwrite(str(dst_dir) + label + '_' + mode + '.jpg', result)
			print('Success : ' + str(dst_dir) + label + '_dilation_.jpg')
		except:
			print('Fail')