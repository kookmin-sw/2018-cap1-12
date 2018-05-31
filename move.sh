# work directory : 2018-cap1-12/
work_dir=$( cd "$(dirname "$0")" ; pwd )

cd ${work_dir}/flask_server/static/fonts

sudo cp $1 /home/ubuntu/sw/demo1/flask_server/static/fonts
sudo cp $1 /home/ubuntu/sw/demo2/flask_server/static/fonts