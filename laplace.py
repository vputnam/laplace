#laplace1

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
total1 = 0
for line in f:
    value1 = line.split(",")
    value1 = map(int, value1)
    count += value1.count(1)
    del value1[-1]
    D1.append(value1)
f.close()
total1= len(D1)*len(value1)
trueavg1 = float(count)/float(total1)

#take in D2
#data2 = raw_input('Enter the name of your second dataset: ')
f = file('smallpoker2.txt', 'r')
f = open('smallpoker2.txt', 'r')

D2 = []
value2 = []
for line in f:
    value2 = line.split(",")
    value2 = map(int, value2)
    count += value1.count(1)
    del value2[-1]
    D2.append(value2)
f.close()
total2= len(D2)*len(value2)
trueavg2 = float(count)/float(total1)




plt.xlabel('x')
plt.ylabel('pdf')
plt.title('Title')

mu, b = trueavg1, 1
f = np.random.laplace(mu, b, 100)

 

x1 = np.arange(-10, 10, .01)
pdf1 = np.exp(-abs(x1-mu)/b)/(2.*b)
plt.plot(x1, pdf1)


mu, b = trueavg2, 1
x2 = np.arange(-10, 10, .01)
pdf2 = np.exp(-abs(x2-mu)/b)/(2.*b)
plt.plot(x2, pdf2)

plt.show()