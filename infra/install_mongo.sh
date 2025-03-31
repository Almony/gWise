#!/bin/bash

set -e

curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \
  sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \
  --dearmor

echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] \
https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | \
  sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list


echo "Install MongoDB on the server"
sudo apt update
sudo apt install -y mongodb-org

echo "Start enable and start MongoDB"
sudo systemctl start mongod
sleep 1
sudo systemctl enable mongod

echo "MongoDB installed and running..."
sudo systemctl status mongod --no-pager

