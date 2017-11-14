import matplotlib.pyplot as plt

__author__ = 'Chopin.Y'
__eamil__ = 'yylnascent@126.com'

days = [1, 2, 3, 4, 5] 

sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])
plt.plot([], [], label='Sleeping', color='m', linewidth=5)
plt.plot([], [], label='Eating', color='c', linewidth=5)
plt.plot([], [], label='Working', color='r', linewidth=5)
plt.plot([], [], label='Playing', color='k', linewidth=5)

# set axis label
plt.xlabel('x')
plt.ylabel('y')

plt.title('Chopin.Y\'s daily')

# show legend()
plt.legend()

plt.show()

