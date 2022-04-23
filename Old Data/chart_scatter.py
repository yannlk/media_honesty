import csv
import matplotlib as plt

f = open("/Users/yannkull/Library/Mobile_Documents/com~apple~CloudDocs/Documents/Projects/Programming/Media_Bias_Bot/bias_data2.csv")

x = []
y = []

for row in csv.reader(f):
    x.append(row[1])
    y.append(row[2])

plt.scatter(x, y)
plt.show()
