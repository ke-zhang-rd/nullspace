set -xe

ls /usr/include 
yum -y install eigen3-devel
ln -s /usr/include/eigen3/Eigen /usr/include/Eigen
ls /usr/include
