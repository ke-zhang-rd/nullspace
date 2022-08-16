set -x

brew install eigen
ln -s /usr/local/Cellar/eigen/3.3.4/include/eigen3/Eigen /usr/local/include/Eigen
echo | gcc -E -Wp,-v -
ls -la /usr/local/include
ls /usr/local/include/Eigen
