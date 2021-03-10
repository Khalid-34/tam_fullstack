#!/bin/bash 
echo "UBUNTU POST-INSTALL SCRIPT"
apt -yq install net-tools 

echo "Setting local date/time"
timedatectl set-timezone Europe/Paris

echo "Installing base packages"
apt-get -yq install  git git-extras build-essential python3-pip 

echo "PermitRootLogin without-password" >> /etc/ssh/sshd_config
sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

clear 

echo "Necessary modules installation"

echo "Installing sqlite module" 
sudo pip install pysqlite3 

clear

echo "Installing Flask module"
sudo pip3 install Flask

echo "Installing Flask-CORS module"
sudo pip3 install -U flask-cors

clear

echo "Updating APT..."
apt-get update

clear

echo "Exporting the Flask app"
export FLASK_APP=app.py

echo "Running the Flask server"
flask run --host=0.0.0.0 --port=80







