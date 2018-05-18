#!/bin/bash
work_dir=$( cd "$(dirname "$0")" ; pwd )

rm ${work_dir}/DiscoGAN-pytorch/*.pyc

rm -r ${work_dir}/DiscoGAN-pytorch/data/sms_dms/A
rm -r ${work_dir}/DiscoGAN-pytorch/data/sms_dms/B

rm -r ${work_dir}/DiscoGAN-pytorch/logs/sms_dms/test

rm ${work_dir}/sub_module/svg2ttf/MyFont.svg

rm -r ${work_dir}/sub_module/svg2ttf/__pycache__

rm ${work_dir}/sub_module/svg2ttf/data/B294.png
rm ${work_dir}/sub_module/svg2ttf/data/C740.png

rm -r ${work_dir}/sub_module/svg2ttf/tmp

