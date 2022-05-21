#!/bin/bash

usage(){
echo "PLease use as mentioned below  
sh $0 <fully_qualified_path_to_config>.yml

Example :
sh $0 ../transfer.yml
"
}


if [ $# -eq 0 ] 
then 
usage
exit 1 
fi

python ../core_file_transfer.py $1
