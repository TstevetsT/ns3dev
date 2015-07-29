#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sys
with open(sys.argv[1]) as f:
	lines =  f.read().splitlines() 
#/*
#headers=lines[0]
#i=0
column=[]
#while i <=headers.count(','):
#	column.append(headers.split(', ')[i])
#	i+=1
#
i=0
data=[]
for line in lines:
	while i <=line[0].count(','): 
		column.append(line.split(', ')[i])
		i+=1
	data.append(column)
print(data)
