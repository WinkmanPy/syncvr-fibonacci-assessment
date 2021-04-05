#!/bin/bash

number=0
while [ $number -le 100 ]
do
    echo "$(curl -s http://127.0.0.1:5000/api/${number})"
    ((number++))
done
