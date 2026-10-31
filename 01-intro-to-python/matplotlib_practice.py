"""Intro to Python (DataCamp) - Matplotlib practice.

Covers: line plot, scatter plot, histogram, and customization
(labels, title, ticks, adding more data).
"""
import matplotlib
matplotlib.use("Agg")  # save to files instead of opening a window
import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

# Line plot
plt.plot(year, pop)
plt.savefig("line_plot.png")
plt.clf()

# Scatter plot
plt.scatter(year, pop)
plt.savefig("scatter_plot.png")
plt.clf()

# Histogram (help(plt.hist) shows the arguments)
values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.hist(values, bins=3)
plt.savefig("histogram.png")
plt.clf()

# Customization: labels, title, ticks, extra historical data
year = [1800, 1850, 1900] + year
pop = [1.0, 1.262, 1.650] + pop

plt.plot(year, pop)
plt.xlabel("Year")
plt.ylabel("Population (billions)")
plt.title("World Population Projections")
plt.yticks([0, 2, 4, 6, 8, 10], ["0", "2B", "4B", "6B", "8B", "10B"])
plt.savefig("population.png")
print("Saved line_plot.png, scatter_plot.png, histogram.png, population.png")
