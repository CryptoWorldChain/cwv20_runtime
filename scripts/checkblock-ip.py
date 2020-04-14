import requests
from prettytable import PrettyTable
import re
import json
import time
import os
import traceback



ipport='172.19.191.241:8002'

session = requests.session()

while 1>0:
    x = PrettyTable(["bcuid", "block","bcuid1","block1","bcuid2","block2"])
    x.border = True
    try:     
    	pzpurl='http://fc0:8000/fbs/pzp/pbinf.do?bd={"nid":"vrf"}'
    	resp=session.get(pzpurl,timeout=10)
    	jsonData = resp.json()
    	bcuidmap={}
    	pendindbcuidmap={}
	coaddrmap={}
	if 'dnodes' in jsonData:
    		nodes=jsonData['dnodes']
    		for node in nodes :
       			bcuidmap[node['bcuid']]=node
			coaddrmap[node['co_address']]=node
        else:
		nodes=[]

	if 'pnodes' in jsonData:
	        pnodes= jsonData['pnodes']
               	pnodessize = len(jsonData['pnodes'])
		for pnode in pnodes :
			pendindbcuidmap[pnode['bcuid']]=pnode
        else:
 	       	pnodessize = 0
		pnodes=[]

	url='http://fc0:8000/fbs/sio/pbcio.do'
        resp=session.get(url,timeout=10)
        jsonData = resp.json()

	if 'totalReceiveTx' in jsonData:
		totalReceiveTx = jsonData['totalReceiveTx']
	else:
		totalReceiveTx = 0
	if  'totalProcessTx' in jsonData:
		totalProcessTx = jsonData['totalProcessTx']
	else:
		totalProcessTx = 0

    	url='http://fc0:8000/fbs/vrf/pbinf.do?bd={"messageid":"a"}'
   	resp=session.get(url,timeout=10)
    	jsonData = resp.json()
    	murs = jsonData['murs']
	
	if 'vn' in jsonData :
		vn = jsonData['vn']
	else:
		vn = {}
    	size = len(murs)
    	outx = []
    	for mur in murs :
		if bcuidmap.has_key(mur['bcuid']) :
       			node = bcuidmap[mur['bcuid']]['uri'][6:]
       		else:
			if pendindbcuidmap.has_key(mur['bcuid']) :
				node = "p."+pendingbcuidmap[mur['bcuid']]['uri'][6:]
			else:
				node=mur['bcuid']
		
		outx.append([node,mur['cur_block']])
    	outx.sort(key=lambda x:x[0])
    	for idx in range(0,size,3):
        	try:
            		mur = outx[idx]
	    
	    		if idx + 1 < size :
				mur1 = outx[idx+1]
	    		else:
				mur1 = ['-','-']

            		if idx + 2 < size :
                		mur2 = outx[idx+2]
            		else:
                		mur2 = ['-','-']
	    		x.add_row([mur[0],mur[1],mur1[0],mur1[1],mur2[0],mur2[1]])            

	        except:
        	    x.add_row(['-','-','-','-','-','-'])

    	os.system('clear')
    	print ">>>>>>>>>>>>>>    DNodes="  + str(len(nodes)) +  " PNodes=" + str(pnodessize) +"  >>>>>>>>>" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    	print x
	if coaddrmap.has_key(vn['cur_block_miner_coaddr']) :
		minerhostport=coaddrmap[vn['cur_block_miner_coaddr']]['uri'][6:]
	else:
		minerhostport='-'

	print ">>> miner: " + vn['cur_block_miner_coaddr'] + " height: "+str(vn['cur_block']) +" uri: "+minerhostport +" pending="+str(totalReceiveTx-totalProcessTx)+",confirmed="+str(totalProcessTx)
    except Exception ,e:
        #os.system('clear')
        exstr = traceback.format_exc()
	print 'not ready >>' + exstr	
	time.sleep(10)
	os.system('clear')
    time.sleep(1)
