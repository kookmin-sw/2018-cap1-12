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
args = parser.parse_args()

if __name__=="__main__":
	dst_dir = args.dst_dir
	src_dir = args.src_dir
	

	if not os.path.exists(dst_dir):
		os.makedirs(dst_dir)

	paths1 = glob.glob(os.path.join(src_dir, "*.png"))
	
	for p1 in paths1:
		try:
			label = os.path.basename(p1).split('.')[0]
			img = cv2.imread(p1)
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

			if dst_dir[-1] != '/':
				dst_dir += '/'

			median = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
			b, g, r = cv2.split(median)
			median_dst=cv2.merge([r,g,b])
			median = median_dst

			cv2.imwrite(str(dst_dir) + label + '.png', median)
			print('Success : Denoise ' + str(dst_dir) + label + '.png')
		except:
			print('Fail')

