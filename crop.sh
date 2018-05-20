#!/bin/bash


# Work Directory : 2018-cap1-12/
work_dir=$( cd "$(dirname "$0")" ; pwd )


python3 sub_module/crop.py --src flask_server/static/pictures/testcrop.jpeg --dst flask_server/static/cutImage/ --line 1

# rm flask_server/static/cutImage/crop_back.jpg
# rm flask_server/static/cutImage/line1_total.jpg