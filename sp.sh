

# Создаем папки на тот случай если их вдруг нет
mkdir "/mnt/ftp/$1/$2/Загрузка"
mkdir "/mnt/ftp/$1/$2/Выгрузка"

# cd "/mnt/ftp/$1/$2/$3"
mkdir ~/camera
gphotofs ~/camera

cp -R ~/camera/store_00010001/DCIM/* "/mnt/ftp/$1/$2/$3"
# echo "/mnt/ftp/$1/$2/$3" > TEST2.TXT
# sleep 1

# gphoto2 --get-all-files --skip-existing --folder "/store_00010001/DCIM" > /home/anton/TEST.TXT

if [ $4 -eq '1' ]
then
    rm -rf ~/camera/store_00010001/DCIM/*
    # gphoto2 --delete-all-files --recurse --folder "/store_00010001/DCIM"
fi

fusermount -u ~/camera
rmdir ~/camera