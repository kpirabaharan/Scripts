#!/bin/zsh

source_arg=""
destination_arg=""
r_flag=false


if [ $1 = "-r" ]; then
  r_flag=true
  source_arg=$2
  destination_arg=$3
else
  source_arg=$1
  destination_arg=$2
fi



if [ "$r_flag" = true ]; then
  python ~/Developer/Scripts/Image-Conversion/script.py "recursive" $source_arg $destination_arg
else
  python ~/Developer/Scripts/Image-Conversion/script.py $source_arg $destination_arg
fi