#!/bin/bash

ENV_VAR_FILE="setenv.sh"

if [ ! -f $ENV_VAR_FILE ];
then
    WORK_DIR=${PWD}
    NEW_FILE_PATH=${PWD}/$ENV_VAR_FILE
    #DDS_VARS=$(readlink -f ../third-party-build/DDS/setenv.sh)

    echo 'export MORSE_ROOT=/opt/morse' > ${ENV_VAR_FILE}
    
    echo 'export PATH=/opt/morse/bin:${PATH}' >> ${ENV_VAR_FILE}
    echo 'export MORSE_BLENDER=~/apps/blender-2.67a-linux-glibc211-x86_64/blender' >> ${ENV_VAR_FILE}
    echo 'export PYTHONPATH=/opt/morse/lib/python3.3/site-packages:${PYTHONPATH}' >> ${ENV_VAR_FILE}

    echo 'export QTDIR=/usr/share/qt4' >> ${ENV_VAR_FILE}
    echo 'export PATH=${PATH}:~/apps/blender-2.67a-linux-glibc211-x86_64' >> ${ENV_VAR_FILE}

    echo "export MORSE_RESOURCE_PATH=${PWD}/turtlebot_sim/data" >> ${ENV_VAR_FILE}                           
    echo "export PYTHONPATH=${PWD}"'/turtlebot_sim/src:${PYTHONPATH}' >> ${ENV_VAR_FILE}
    
    echo 'export MORSE_RESOURCE_PATH=${MORSE_RESOURCE_PATH}:'"${PWD}/videoray_sim/data" >> ${ENV_VAR_FILE}
    echo "export PYTHONPATH=${PWD}"'/videoray_sim/src:${PYTHONPATH}' >> ${ENV_VAR_FILE}
    
    echo 'export MORSE_RESOURCE_PATH=${MORSE_RESOURCE_PATH}:'"${PWD}/diver_sim/data" >> ${ENV_VAR_FILE}
    echo "export PYTHONPATH=${PWD}"'/diver_sim/src:${PYTHONPATH}' >> ${ENV_VAR_FILE}
    
    echo 'export MORSE_RESOURCE_PATH=${MORSE_RESOURCE_PATH}:'"${PWD}/uhri_sim/data" >> ${ENV_VAR_FILE}
    echo "export PYTHONPATH=${PWD}"'/uhri_sim/src:${PYTHONPATH}' >> ${ENV_VAR_FILE}
    
    echo 'export MORSE_RESOURCE_PATH=${MORSE_RESOURCE_PATH}:'"${PWD}" >> ${ENV_VAR_FILE}

    chmod +x ${ENV_VAR_FILE}

    echo "-----------------------------------------------------"
    echo "Generated environment file"
    echo "Add the following to your .bashrc file for future use"
    echo "        source ${NEW_FILE_PATH}"
else
    echo "Environment file already exists, execute ./uninstall.sh to remove"
fi

source $ENV_VAR_FILE
