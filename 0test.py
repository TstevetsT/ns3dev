#! /usr/bin/env python
# This script is for parsing the output from an ns-3 simulation trace file and calculating 
# delivery ratio, dropped ratio, delay, hopct, and more.  the node number for source and sink
# USAGE  ./0proc.py <inputfilename>
# The nodes MUST be all have a unique last octet (Limited to 253 nodes)
# ToDo
# -  Make code work for all IP address (not dependent on unique last octet)
import sys
import datetime
now=str(datetime.datetime.now())+"\n"
print(now)
