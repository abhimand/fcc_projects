import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
# df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
# df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
# df.loc[df['gluc'] == 1, 'gluc'] = 0
# df.loc[df['gluc'] > 1, 'gluc'] = 1
# or 
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    #### Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, value_vars=[ 'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'], id_vars=['cardio'],)
    print(df_cat)

    ### Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    # df_cat = df_cat.groupby(['cardio','variable', 'value'], as_index = False).size().rename(columns={'value': 'total'})  
    # NO NEED TO DO THIS PART, SEABORN TAKES CARE OF IT

    ### Draw the catplot with 'sns.catplot()'
    g = sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio')
    # for some reason in the docs, they never mentioned to set our y label BUT only in the test case it was shown 
    g.set_ylabels('total', fontsize=15) # 
    fig = g.fig

    ### Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    ### Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    ### Calculate the correlation matrix
    corr = sns.heatmap(df_heat.corr())

    ### Generate a mask for the upper triangle
    mask = np.triu(df_heat.corr())

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    # i got the mask, corr down but had to search up to format the triangular plot!
    ax = sns.heatmap(df_heat.corr() ,linewidths=.5,annot=True,fmt='.1f',mask=mask,square=True,center=0,vmin=-0.1,vmax=0.25,cbar_kws={'shrink': .45,'format': '%.2f'})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
