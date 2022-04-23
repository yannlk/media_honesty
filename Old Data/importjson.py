import json
import csv
from urllib.parse import urlparse

with open("jsonformatter.txt") as f:
    data = json.load(f)

sources = {}
for line in data:
    if line["main_url"] not in sources:
        sources[line["main_url"]] = [line["moniker_name"]]

calculate = {}
for line in data:
    if line["main_url"] not in calculate:
        calculate[line["main_url"]] = [[line["bias"]], [line["reliability"]]]
    else:
        calculate[line["main_url"]][0].append(line["bias"])
        calculate[line["main_url"]][1].append(line["reliability"])

for id in calculate:
    bias = sum(calculate[id][0])/len(calculate[id][0])
    reliability = sum(calculate[id][1]) / len(calculate[id][1])
    sources[id].append(bias)
    sources[id].append(reliability)

with open('bias_data.csv', 'w') as f:
    for key in sources.keys():
        f.write("%s,%s\n" % (key, sources[key]))

with open('bias_data2.csv', 'w') as f:
    for key in sources.keys():
        new_key = urlparse(key).netloc
        f.write("\n" + new_key + "," + (str(sources[key][0]) + "," + str(sources[key][1]) + "," + str(sources[key][2])))