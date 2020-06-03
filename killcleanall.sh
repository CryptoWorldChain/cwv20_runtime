#!/bin/sh

pid=$(ps -ef|grep java|grep "RUN_PATH=`pwd`"|awk '{print $2}')

echo killing pid=$pid

kill -9 $pid

kill -9 $pid

./clear.sh


