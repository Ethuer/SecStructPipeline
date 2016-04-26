import csv

from pylab import *


counter = 0
count_s = 0

with open('results/subset_HE605206','r') as in_raw:
    infile = csv.reader(in_raw, delimiter = '\t')


    for row in infile:
        counter +=1
        if 'NA' not in row[2] and float(row[2]) < 0.05:
            count_s +=1

    print counter
    print count_s




n = 12
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x,y in zip(X,Y1):
    text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

ylim(-1.25,+1.25)
show()
