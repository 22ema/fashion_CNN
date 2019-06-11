#!/bin/bash

a="0"
while : 

do
 vCount="0" 
 echo "press ctrl+c to stop..."
 vCount="./image/"$a
 vCount=$vCount".jpg" 
 echo "${a}"
 python clothes_test.py ${vCount}
 if [ -s ${vCount} ]; then
  a=`expr ${a} + 1`
  echo "file exist"
 else
  echo "file not exist"
 fi 
 sleep 2s  
done
echo "execute!!"

