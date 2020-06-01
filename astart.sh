#!/bin/sh

nohup java -Xmx16G -Xmx16G -DRUN_PATH=`pwd` -cp sbin/felix.jar:sbin/protobuf-java-3.6.1.jar -DofwConf=conf/ofw.properties \
	 -Dorg.bc.dpos.force.reset.vote.term=1 -XX:+UseParallelGC -XX:+UseParallelOldGC -XX:+UseAdaptiveSizePolicy \
	 -XX:+UnlockCommercialFeatures -XX:+FlightRecorder -Duser.timezone=GMT+08 \
	 -Dorg.brewchain.man.dev=false  -Dorg.bc.manage.node.net=prodnet \
	 -Dlogback.configurationFile=conf/logback-server.xml org.apache.felix.main.Main &


sleep 5s;
tail -f logs/app.log

