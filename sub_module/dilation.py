#-*- coding: utf-8 -*-
import numpy as np
import cv2
import argparse
import os
import glob

parser = argparse.ArgumentParser(description='image rotation')
parser.add_argument('--src', dest='src_dir', required=True, help='path of the source img')
parser.add_argument('--num', dest='num', required=True, help='num of iterator')
args = parser.parse_args()

if __name__=="__main__":
	src_dir = args.src_dir
	num = args.num

	paths = glob.glob(os.path.join(src_dir, "*.jpg"))

	for p in paths:
		print (p)
		try : 
			name = os.path.basename(p).split('.jpg')[0]
			img = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
			kernel = np.ones((3,3), np.uint8)
			dilation_img = cv2.dilate(np.array(img), kernel, iterations = int(num))
			cv2.imwrite(src_dir +'/'+ name + '.jpg' , dilation_img)
			print('Success : ' + str(src_dir) +'/' + name + '.jpg')
		except : 
			print('Fail : ' + name + 'File is not exist in src')
