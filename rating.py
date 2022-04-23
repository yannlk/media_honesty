import csv

f = open("r_scores.csv", 'r', encoding="utf-8-sig")

data = []
for row in csv.reader(f):
    data.append(row)


def bias_score(num):
    line = 0
    while line + 1 < len(data):
        if float(data[line + 1][0]) > num >= float(data[line][0]):
            return data[line][1]
        line += 1


def reliability_score(num):
    line = 0  # iterator
    while line < len(data):
        if float(data[line + 1][2]) > num >= float(data[line][2]):
            return data[line][3]
        line += 1

