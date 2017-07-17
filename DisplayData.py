import matplotlib
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def graph():
    with open("monte-carlo-liberal.csv") as montecarlo:
        data = csv.reader(montecarlo, delimiter=',') # Easily read contents from csv file (We could have used Pandas

        for line in data:
            percentROI = float(line[0])
            wager_size_percent = float(line[1])
            wager_count = float(line[2])
            p_color = line[3]

            ax.scatter(wager_size_percent, wager_count, percentROI, color=p_color) # Graph 3D
            ax.set_xlabel('wager percent size')
            ax.set_ylabel('wager count')
            ax.set_zlabel('Percent ROI')

    plt.show()

graph()