"""Missouri COVID-19 Analysis Script
"""

from datetime import date

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

from utils import plot_utils as pu
from utils import markdown_utils as mu


class RegionalAnalysis(object):
    def __init__(self, time_series_path, 
                 daily_reports_path, stat_area_path,
                 results_path):
        self.time_series_path_ = time_series_path
        self.daily_reports_path_ = daily_reports_path
        self.stat_area_path_ = stat_area_path
        self.results_path_ = results_path
        self.stat_area_map_ = pd.DataFrame()
        self.daily_reports_ = pd.DataFrame()
        self.time_series_deaths_ = pd.DataFrame()
        self.time_series_cases_ = pd.DataFrame()
        self.time_series_files_ = {
            'deaths': 'csse_covid_19_time_series/time_series_covid19_deaths_US.csv',
            'cases': 'csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
        }

    def _pull_stat_area_map(self):
        self.stat_area_map_ = pd.read_csv(self.stat_area_path_+'statistical_areas.csv')

    def _join_stat_areas(self, df):
        if self.stat_area_map_.empty:
            self._pull_stat_area_map()

        df = df.join(
            self.stat_area_map_.set_index(['Province_State', 'Admin2']),
            how='left', on=['Province_State', 'Admin2']
        )

        return df

    def _pull_time_series(self):
        for k in self.time_series_files_.keys():

            df = pd.read_csv(self.time_series_path_+self.time_series_files_[k])
            df = self._join_stat_areas(df)
            df = df[
                (df.Province_State == 'Missouri')|
                (df.MSA.notnull())
            ]
            df.loc[df.Admin2.isin(['Out of MO', 'Unassigned']), 'MSA'] = 'Unassigned/Out of MO'
            df.loc[
                (df.Province_State == 'Missouri')&
                (df.MSA.isnull()),
                'MSA'
            ] = 'Missouri non-MSA'
            attr = [x for x in dir(self) if k in x][0]
            self.__dict__[attr] = df

    def _pull_daily_report_data(self):

        pass


if __name__ == "__main__":
    print('===== Running MO COVID-19 Analysis Script =====')

    # set up object
    ra = RegionalAnalysis(
        time_series_path='../csse_covid_19_data/',
        daily_reports_path=None,
        stat_area_path='data/',
        results_path=''
    )

    print('\n=== Pulling Data ===')
    # pull data
    ra._pull_time_series()

    print('\n=== Plotting Daily Change Data ===')
    # plot running average of daily changes
    pu.plot_daily_data(ra.time_series_cases_,
                       save_loc='images/mo_daily_cases.png',
                       title='New Daily Confirmed Cases')
    pu.plot_daily_data(ra.time_series_deaths_,
                       save_loc='images/mo_daily_deaths.png',
                       title='New Daily Deaths')
    pu.plot_msa_breakdown_data(ra.time_series_cases_,
                               msa='St. Louis-Farmington',
                               save_loc='images/stl_daily_cases.png',
                               title='New Daily Confirmed Cases')
    pu.plot_msa_breakdown_data(ra.time_series_deaths_,
                               msa='St. Louis-Farmington',
                               save_loc='images/stl_daily_deaths.png',
                               title='New Daily Deaths')

    print('\n=== Updating Markdown ===')
    mu.write_markdown('missouri_analysis.md', ra)
