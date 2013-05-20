#!/usr/bin/python2.7

from sys import argv

file_names = []
for i in range(1, len(argv)):
    file_names.append(argv[i]) 

delimiter = " "
key = 0 
column = 0 

keys = set() 
tables = []

for name in file_names:
    file = open(name) 
    table={}
    for line in file:
        line = line.strip()
        data = line.split(delimiter) 
        table[data[key]] = []
        keys.add(data[key])
        for i in range(1,len(data)):
            table[data[key]].append(data[i])
    tables.append(table)

for element in keys:
    print element, 
    for table in tables:
        if(element in table):
            print table[element][column],
    print
