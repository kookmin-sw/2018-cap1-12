# -*- coding: utf-8 -*- 
import cv2;
import numpy as np
import argparse
import os
import glob
from matplotlib import pyplot as plt
from matplotlib.image import imsave



parser = argparse.ArgumentParser(description='img crop')
parser.add_argument('--src', dest = 'src_dir', required=True, help='path of the source img')
parser.add_argument('--dst', dest = 'dst_dir', required=True, help='path of the target img')
parser.add_argument('--line', dest = 'line', required=True, help='line of crop')
args = parser.parse_args()

def crop_white_background(img_gray, Height, Width):
	back_start_height = 391
	back_end_height = Height - 328 
	back_start_width = 324
	back_end_width = Width-280
	crop_background_img = img_gray[back_start_height:back_end_height, back_start_width:back_end_width]
	return crop_background_img

def crop_column_img(line, crop_background_img, start_height, end_height, dst_dir):
	names = ['돈', '이', '없', '다', '라', '는', '것']

	file_name='/line' + str(line)
	start_word = 0
	back_Height, back_Width = crop_background_img.shape
	back_width_offset = back_Width / 7
	for a in range(1,8):
		crop_img = crop_background_img[int(start_height) : int(end_height) , start_word:start_word+back_width_offset]
		# cv2.imwrite(dst_dir + file_name + '_' + str(a) + '.jpg', crop_img)
		cv2.imwrite(dst_dir + names[a-1] + '.jpg', crop_img)
		print('Crop Success the '+ str(line) + '번째 라인의' + str(a) + ' word')
		start_word += back_width_offset



def main():
	src_dir = args.src_dir
	dst_dir = args.dst_dir
	line = int(args.line)

	if not os.path.exists(dst_dir):
		os.makedirs(dst_dir)

	img = cv2.imread(src_dir, cv2.IMREAD_COLOR)
	Height, Width, Channel = img.shape							
	print (Height, Width, Channel)								
	if Channel==3:												
		img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	crop_background_img = crop_white_background(img_gray, Height, Width)
	cv2.imwrite(dst_dir+'crop_back.jpg', crop_background_img)
	back_Height, back_Width = crop_background_img.shape


	back_height_offset = back_Height / 10

	if line == 1:
		start_height=0
	else : 
		start_height = (line-1) * back_height_offset
	end_height = start_height + back_height_offset

	crop_line_img = crop_background_img[int(start_height) : int(end_height), 0 : Width]
	cv2.imwrite(dst_dir+'/line'+str(line)+'_total.jpg',crop_line_img)					

	crop_column_img(line, crop_background_img, start_height, end_height, dst_dir)



if __name__ == '__main__':										
	main()