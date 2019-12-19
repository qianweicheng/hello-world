#!/usr/bin/env bash
set -e
# read -p "Please choose yes/no: " -t 30 cho
cho=$1
case $cho in
    yes|Y)
        echo "Your choose is yes!"
        ;;
    no|N)
        echo "Your choose is no!"
        ;;
    [oO][kK])
        echo "Your choose is ok!"
        ;;
    *)
    echo "Your choose is error!"
    ;;
esac