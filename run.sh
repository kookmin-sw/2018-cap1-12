#!/bin/bash



# Work Directory : 2018-cap1-12/
work_dir=$( cd "$(dirname "$0")" ; pwd )



# Train : 는_은
# ----------------------------
# 	 dataset : data/sms_dms/
#	loadpath : logs/sms_dms/
#	 isTrain : False
# ----------------------------
cd DiscoGAN-pytorch
python main.py --dataset=djqt_dlT --load_path=logs/djqt_dlT --is_train=False
python main.py --dataset=ehs_eh --load_path=logs/ehs_eh --is_train=False
python main.py --dataset=ek_EK --load_path=logs/ek_EK --is_train=False
python main.py --dataset=ek_rh --load_path=logs/ek_rh --is_train=False
python main.py --dataset=fk_rk --load_path=logs/fk_rk --is_train=False
python main.py --dataset=sms_dms --load_path=logs/sms_dms --is_train=False




# Move : 는, 은
# --------------------------------
# 	word : 는 (B294)
#	move : 0_x_A.png -> B294.png
# 
# 	word : 은 (C740)
# 	move : 0_x_AB.png -> C740.png
# --------------------------------
# cd ${work_dir}
# mv DiscoGAN-pytorch/logs/sms_dms/test/0_x_A.png sub_module/svg2ttf/data/B294.png
# mv DiscoGAN-pytorch/logs/sms_dms/test/0_x_AB.png sub_module/svg2ttf/data/C740.png



# Make Font
# cd ${work_dir}/sub_module/svg2ttf
# python3 main.py



# Delete Trash File

# -- DiscoGAN-pytorch/
# cd ${work_dir}/DiscoGAN-pytorch
# rm *.pyc
# # rm data/sms_dms/train/*
# rm -r data/sms_dms/A
# rm -r data/sms_dms/B
# rm -r logs/sms_dms/test

# -- sub_module/svg2ttf/
# cd ${work_dir}/sub_module/svg2ttf
# rm -r __pycache__
# rm -r tmp
# rm data/*


