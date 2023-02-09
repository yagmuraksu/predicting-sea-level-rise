import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  year = np.array(df['Year'])
  csiro = np.array(df['CSIRO Adjusted Sea Level'])

  # Create scatter plot
  fig, ax = plt.subplots(1, 1, figsize=(15, 10))
  ax = plt.scatter(x=year, y=csiro)

  # Create first line of best fit
  slope, intercept, r, p, se = linregress(year, csiro)
  year_future = np.arange(year[0], 2051, 1)
  best_line = [slope * x + intercept for x in year_future]
  ax = plt.plot(year_future, best_line, 'r', label='first line of best fit')

  # Create second line of best fit
  year2 = np.array(df[df['Year'] >= 2000]['Year'])
  csiro2 = np.array(df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
  slope2, intercept2, r2, p2, se2 = linregress(year2, csiro2)
  year_future2 = np.arange(2000, 2051, 1)
  best_line2 = [slope2 * x + intercept2 for x in year_future2]
  ax = plt.plot(year_future2, best_line2, 'g', label='second line of best fit')

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
  plt.legend()

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
