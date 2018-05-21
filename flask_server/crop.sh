#!/bin/bash


echo $2
python3 ../sub_module/crop.py --src static/pictures/testcrop.jpeg --dst static/cutImage/ --line $1


# mkdir ../user/$2
# rm static/cutImage/crop_back.jpg
# rm static/cutImage/line1_total.jpg
# cp static/cutImage/* user/$2
# rm static/cutImage/*