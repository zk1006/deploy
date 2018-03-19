#! /bin/bash

apt-get install git -y
apt-get install openssl -y
apt-get install libssl-dev -y

git clone https://github.com/zk1006/deploy.git

wget https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz

tar zxvf Python-3.6.4.tgz

cd Python-3.6.4/

./configure --prefix=/opt/python3.6 && make && make install

echo "export PATH=/opt/python3.6/bin:\$PATH" >>/etc/profile

source /etc/profile

ln -s /opt/python3.6/bin/pip3 /usr/bin/pip3
rm -rf /usr/bin/python3
ln -s /opt/python3.6/bin/python3 /usr/bin/python3

cd ../deploy

pip3 install --upgrade pip
pip3 install -r requirements.txt