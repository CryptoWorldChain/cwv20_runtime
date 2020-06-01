#!/bin/sh

nohup java -Xmx16G -Xmx16G -DRUN_PATH=`pwd` -cp sbin/felix.jar:sbin/protobuf-java-3.6.1.jar -DofwConf=conf/ofw.properties \
	 -Dorg.bc.dpos.force.reset.vote.term=1 -XX:+UseParallelGC -XX:+UseParallelOldGC -XX:+UseAdaptiveSizePolicy \
	 -XX:+UnlockCommercialFeatures -XX:+FlightRecorder -Duser.timezone=GMT+08 \
	 -Dorg.brewchain.man.dev=false  -Dorg.bc.manage.node.net=prodnet \
	 -Dorg.apache.felix.http.jetty.acceptors=16 \
	 -Dorg.bc.pzp.networks.loc.id=$HOSTNAME \
	 -Dorg.bc.pzp.networks.loc.gwuris=$HOSTNAME:5100 \
	 -Dorg.brewchain.account.coinbase.address=3c1ea4aa4974d92e0eabd5d024772af3762720a0 \
	 -Dorg.bc.pzp.networks.vrf.nodelist="tcp://fc0:5100,tcp://fc1:5100,tcp://fc2:5100,tcp://fc3:5100,tcp://fc4:5100" \
	 -Dlogback.configurationFile=conf/logback-server.xml org.apache.felix.main.Main &


sleep 5s;
tail -f logs/app.log

