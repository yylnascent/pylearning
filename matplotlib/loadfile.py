import matplotlib.pyplot as plt
import numpy as np
import csv

__author__ = 'Chopin.Y'
__eamil__ = 'yylnascent@126.com'

x = []
y = []

# csv reader
data_file = "example.data"

with open(data_file, 'r') as csv_fp:
    plots = csv.reader(csv_fp, delimiter=',')
    for point in plots:
        x.append(point[0])
        y.append(point[1])

# numpy loadtxt
x, y = np.loadtxt(data_file, delimiter=',', unpack=True)

plt.plot(x, y, label='Loaded data from file')

# set axis label
plt.xlabel('x')
plt.ylabel('y')

plt.title('Chopin.Y\'s daily')

# show legend()
plt.legend()

plt.show()

