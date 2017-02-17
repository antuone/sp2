#!/bin/bash
ftp_user="ekb"
ftp_password="cb4yb5wf"
ftp_ip="127.0.0.1"
mkdir /mnt/ftp
curlftpfs ${ftp_user}:${ftp_password}@${ftp_ip}/ /mnt/ftp -o allow_other
su anton -c "export DISPLAY=:0; bash -c 'python3 /etc/udev/rules.d/sp/sp.py'"
umount /mnt/ftp
rmdir /mnt/ftp
