#!/bin/bash

# work directory : 2018-cap1-12/
work_dir=$( cd "$(dirname "$0")" ; pwd )

# crop
cd ${work_dir}
python3 sub_module/crop.py --src flask_server/static/pictures/$1 --dst flask_server/static/cutImage/ --line $2

# copy to user
mkdir user
mkdir user/$3
rm flask_server/static/cutImage/crop_back.jpg
rm flask_server/static/cutImage/line*.jpg
cp flask_server/static/cutImage/* user/$3