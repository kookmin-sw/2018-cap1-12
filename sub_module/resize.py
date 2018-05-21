# -*- coding: utf-8 -*-
import cv2
import argparse
import os
import glob # 특정 디렉토리에 있는 파일을 유용하게 사용하게 도와줌
from PIL import Image
import numpy as np

parser = argparse.ArgumentParser(description='image rotation')
parser.add_argument('--src', dest='src_dir', required=True, help='path of the source img')
parser.add_argument('--resize', dest='resize', required=True, help='size of img')
args = parser.parse_args()

if __name__=="__main__":
	src_dir = args.src_dir
	resize = args.resize

	paths = glob.glob(os.path.join(src_dir, "*.jpg"))
	
	for p in paths:
		try : 
			name = os.path.basename(p).split('.jpg')[0]
			img = cv2.imread(p)
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
			height, width = img.shape[:2]
			resize = int(resize)
			half_height = int(height / 2)
			half_width = int(width / 2 )
			if half_width + (resize / 2 ) - (half_height - (resize / 2 ) - 1 ) < resize:
				resize_img = img[half_height - (resize / 2) - 1 : half_height + (resize / 2 ) - 1, half_width - (resize / 2) - 1 : half_width + (resize / 2) - 1]
			elif half_width + (resize / 2 ) - (half_height - (resize / 2 ) - 1 ) > resize:
				resize_img = img[half_height - (resize / 2) : half_height + (resize / 2 ), half_width - (resize / 2)  : half_width + (resize / 2)]
			else : 
				resize_img = img[half_height - (resize / 2) - 1 : half_height + (resize / 2 ), half_width - (resize / 2) - 1 : half_width + (resize / 2)]

			cv2.imwrite(src_dir +'/'+ name + '.jpg' , resize_img)
			print('Success : ' + str(src_dir) +'/' + name + '.jpg')
		except : 
			print('Fail : ' + name + 'File is not exist in src')

	



