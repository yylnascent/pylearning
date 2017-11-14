import matplotlib.pyplot as plt

__author__ = 'Chopin.Y'
__eamil__ = 'yylnascent@126.com'

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['c', 'm', 'r', 'b']
explode = (0, 0.1, 0, 1)

plt.pie(slices, 
        labels=activities, 
        colors=colors, 
        startangle=90, 
        shadow=True, 
        explode=(0, 0.1, 0, 0), 
        autopct='%1.1f%%')

# title
plt.title('Chopin.Y\' time distributed')

# perfact circle
plt.axis('equal')

plt.show()

