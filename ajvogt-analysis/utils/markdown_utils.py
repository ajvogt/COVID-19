from datetime import date
import numpy as np
import pandas as pd


def _county_table(md, deaths, cases):
    # msa table
    header = '## Metropolitan Statistical Area (MSA) Counties'
    start = [x for x in md if header in x][0]
    ind = md.index(start)
    md = md[:ind+3]            

    # write new file
    new_md = ''
    for line in md:
        new_md += line +'\n'

    for ind in deaths.index:
        line = '| {} | {} | {} |'.format(
            ind[2], ind[0], ind[1]
        )
        line += ' %i |'%cases.loc[ind].values[-1]
        line += ' %i |'%deaths.loc[ind].values[-1]
        new_md += line +'\n'

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

    # writing county table
    new_md = _county_table(md, deaths, cases)

    f = open(filename, 'w')
    f.write(new_md)
    f.close()
