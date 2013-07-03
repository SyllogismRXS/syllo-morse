#!/bin/bash

# Script usage display function
usage()
{
cat << EOF
usage: $0

This script installs MORSE and its dependencies

EOF
}

# Require the script to be run as root
if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo 
    echo "This script must be run as root because libraries will be installed."
    usage
    exit
fi

# Grab username of caller for later
ME=$(who am i | awk '{print $1}')

###############################################################################
# Install Basic Dependencies
###############################################################################
./pkg-deps.sh

###############################################################################
# Setup 3rd Party Build Directory
###############################################################################
BUILD_DIR=$(readlink -f ../3rd-party-build)

if [ ! -d  $BUILD_DIR ];
then
    su $ME -m -c "mkdir -p $BUILD_DIR"
fi

###############################################################################
# Download and install Python 3.3.x
###############################################################################
if [ ! -d $BUILD_DIR/Python-3.3.0 ];
then
    
    pushd $BUILD_DIR >& /dev/null # 1) BUILD_DIR

    su $ME -m -c "wget http://www.python.org/ftp/python/3.3.0/Python-3.3.0.tar.bz2"
    su $ME -m -c "tar xvf Python-3.3*"

    pushd ./Python-3.3* >& /dev/null # 2) Python-3.3

    su $ME -m -c "./configure"
    su $ME -m -c "make"
    make install
    ldconfig

    popd >& /dev/null # 2) Python-3.3
    popd >& /dev/null # 1) BUILD_DIR
fi


###############################################################################
# Clone MORSE Repo and Build
###############################################################################
REPO_DIR=$(readlink -f ~/repos)

if [ ! -d  $REPO_DIR ];
then
    su $ME -m -c "mkdir -p $REPO_DIR"
fi

pushd ~/repos >& /dev/null # 1) ~/repos

if [ ! -d $REPO_DIR/morse ];
then
    su $ME -m -c "git clone https://github.com/morse-simulator/morse.git"
fi

pushd ./morse >& /dev/null # 2) ./morse

su $ME -m -c "mkdir -p ./build"

pushd ./build >& /dev/null # 3) ./build

su $ME -m -c "cmake .. -DBUILD_ROS_SUPPORT=ON \
                       -DCMAKE_BUILD_TYPE=Release \
                       -DCMAKE_INSTALL_PREFIX=/opt/morse \
                       -DPYMORSE_SUPPORT=ON"

su $ME -m -c "make"
make install

popd >& /dev/null # 3) ./build
popd >& /dev/null # 2) ./morse
popd >& /dev/null # 1) ~/repos

###############################################################################
# Generate Environment Variables file 
###############################################################################
pushd ../ >& /dev/null
su $ME -m -c "./install.sh"
popd >& /dev/null
