import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

DEFAULTS = {
    'Missouri': 'k',
    'St. Louis-Farmington': 'C1',
    'Cape Girardeau-Sikeston': 'C2',
    'Springfield': 'C3',
    'Joplin': 'C4',
    'Columbia-Jefferson City': 'C5',
    'Kansas City': 'C0',
    'St. Joseph': 'tab:pink',
    'Missouri non-MSA': 'k'
}

def plot_daily_data(df, save_loc=None,
                    title='New Daily Confirmed Cases'):
    # Figure Info
    plt.figure(figsize=(10, 5))

    # X-axis
    cols = df.columns[df.columns.str.contains('/20')]
    xlabels = df.loc[:, cols].columns
    xticks = np.arange(0, xlabels.shape[0], 1)
    steps = np.arange(0, xticks.shape[0], 7)

    # Missouri
    cond = "(Province_State == 'Missouri')"
    y = df.query(cond).loc[:, cols].sum(axis=0).diff().rolling(window=7).mean()
    latest_total = df.query(cond).loc[:, cols].sum(axis=0)
    plt.plot(xticks, y, label='Missouri', color='k')

    # MSAs
    for area in [x for x in df.MSA.unique() if 'Unassigned' not in x]:
        cond = "(MSA == '%s')"%area
        y = df.query(cond).loc[:, cols].sum(axis=0).diff().rolling(window=7).mean()
        latest_total = df.query(cond).loc[:, cols].sum(axis=0)
        if area == 'Missouri non-MSA':
            linestyle = '--'
        else:
            linestyle = '-'
        plt.plot(xticks, y, label='%s'%area,
                 linestyle=linestyle, 
                 color=DEFAULTS[area])

    # Titles, Legends, & Labels
    plt.xticks(xticks[steps], xlabels[steps], rotation=90)
    plt.ylabel(title+'\n(7-day Moving Average)')
    plt.title('Missouri Metropolitan Statistical Areas')
    plt.legend(loc='upper left')
    plt.tight_layout()
    if save_loc is not None:
        plt.savefig(save_loc)
    plt.show()
