set -x

brew install eigen
ln -s /usr/local/Cellar/eigen/3.3.4/include/eigen3/Eigen /usr/local/include/Eigen
echo | gcc -E -Wp,-v -
ls /usr/local/include
