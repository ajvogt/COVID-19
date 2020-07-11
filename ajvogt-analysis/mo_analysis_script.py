"""Missouri COVID-19 Analysis Script
"""

from datetime import date

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

DEFAULTS = {
    'deaths': {
        'filename': 'time_series_covid19_deaths_US.csv',
        'ylabel': 'New Daily Deaths'
    },
    'cases': {
        'filename': 'time_series_covid19_confirmed_US.csv',
        'ylabel': 'New Daily Confirmed Cases'
    }
}

class RegionalAnalysis(Object):
    def __init__(self, data_path, stat_area_path):
        self.data_path = data_path
        self.stat_area_path = stat_area_path
        self.stat_area_map = pd.DataFrame()
        self.stat_area_data = pd.DataFrame()
        self.state_data = pd.DataFrame()
        self.county_data = pd.DataFrame()

    def _pull_stat_area_map(self):
        return pd.read_csv(self.stat_area_path+'statistical_areas.csv')

    def _pull_state_data(self):

        df = pd.read_csv(self.data_path+'csse_covid_19_time_series.csv')
        df = df[df.Province_State == 'Missouri']

        return df

    def _pull_county_data(self):

        pass
    
    def pull_all_data(self):

        self.stat_area_map = self._pull_stat_area_map()
        self.state_data = self._pull_state_data()
        self.county_data = self._pull_county_data()
        self.stat_area_data = self._compile_stat_area_data()


def plot_daily_info(path, msa, data='deaths'):
    

    df = pd.read_csv(path+DEFAULTS[data]['filename'])
    cols = df.columns[df.columns.str.contains('/20')]
    xlabels = df.loc[:, cols].columns
    xticks = np.arange(0, xlabels.shape[0], 1)
    plt.figure(figsize=(10, 5))

    # Missouri
    cond = "(Province_State == 'Missouri')"
    y = df.query(cond).loc[:, cols].sum(axis=0).diff().rolling(window=7).mean()
    latest_total = df.query(cond).loc[:, cols].sum(axis=0)
    plt.plot(xticks, y, label='Missouri: %i'%latest_total[-1])

    cond = "(Province_State == 'Missouri')&"
    for row in msa.Admin2.values:
        cond += "(Admin2 != '%s')&"%row
    cond = cond[:-1]
    y = df.query(cond).loc[:, cols].sum(axis=0).diff().rolling(window=7).mean()
    latest_total = df.query(cond).loc[:, cols].sum(axis=0)
    plt.plot(xticks, y, label='Missouri non-MSA: %i'%latest_total[-1],
             color='C0', linestyle='--')

    # MSAs
    for area in msa.MSA.unique():
        cond = ""
        for row in msa[msa.MSA == area].values:
            cond += "((Province_State == '%s')&(Admin2 == '%s'))|"\
                    %(row[1], row[2])
        cond = cond[:-1]

        y = df.query(cond).loc[:, cols].sum(axis=0).diff().rolling(window=7).mean()
        latest_total = df.query(cond).loc[:, cols].sum(axis=0)
        plt.plot(xticks, y, label='%s: %i'%(area, latest_total[-1]))

    # St. Louis City + County
    cond = "((Province_State == 'Missouri')&(Admin2 == 'St. Louis'))|"
    cond += "((Province_State == 'Missouri')&(Admin2 == 'St. Louis City'))"
    y = df.query(cond).loc[:, cols].sum(axis=0).diff().rolling(window=7).mean()
    latest_total = df.query(cond).loc[:, cols].sum(axis=0)
    plt.plot(xticks, y, label='St. Louis City + County: %i'%latest_total[-1],
            linestyle='--', color='C1')

    steps = np.arange(0, xticks.shape[0], 7)
    plt.xticks(xticks[steps], xlabels[steps], rotation=90)
    plt.ylabel('%s\n(7-day Moving Average)'%DEFAULTS[data]['ylabel'])
    plt.title('Missouri Metropolitan Statistical Areas')
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.savefig('images/mo_daily_%s.png'%data)

    plt.show()

def write_markdown(filename, msa):
    """Writing markdown file
    """
    with open(filename) as f:
        md = f.read()
    md = md.split('\n')

    # update date
    update = [x for x in md if 'Updated:' in x][0]
    ind = md.index(update)
    md[ind] = 'Updated: %s  '%(date.today().strftime("%m/%d/%Y"))
    
    # msa table
    start = [x for x in md if '|-' in x][0]
    ind = md.index(start)
    md = md[:ind+1]            

    # write new file
    new_md = ''
    for line in md:
        new_md += line +'\n'
    
    # including county info
    deaths = pd.read_csv(path+DEFAULTS['deaths']['filename'])
    cases = pd.read_csv(path+DEFAULTS['cases']['filename'])
    deaths_cols = deaths.columns[deaths.columns.str.contains('/20')]
    cases_cols = cases.columns[cases.columns.str.contains('/20')]

    for row in msa.values:
        line = '|'
        for i in row:
            line += ' %s |'%i
        
        cond = "((Province_State == '%s')&(Admin2 == '%s'))"%(row[1], row[2])
        vals_cases = cases.query(cond)[cases_cols].values[0]
        line += ' %i |'%vals_cases[-1]
        vals_deaths = deaths.query(cond)[deaths_cols].values[0]
        line += ' %i |'%vals_deaths[-1]
        new_md += line +'\n'
    
    cond = (cases.Province_State == 'Missouri')&\
           (~cases.Admin2.isin(msa.Admin2))&\
           (~cases.Admin2.isin(['Out of MO', 'Unassigned']))
    for row in cases[cond].Admin2.values:
        line = '| Missouri non-MSA | Missouri | %s | '%row
        cond = "((Province_State == 'Missouri')&(Admin2 == '%s'))"%row
        vals_cases = cases.query(cond)[cases_cols].values[0]
        line += ' %i |'%vals_cases[-1]
        vals_deaths = deaths.query(cond)[deaths_cols].values[0]
        line += ' %i |'%vals_deaths[-1]
        new_md += line +'\n'

    f = open(filename, 'w')
    f.write(new_md)
    f.close()


if __name__ == "__main__":
    print('===== Running MO COVID-19 Analysis Script =====')
    path = '../csse_covid_19_data/csse_covid_19_time_series/'

    print('=== Reading MSA Data ===')
    msa = pd.read_csv('data/statistical_areas.csv')

    print('=== Pulling and plotting Deaths Data ===')
    plot_daily_info(path=path,
                    msa=msa,
                    data='deaths')
    
    print('=== Pulling and plotting Cases Data ===')
    plot_daily_info(path=path,
                    msa=msa,
                    data='cases')

    print('=== Updating Markdown ===')
    write_markdown('missouri_analysis.md', msa)
