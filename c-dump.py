import json
import glob

megalist = []

for filename in glob.glob('*.c'):
    f = open(filename, 'r')
    for line in f:
        megalist.append(line)
    f.close()

json.dump(megalist, fp=open('singleStringArr.json', 'w'), indent=4)
