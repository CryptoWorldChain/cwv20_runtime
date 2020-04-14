import requests
from prettytable import PrettyTable
import re
import json
import time
import os



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
    	nodes=jsonData['dnodes']
    	for node in nodes :
       		bcuidmap[node['bcuid']]=node
        if 'pnodes' in jsonData:
             	pnodessize = len(jsonData['pnodes'])
        else:
 	       pnodessize = 0
    	url='http://fc0:8000/fbs/vrf/pbinf.do?bd={"messageid":"a"}'
   	resp=session.get(url,timeout=10)
    	jsonData = resp.json()
    	murs = jsonData['murs']
    	size = len(murs)
    	outx = []
    	for mur in murs :
       		#node = bcuidmap[mur['bcuid']]['uri'][6:]
		node=mur['bcuid'][0:16]

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
    	print ">>>>>>>>>>>>>>    DNodes="  + str(size) +  " PNodes=" + str(pnodessize) +"  >>>>>>>>>" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    	print x
    except:
        #os.system('clear')
	print 'not ready'	
    time.sleep(1)
