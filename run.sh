#!/bin/bash


# work directory : 2018-cap1-12/
work_dir=$( cd "$(dirname "$0")" ; pwd )


# resize
cd ${work_dir}/user/$1
mogrify -resize 256x256! -quality 100 *.jpg


# user data move
cd ${work_dir}
cp user/$1/돈.jpg DiscoGAN-pytorch/data/ehs_eh/train/돈.jpg
cp user/$1/없.jpg DiscoGAN-pytorch/data/djqt_dlT/train/없.jpg
cp user/$1/다.jpg DiscoGAN-pytorch/data/ek_EK/train/다.jpg
cp user/$1/다.jpg DiscoGAN-pytorch/data/ek_rh/train/다.jpg
cp user/$1/는.jpg DiscoGAN-pytorch/data/sms_dms/train/는.jpg
cp user/$1/라.jpg DiscoGAN-pytorch/data/fk_rk/train/라.jpg


# merge
cd ${work_dir}
python sub_module/merge.py --src1 DiscoGAN-pytorch/data/ehs_eh/train   --src2 DiscoGAN-pytorch/data --dst DiscoGAN-pytorch/data/ehs_eh/train/
python sub_module/merge.py --src1 DiscoGAN-pytorch/data/djqt_dlT/train --src2 DiscoGAN-pytorch/data --dst DiscoGAN-pytorch/data/djqt_dlT/train/
python sub_module/merge.py --src1 DiscoGAN-pytorch/data/ek_EK/train    --src2 DiscoGAN-pytorch/data --dst DiscoGAN-pytorch/data/ek_EK/train/
python sub_module/merge.py --src1 DiscoGAN-pytorch/data/ek_rh/train    --src2 DiscoGAN-pytorch/data --dst DiscoGAN-pytorch/data/ek_rh/train/
python sub_module/merge.py --src1 DiscoGAN-pytorch/data/sms_dms/train  --src2 DiscoGAN-pytorch/data --dst DiscoGAN-pytorch/data/sms_dms/train/
python sub_module/merge.py --src1 DiscoGAN-pytorch/data/fk_rk/train    --src2 DiscoGAN-pytorch/data --dst DiscoGAN-pytorch/data/fk_rk/train/




# # train
# cd DiscoGAN-pytorch

# python main.py --dataset=ehs_eh --load_path=logs/ehs_eh --is_train=False
# python main.py --dataset=djqt_dlT --load_path=logs/djqt_dlT --is_train=False
# python main.py --dataset=ek_EK --load_path=logs/ek_EK --is_train=False
# python main.py --dataset=ek_rh --load_path=logs/ek_rh --is_train=False
# python main.py --dataset=sms_dms --load_path=logs/sms_dms --is_train=False
# python main.py --dataset=fk_rk --load_path=logs/fk_rk --is_train=False


# Move : 는, 은
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


