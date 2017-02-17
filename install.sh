#!/bin/bash

USER="anton"
ftp_user="ekb"
ftp_password="cb4yb5wf"
ftp_ip="127.0.0.1"

mkdir /etc/udev/rules.d/sp

cp camera.sh /etc/udev/rules.d/sp/camera.sh
cp sp.sh /etc/udev/rules.d/sp/sp.sh
cp sp.py /etc/udev/rules.d/sp/sp.py
cp usb.rules /etc/udev/rules.d/usb.rules

chmod +x /etc/udev/rules.d/sp/camera.sh
chmod +x /etc/udev/rules.d/sp/sp.sh
chmod +x /etc/udev/rules.d/sp/sp.py

apt-get install curlftpfs
apt-get install python3
apt-get install gphoto2
