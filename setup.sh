#!/bin/sh

mpa_root_dir=/mpa
mpa_user=mpa

if [ -d "$mpa_root_dir" ]; then
 echo "mpa already installed.";
else
 mkdir $mpa_root_dir
fi

 	
