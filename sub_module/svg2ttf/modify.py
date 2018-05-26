#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageChops, ImageOps
from svg2ttf import insert2target, svgicon2svgfont, svg2ttf, cp_svg
import os
# import logging
# import base64
# from io import BytesIO
# import io
# import requests
# import json
import numpy as np
import cv2


def scale(image, max_size, method=Image.ANTIALIAS):
    im_aspect = float(image.size[0]) / float(image.size[1])
    out_aspect = float(max_size[0]) / float(max_size[1])
    if im_aspect >= out_aspect:
        scaled = image.resize(
            (max_size[0], int((float(max_size[0]) / im_aspect) + 0.5)), method)
    else:
        scaled = image.resize(
            (int((float(max_size[1]) * im_aspect) + 0.5), max_size[1]), method)

    offset = (int((max_size[0] - scaled.size[0]) / 2), int(
        (max_size[1] - scaled.size[1]) / 2))
    # print(offset)
    back = Image.new("RGB", max_size, "white")
    back.paste(scaled, offset)
    return back


def trim_resize_PIL(input_PIL, width, height, border):
    bg = Image.new(input_PIL.mode, input_PIL.size, input_PIL.getpixel((0, 0)))
    diff = ImageChops.difference(input_PIL, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    image_output = input_PIL.crop(bbox)
    image_output = scale(image_output, [width, height])
    image_output = ImageOps.expand(image_output, border=border, fill='white')
    return image_output


def resize_trim_PIL(input_PIL, width, height, border):
    # resize
    image_output = scale(input_PIL, [width, height])
    image_output = ImageOps.expand(image_output, border=border, fill='white')

    # trim
    bg = Image.new(image_output.mode, image_output.size, image_output.getpixel((0, 0)))
    diff = ImageChops.difference(image_output, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    image_output = image_output.crop(bbox)
    return image_output


def noise_filter(PIL_img):
    """
    IF use convertio, THEN just pass out the input
    ELSE, take PIL image and return PIL image
    """
    kernel = np.ones((5,5), np.uint8)
    PlL_img = cv2.erode(np.array(PIL_img), kernel, iterations = 1)
    PlL_img = cv2.dilate(np.array(PIL_img), kernel, iterations = 1)
    denoides_img = PIL_img
    
    return denoides_img


# def vectoralize(PIL_img, unicod):
#     """
#     take PIL, convert to base64, pass through convertio API, return 'path/name.svg'
#     """
#     # change PIL -> base64
#     buffer = BytesIO()
#     PIL_img.save(buffer, format='JPEG')
#     convert_base64 = base64.b64encode(buffer.getvalue())

#     # POST base64 for conversion
#     url_post_base64 = 'https://api.convertio.co/convert'
#     params_post = {'apikey': os.environ["CONVERTIO_TOKEN"],
#                    'input': 'base64',
#                    'file': convert_base64.decode("utf-8"),
#                    'filename': 'BD00.jpg',
#                    'outputformat': 'svg'}
#     req_post_base64 = requests.post(url_post_base64, data=json.dumps(params_post))

#     #GET conversion status
#     res_post_base64 = json.loads(req_post_base64.text)
#     url_get_status = 'https://api.convertio.co/convert/' + res_post_base64['data']['id'] + '/status'
#     params_get = { 'id': res_post_base64['data']['id'] }
#     while(True):
#         req_get_status = requests.get(url_get_status, params=params_get)
#         res_get_status = json.loads(req_get_status.text)
#         if res_get_status['data']['step'] == 'finish':
#             break

#     # GET result file (svg) with base64 encoded
#     url_get_base64 = 'http://api.convertio.co/convert/' + res_post_base64['data']['id'] + '/dl/' + 'base64'
#     params_get = {'id': res_post_base64['data']['id']}
#     req_get_result = requests.get(url_get_base64, params = params_get)
#     print(req_get_result.status_code)
#     print(req_get_result.text)
#     res_get_base64 = json.loads(req_get_result.text)
#     converted_base64 = res_get_base64['data']['content']

#     #save base64 to svg in local
#     bytes_form_base64 = converted_base64.encode()
#     decoded_base64 = base64.b64decode(bytes_form_base64)
#     unicod = unicod
#     with open('u' + unicod.upper() + '-UNI' + unicod.lower() + '.svg', 'wb') as svg_file:
#         svg_file.write(decoded_base64)

#     vectored_local_svg = 'u' + unicod.upper() + '-UNI' + unicod.lower() + '.svg'
#     return vectored_local_svg


def vectoralize_potrace(PIL_img, unicod):
    """
    take PIL, convert to svg and save to vectored_local_svg
    """
    path = 'tmp/'
    if not os.path.isdir("./" + path):
        os.mkdir("./" + path)

    file_name = 'u' + unicod.upper() + '-UNI' + unicod.lower()
    PIL_img.save(path + file_name + '.bmp')
    # logging.info(":: [system call] potrace -s %s" % (path + file_name + '.bmp'))
    os.system("potrace -s %s" % (path + file_name + '.bmp'))
    vectored_local_svg = path + file_name + '.svg'
    return vectored_local_svg


def svgs2ttf(svg_set):
    """
    go through hash 'svg_set', read each unicode & svgfile, compine all to one ttf file and return single ttf file
    svg_set is svg filenames
    """
    DEFAULT_SVG = 'assets/base.svg'
    FONT_NAME = 'MyFont'
    NEW_SVG = FONT_NAME + ".svg"
    cp_svg(DEFAULT_SVG, NEW_SVG)
    for svg in svg_set:
        svgicon2svgfont(svg, 'making_tmp.svg')
        insert2target('making_tmp.svg', NEW_SVG)

    # svg2woff(NEW_SVG)
    svg2ttf(NEW_SVG)
    os.remove('making_tmp.svg')
    # logging.info(":: svgs2ttf done! removed file [%s]" % ('making_tmp.svg'))

    # woff_converted = FONT_NAME + '.woff'
    ttf_converted = FONT_NAME + '.ttf'
    return ttf_converted
