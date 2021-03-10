#!/bin/bash

apt-get install -y python3-venv chromium-browser docker docker-compose tigervnc-viewer
rm -rf build/
python3 -m venv build/venv
build/venv/bin/pip3 install selenium pytest pytest-html PyYAML
wget https://github.com/mozilla/geckodriver/releases/download/v0.29.0/geckodriver-v0.29.0-linux64.tar.gz -P build/geckodriver
tar -xf build/geckodriver/geckodriver-v0.29.0-linux64.tar.gz -C /usr/local/bin/
rm -rf build/geckodriver/
touch build/geckodriver.log
chmod +777 build/geckodriver.log
systemctl start docker.service
