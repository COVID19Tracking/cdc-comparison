import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from .munge import palette


def state_level_metric_diff(df:pd.DataFrame, left_metric_col:str, right_metric_col:str, 
                            log:bool=False, plot_title:str=None) -> None:
    """Compare how similar reported states numbers. Requires 1 column to be 'state' and the other 2 to be metric_cols."""
    
    sns.set_context("notebook", font_scale=1.2)
    sns.set_style("whitegrid")
    
    plt.figure(figsize=(9,20))
    df = df.sort_values(left_metric_col, ascending=True)

    if log:
        df[left_metric_col] = np.log10(df[left_metric_col])
        df[right_metric_col] = np.log10(df[right_metric_col])
        
    i_range = range(1, df.shape[0]+1)
    plt.hlines(
        y=i_range, 
        xmin=df[[left_metric_col, right_metric_col]].min(axis=1), 
        xmax=df[[left_metric_col, right_metric_col]].max(axis=1), 
        color='black', alpha=0.4)
    plt.scatter(df[left_metric_col], i_range, alpha=.6, color=palette["fox"], label=left_metric_col)
    plt.scatter(df[right_metric_col], i_range, alpha=.8, color=palette["grey"], label=right_metric_col)
    plt.legend()

    # Add title and axis names
    plt.yticks(i_range, df['state'])
    plt.title(plot_title)

    plt.ylabel('State')
    sns.despine(left=True)
    if log:
        plt.legend(bbox_to_anchor=(.45, .95))
        plt.xlabel('log')
        
    plt.show()