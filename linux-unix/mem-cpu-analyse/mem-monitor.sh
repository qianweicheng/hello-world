#!/usr/bin/env bash
filename=`date "+%Y%m%d%H%M%S"`
log_file_count=`ls -l mem-track.*.log | wc -l`
filename="mem-track.${log_file_count}.log"
echo log file: $filename
unset last_text
while true;
do
    pid=`ps aux | awk '$11~/docker-java-home/{print $2}'`
    if [ -z $pid ];then
        pid=`ps aux | awk '$11~/java/{print $2}'`
    fi
    # echo pid:$pid
    timestamp=`date "+%Y-%m-%d %H:%M:%S"`
    current_text=$(cat /proc/$pid/status | awk '/VmHWM/{printf("%s", $0)}')
    if [[ "$last_text" != "$current_text" ]];then
        new_log=${timestamp}\t${current_text}
        echo $new_log >> "$filename"
        echo $new_log
        last_text=$current_text
    fi
    sleep 5;
done