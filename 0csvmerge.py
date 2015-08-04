#! /usr/bin/env python
# This script is for parsing the output from an ns-3 simulation trace file and calculating 
# delivery ratio, dropped ratio, delay, hopct, and more.  the node number for source and sink
# USAGE  ./0csvmerge.py <inputfilename> <inputcolumns> <outputfilename>
# The nodes MUST be all have a unique last octet (Limited to 253 nodes)
# ToDo
# -  Make code work for all IP address (not dependent on unique last octet)
import sys
import csv
temp=" "
newline=[]
newlist=[]
with open(sys.argv[1]) as f:
	lines =  f.read().splitlines() 
for line in lines:	
	temp=line.split(' ')[0]
	temp=temp.split(',')[0]
	temp2=line.split(' ')[2]
	temp2=temp2.split(',')[0]
	newline.append(temp+temp2)
	newline.append(int(((line.split(' ')[1])).split(',')[0]))
	newline.append(float(((line.split(' ')[3])).split(',')[0]))
	newline.append(float(((line.split(' ')[4])).split(',')[0]))
	newline.append(float(((line.split(' ')[5])).split(',')[0]))
	newlist.append(newline)
	newline=[]
with open(sys.argv[2], 'wb') as csvfile:
	writer=csv.writer(csvfile)
	writer.writerows(newlist)

#Proto, nodePauseTime, nFlows, Average hops/flow, Average delay (ms), Average PDR
