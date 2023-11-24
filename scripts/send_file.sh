#!/bin/bash

usage(){
echo "Please use as mentioned below  
sh $0 <fully_qualified_path_to_config>.yml

Example :
sh $0 ../transfer.yml
"
}

if [ $# -eq 0 ] 
then
echo "Using default file transfer.yml"
sh $0 ../transfer.yml
fi

python ../core_file_transfer.py $1
