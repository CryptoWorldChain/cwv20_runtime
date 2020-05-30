#!/bin/sh

nohup java -Xmx8G -DRUN_PATH=`pwd` -cp sbin/felix.jar:sbin/protobuf-java-3.6.1.jar -DofwConf=conf/ofw.properties \
	 -Dlogback.configurationFile=conf/logback-server.xml org.apache.felix.main.Main &


sleep 5s;
tail -f logs/app.log

