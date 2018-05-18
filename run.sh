#!/bin/bash
work_dir=$( cd "$(dirname "$0")" ; pwd )


# test
cd DiscoGAN-pytorch
python main.py --dataset=sms_dms --load_path=logs/sms_dms/ --is_train=False


# move
cd ${work_dir}
mv DiscoGAN-pytorch/logs/sms_dms/test/0_x_A.png sub_module/svg2ttf/data/B294.png
mv DiscoGAN-pytorch/logs/sms_dms/test/0_x_AB.png sub_module/svg2ttf/data/C740.png


# svg2ttf
cd ${work_dir}/sub_module/svg2ttf/
python3 main.py