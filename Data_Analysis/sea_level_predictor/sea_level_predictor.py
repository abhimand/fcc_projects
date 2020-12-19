import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')
    # Create scatter plot
    ax = df.plot(x='Year',y='CSIRO Adjusted Sea Level', kind='scatter', label='original data', title='Rise in Sea Level')

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    x2 = list(range(1880, 2050))
    y2 = []
    for year in x2: 
        y2.append(intercept + slope*year)
    ax.plot(x2, y2, 'r', label='first fitted line')


    # Create second line of best fit
    x = df['Year'].tail(14)
    y = df['CSIRO Adjusted Sea Level'].tail(14)
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    x2 = list(range(2000, 2050))
    y2 = []
    for year in x2: 
        y2.append(intercept + slope*year)
    ax.plot(x2, y2, 'b', label='second fitted line')
    ax.legend()

    # Add labels and title
    plt.ylabel('Sea Level (inches)')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()