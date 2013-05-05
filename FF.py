file_names = ["conv1.csv", "conv2.csv", "conv3.csv", "conv4.csv", "conv5.csv"] 

delimiter = " "
key = 0 
column = 0 

keys = set() 
tables = []

for name in file_names:
    file = open(name) 
    table={}
    for line in file:
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
