#laplcehist.py

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import laplace

#take in D1
#data1 = raw_input('Enter the name of your first dataset: ')
f = file('smallpoker1.txt', 'r')
f = open('smallpoker1.txt', 'r')

D1 = []
value1 = []
count = 0
total = 0
for line in f:
    value1 = line.split(",")
    value1 = map(int, value1)
    count += value1.count(1)
    del value1[-1]
    D1.append(value1)
f.close()
total= len(D1)*len(value1)
trueavg1 = float(count)/float(total)
 

#take in D2
#data2 = raw_input('Enter the name of your second dataset: ')
f = file('smallpoker2.txt', 'r')
f = open('smallpoker2.txt', 'r')

D2 = []
value2 = []
count = 0
total = 0
for line in f:
    value2 = line.split(",")
    value2 = map(int, value2)
    count += value1.count(1)
    del value2[-1]
    D2.append(value2)
f.close()
total= len(D2)*len(value2)
trueavg2 = float(count)/float(total)

mu, b = trueavg1, 1
average1 = np.random.laplace(mu, b, 1000)

mu, b = trueavg2, 1
average2 = np.random.laplace(mu, b, 1000)

x1 = np.arange(-1, 1, .01)
pdf1 = np.exp(-abs(x1-mu)/b)/(2.*b)
plt.hist(average1, bins=100)
plt.hist(average2, bins=100)

plt.xlabel('x')
plt.ylabel('pdf')
plt.title('Title')

plt.show()
