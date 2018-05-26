#!/bin/bash

# work directory : 2018-cap1-12/
work_dir=$( cd "$(dirname "$0")" ; pwd )

# init
cd ${work_dir}/DiscoGAN-pytorch/data
sudo rm -r sms_dms/A
sudo rm -r sms_dms/B
sudo rm -r ehs_eh/A
sudo rm -r ehs_eh/B
sudo rm -r djqt_dlT/A
sudo rm -r djqt_dlT/B
sudo rm -r ek_EK/A
sudo rm -r ek_EK/B
sudo rm -r ek_rh/A
sudo rm -r ek_rh/B
sudo rm -r fk_rk/A
sudo rm -r fk_rk/B

# resize 192x192
cd ${work_dir}
python sub_module/resize.py --src user/$1 --resize 192

# resize 256x256
cd ${work_dir}/user/$1
mogrify -resize 256x256! -quality 100 *.jpg

# dilation 1
cd ${work_dir}
python sub_module/dilation.py --src user/$1 --num 1

# erosion 2
cd ${work_dir}
python sub_module/erosion.py --src user/$1 --num 1

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

# train
cd DiscoGAN-pytorch
python main.py --dataset=ehs_eh --load_path=logs/ehs_eh --is_train=False
python main.py --dataset=djqt_dlT --load_path=logs/djqt_dlT --is_train=False
python main.py --dataset=ek_EK --load_path=logs/ek_EK --is_train=False
python main.py --dataset=ek_rh --load_path=logs/ek_rh --is_train=False
python main.py --dataset=sms_dms --load_path=logs/sms_dms --is_train=False
python main.py --dataset=fk_rk --load_path=logs/fk_rk --is_train=False

# move
cd ${work_dir}
sudo mv DiscoGAN-pytorch/logs/ehs_eh/test/0_x_A.png    sub_module/svg2ttf/data/B3C8.png # 돈 B3C8
sudo mv DiscoGAN-pytorch/logs/ehs_eh/test/0_x_AB.png   sub_module/svg2ttf/data/B3C4.png # 도 B3C4
sudo mv DiscoGAN-pytorch/logs/djqt_dlT/test/0_x_A.png  sub_module/svg2ttf/data/C5C6.png # 없 C5C6
sudo mv DiscoGAN-pytorch/logs/djqt_dlT/test/0_x_AB.png sub_module/svg2ttf/data/C788.png # 있 C788
sudo mv DiscoGAN-pytorch/logs/ek_EK/test/0_x_A.png     sub_module/svg2ttf/data/B2E4.png # 다 B2E4
sudo mv DiscoGAN-pytorch/logs/ek_EK/test/0_x_AB.png    sub_module/svg2ttf/data/B530.png # 따 B530
sudo mv DiscoGAN-pytorch/logs/ek_rh/test/0_x_AB.png    sub_module/svg2ttf/data/ACE0.png # 고 ACE0
sudo mv DiscoGAN-pytorch/logs/sms_dms/test/0_x_A.png   sub_module/svg2ttf/data/B294.png # 는 B294
sudo mv DiscoGAN-pytorch/logs/sms_dms/test/0_x_AB.png  sub_module/svg2ttf/data/C740.png # 은 C740
sudo mv DiscoGAN-pytorch/logs/fk_rk/test/0_x_A.png     sub_module/svg2ttf/data/B77C.png # 라 B77C
sudo mv DiscoGAN-pytorch/logs/fk_rk/test/0_x_AB.png    sub_module/svg2ttf/data/AC00.png # 가 AC00
sudo mv user/$1/이.jpg sub_module/svg2ttf/data/C774.png # 이 C774
sudo mv user/$1/것.jpg sub_module/svg2ttf/data/AC83.png # 것 AC83

# make font
cd ${work_dir}/sub_module/svg2ttf
python3 main.py
echo 'make font success!!'

# move font & delete font remain file
cd ${work_dir}
sudo mv sub_module/svg2ttf/MyFont.ttf user/$1/$1.ttf
cp user/$1/$1.ttf flask_server/static/fonts
sudo rm sub_module/svg2ttf/MyFont.svg
sudo rm sub_module/data/*
sudo rm -r sub_module/svg2ttf/tmp
