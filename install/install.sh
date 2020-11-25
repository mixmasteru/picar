sudo service unattended-upgrades stop
sudo apt-get update && sudo apt-get upgrade -y
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-noetic-ros-base
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
sudo apt-get install -y python3-rosdep python3-rosinstall-generator python3-wstool python3-rosinstall build-essential cmake
sudo apt-get install python3-pip
sudo apt-get install i2c-tools

sudo mv 99-com.rules /lib/udev/rules.d/

sudo groupadd i2c
sudo groupadd spi
sudo groupadd gpio

sudo adduser ubuntu gpio
sudo adduser ubuntu spi
sudo adduser ubuntu i2c

sudo apt-get install -y lua5.1 alsa-utils
wget https://archive.raspberrypi.org/debian/pool/main/r/raspi-config/raspi-config_20201108_all.deb
sudo dpkg -i raspi-config_20201108_all.deb
#if neeed sudo apt install --fix-broken

sudo apt-get install ros-noetic-teleop-twist-keyboard