from datetime import date
import numpy as np
import pandas as pd


def _msa_table(md, deaths, cases):
    # msa table
    start = [x for x in md if 'msa_table start' in x][0]
    start = md.index(start)
    end = [x for x in md if 'msa_table end' in x][0]
    end = md.index(end)

    # write new file
    table = []
    cases = cases.groupby('MSA').sum()
    deaths = deaths.groupby('MSA').sum()
    idx = cases.diff(axis=1).rolling(window=7, axis=1).mean()
    idx = idx.sort_values(by=cases.columns[-1], ascending=False).index

    for ind in [x for x in idx if 'Unassigned' not in x]:
        line = '| {} |'.format(ind)
        line += ' %i |'%deaths.loc[ind].values[-1]
        line += ' %i |'%cases.loc[ind].values[-1]
        line += ' %i |'%cases.loc[ind].diff().rolling(window=7).mean().values[-1]
        line += ' %i |'%cases.loc[ind].diff().rolling(window=14).mean().values[-1]
        line += ' %i |'%cases.loc[ind].diff().rolling(window=30).mean().values[-1]
        table.append(line)
    
    # insert new table
    new_md = md[:start+3]+table+md[end:]

    return new_md

def _county_table(md, deaths, cases):
    # county table
    start = [x for x in md if 'county_table start' in x][0]
    start = md.index(start)
    end = [x for x in md if 'county_table end' in x][0]
    end = md.index(end)

    # write new file
    table = []
    idx = cases.diff(axis=1).rolling(window=7, axis=1).mean()
    idx = idx.sort_values(by=cases.columns[-1], ascending=False).index
    for ind in idx:
        line = '| {} | {} | {} |'.format(
            ind[2], ind[0], ind[1]
        )
        line += ' %i |'%deaths.loc[ind].values[-1]
        line += ' %i |'%cases.loc[ind].values[-1]
        line += ' %i |'%cases.loc[ind].diff().rolling(window=7).mean().values[-1]
        line += ' %i |'%cases.loc[ind].diff().rolling(window=14).mean().values[-1]
        line += ' %i |'%cases.loc[ind].diff().rolling(window=30).mean().values[-1]
        table.append(line)
    
    # insert new table
    new_md = md[:start+3]+table+md[end:]

    return new_md


def write_markdown(filename, ra):
    """Writing markdown file
    """
    with open(filename) as f:
        md = f.read()
    md = md.split('\n')

    # update date
    update = [x for x in md if 'Updated:' in x][0]
    ind = md.index(update)
    md[ind] = 'Updated: %s  '%(date.today().strftime("%m/%d/%Y"))

    # grabbing/modifying tables
    index_cols = ['Province_State', 'Admin2', 'MSA']
    deaths = ra.time_series_deaths_.set_index(index_cols)
    cases = ra.time_series_cases_.set_index(index_cols)
    cases = cases.loc[deaths.index]
    assert all(deaths.index == cases.index),\
          'Mismatch in index for deaths and cases'
    deaths = deaths[deaths.columns[
        deaths.columns.str.contains('/20')
    ]]
    cases = cases[cases.columns[
        cases.columns.str.contains('/20')
    ]]

    # writing msa table
    new_md = _msa_table(md, deaths, cases)

    # writing county table
    new_md = _county_table(new_md, deaths, cases)

    # writing final markdown string
    final_md = ''
    for line in new_md:
        final_md += line+'\n'

    f = open(filename, 'w')
    f.write(final_md[:-1])
    f.close()
