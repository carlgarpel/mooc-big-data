import sys

total = 0
oldKey = ''

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        print ("Error en los datos")
        continue

    thisKey, thisAd = data_mapped

    if oldKey and oldKey != thisKey:
        print ("{0}\t{1}".format(oldKey, total))
        oldKey = thisKey
        total=0

    oldKey = thisKey
    total += 1

if oldKey != '':
    print ("{0}\t{1}".format(oldKey, total))
