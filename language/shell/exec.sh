#!/usr/bin/env bash
sleep 10 &
jobid=$!
counter=0
while true;do
    d=`ps -p $jobid | wc -l`
    if [ $d -gt 1 ];then
        echo ${counter} still running...
        sleep 3
        counter=$((counter+3))
    else
        break
    fi
done
echo finished.