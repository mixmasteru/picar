sudo service unattended-upgrades stop
sudo apt-get update && sudo apt-get upgrade -y
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-noetic-ros-base
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
sudo apt-get install -y python3-rosdep python3-rosinstall-generator python3-wstool python3-rosinstall build-essential cmake
