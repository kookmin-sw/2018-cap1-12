#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageChops, ImageOps
from modify import trim_resize_PIL, noise_filter, svgs2ttf, resize_trim_PIL, vectoralize_potrace


def processing():

	unicodes = ["AC12"]
	input_address = "AppleMyungjo.jpg"
	svg_set = []
	output_images = {}

	for input_unicode in unicodes:
		"""
    	이미지를 로드하고 PIL Image로 변환하여 반환
    	- 입력 : url
    	- 반환 : image
    	"""
		input_PIL = Image.open(input_address)
		# input_PIL.save("input_PIL.png")

		modified_PIL = trim_resize_PIL(input_PIL, 216, 216, 20)
		# modified_PIL.save("modified_PIL.png")

		output_images[input_unicode] = modified_PIL
		# ??? output_images = written2all(input_unicode, modified_PIL, opt, is_demo, unicodes)

		for output_unicode, output_image in output_images.items():
			
			filterd = noise_filter(output_image)
			filterd = resize_trim_PIL(filterd, 800, 1000, 0)
			vectoralized = vectoralize_potrace(filterd, output_unicode)
			svg_set.append(vectoralized)

		modified_PIL = resize_trim_PIL(modified_PIL, 800, 1000, 0)
		vectored_svg = vectoralize_potrace(modified_PIL, input_unicode)
		# print(vectored_svg)
		
		svg_set.append(vectored_svg)

	ttf_converted = svgs2ttf(svg_set)


if __name__ == '__main__':
	processing()

	