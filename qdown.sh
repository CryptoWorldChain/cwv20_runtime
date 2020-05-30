#!/bin/sh

pid=$(ps -ef|grep java|grep "RUN_PATH=`pwd`"|awk '{print $2}')

echo killing pid=$pid

kill $pid

