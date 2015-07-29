#! /usr/bin/env python
# This script is for parsing the output from an ns-3 simulation trace file and calculating 
# delivery ratio, dropped ratio, delay, hopct, and more.  the node number for source and sink
# USAGE  ./0proc.py <inputfilename>
# The nodes MUST be all have a unique last octet (Limited to 253 nodes)
# ToDo
# -  Make code work for all IP address (not dependent on unique last octet)
import sys
with open(sys.argv[1]) as f:
	lines =  f.read().splitlines() 
#Initialize Variables
txrx=0
time=1
node=2
seq=28
ttl=26
srcip=38
dstip=40
pric=[]
allx=[]
tx=[]
rx=[]
alltx=[]
temp="  "

# AODV   cat AODV.tr |grep -v RREP |grep -v RERR|grep Udp|cut -d" " -f1-3,27,29,39,41|cut -d"/" -f1,3,9|tr ")" " "|tr "/" " "|tr -s " "|cut -d" " -f1-3,5-8


# SIFT and DGGF
# For block will parse data to extract required data fields
# Outputs:
# 	tx-a parsed list of all source transmitted traces
#       rx-a parsed list of all destination received traces
#       allx-a parsed list of all traces
# it will be in the following form:
# ['<txrx>', <time>, <processing node#>, <seq#>, <ttl>, <srclastoct>, <dstlastoct>] 
#      0       1              2             3      4           5            6



for line in lines:
	if 'Udp' in line and not 'RREP' in line and not 'RERR' in line:  
		pric.append(line.split(' ')[txrx])
        	pric.append(float(line.split(' ')[time]))
        	temp=line.split(' ')[node]
        	pric.append(int(temp.split('/')[2]))
        	pric.append(int(line.split(' ')[seq]))
        	pric.append(int(line.split(' ')[ttl]))
        	temp=line.split(' ')[srcip]
        	pric.append((int(temp.split('.')[3])-1))
        	temp=line.split(' ')[dstip]
        	temp=(temp.split('.')[3])
		pric.append((int(temp.split(')')[0])-1))
        	allx.append(pric)
       	 	if pric[txrx] == 't':               # If packet is transmitted type and
			alltx.append(pric)
			if pric[node] == pric[5]:   #    if processing node == source node
				tx.append(pric)     #    then save as source trace
        	elif pric[txrx] == 'r': 	    # If trace type is recieved  AND
			if pric[node] == pric[6]:   # 	 if processing node == destination node
                		rx.append(pric)     # 	 then save as destination trace
        	pric=[]
seq=3
ttl=4
totalsimulationpacketsprocessed=len(allx)
# This includes all packet in the simulation so network congestion can be calculated
ntxpackets=len(tx)
j=0
tempj=[]
temptx=[]
# This is to ignore retransmission of dropped packets
temptx=sorted(tx, key=lambda x: x[3])
tx=sorted(temptx, key=lambda x: x[2])
temptx=[]
for j in range(0, ntxpackets-1):
	if tx[j][2]==tx[j+1][2]:
		if tx[j][3]!=tx[j+1][3]:
			temptx.append(tx[j])
	else:	
		temptx.append(tx[j])
temptx.append(tx[j+1])
tx=temptx
ntxpackets=len(tx)
print "Total # of packets processed=%d  Total Tx=%d   Packets Sent=%d.\n" %(totalsimulationpacketsprocessed, len(alltx), ntxpackets)
nrxpackets=len(rx)
temprx=[]
temptx=[]
dropped=1
wttl=0
packetsdropped=0
packetsdelivered=0
i=0
#with open(sys.argv[1], "a") as myfile:
#	myfile.write("[Average hops/flow, Average delay (ms), # delivered, delivered #rate, # dropped, dropped rate, BW efficiency]")
for j in range(0, ntxpackets):
	for i in range(0, nrxpackets):
		if rx[i][seq]==tx[j][seq]:
                	if rx[i][6]==tx[j][6]:
		                # print "RxSeq=%d TxSeq=%d RxIP=%d TxIP=%d" %(rx[i][seq],tx[j][seq],rx[i][6],tx[j][6])
				dropped=0
				temprx.append(rx[i])
				temptx.append(tx[j])
				packetsdelivered+=1
				break
j=0
delay=[]
hops=[]
for j in range(0, packetsdelivered):
	delay.append(temprx[j][time]-temptx[j][time])
	hops.append(1+temptx[j][ttl]-temprx[j][ttl])
averagedelay=sum(delay)/float(len(delay))
averagehops=float(sum(hops))/float(len(hops))
averagedelay=averagedelay*1000   # Converts delay to milliseconds
packetsdropped=ntxpackets-packetsdelivered
pacdeliveryrate=float(packetsdelivered)/float(ntxpackets)
pacdroprate=1-pacdeliveryrate
bandwidthefficiency=(float(sum(hops))+float(ntxpackets))/float(len(alltx))
#print "Total hops=%d bandwidthefficiency=(float(sum(hops))+float(Initial Tx))/float(len(Total Tx)) \n" %float(sum(hops))		
#print("[Average hops/flow, Average delay (ms), # delivered, delivered rate, # dropped, dropped rate, BW efficiency]")
output=[] 
output.append(averagehops)
output.append(averagedelay)
output.append(packetsdelivered)
output.append(pacdeliveryrate)
output.append(packetsdropped)
output.append(pacdroprate)
output.append(bandwidthefficiency)
# Change Formatting from python list to csv
temp=str(output)
output=temp.replace("[", "")
temp=output.replace("]", "\n")
print(temp)
with open(sys.argv[2], "a") as myfile:
	myfile.write(temp)

