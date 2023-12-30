#!/bin/bash

if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

input_file=$1
full_path=$(realpath "$input_file")

echo "[Unit]" > CLay.service
echo "Description=CLay Service" >> CLay.service
echo "After=network.target" >> CLay.service
echo "" >> CLay.service
echo "[Service]" >> CLay.service
echo "ExecStart=CLay -c \"$full_path\"" >> CLay.service
echo "Restart=always" >> CLay.service
echo "User=$SUDO_USER" >> CLay.service
echo "" >> CLay.service
echo "[Install]" >> CLay.service
echo "WantedBy=default.target" >> CLay.service

mv CLay.service /etc/systemd/system/

systemctl daemon-reload
systemctl start CLay

systemctl enable CLay

echo "Service created and started successfully!"
