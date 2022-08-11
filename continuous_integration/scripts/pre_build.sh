#!/bin/bash

apt-get update
apt-get install git build-essential cmake libeigen3-dev valgrind
ln -s /usr/include/eigen3/Eigen /usr/include/Eigen
ls /usr/include      
