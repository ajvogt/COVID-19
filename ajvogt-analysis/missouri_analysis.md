# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/21/2021  
Source: [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)  
Source Code: `/ajvogt-analysis/mo_analysis_script.py`  
[Release Notes found below](#release-notes)

This analysis shows the Johns Hopkins University COVID-19 data broken down by 
[Metropolitan Statistcal Area](https://en.wikipedia.org/wiki/Metropolitan_statistical_area) (MSA)
 combinations within the state of Missouri. The list of counties in each MSA comibination can be found in the 
[table](#msa-counties) 
below. The [detailed map of MSAs](https://www2.census.gov/geo/maps/metroarea/us_wall/Sep2018/CBSA_WallMap_Sep2018.pdf) 
can be found here.  The clusters used in the charts and tables below 
are a custom combination of MSAs and 
[Combined Statistical Areas](https://en.wikipedia.org/wiki/Combined_statistical_area) (CSA). 
County populations are pulled from this 
[JHU CSSE repository file](https://github.com/ajvogt/COVID-19/blob/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv).

## Missouri New Daily Confirmed Cases by Metropolitan Statistcal Areas
![](images/mo_daily_cases.png)

## Missouri New Daily Deaths by Metropolitan Statistcal Areas
![](images/mo_daily_deaths.png)

## Missouri Cumulative Deaths by Metropolitan Statistcal Areas
![](images/mo_cumulative_deaths.png)

## Missouri Metropolitan Statistical Area Totals
<!-- msa_table start -->
| MSA | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|
| Kansas City | 2427 | 174260 | 454 | 405 | 544 |
| St. Louis-Farmington | 4471 | 253696 | 391 | 463 | 680 |
| Missouri non-MSA | 1965 | 109253 | 100 | 118 | 194 |
| Springfield | 592 | 35958 | 34 | 51 | 79 |
| Columbia-Jefferson City | 304 | 34275 | 30 | 35 | 61 |
| Joplin | 278 | 16166 | 15 | 21 | 37 |
| Cape Girardeau-Sikeston | 207 | 12772 | 13 | 15 | 22 |
| St. Joseph | 192 | 10047 | 8 | 8 | 17 |
<!-- msa_table end -->

## STL-Farmington MSA New Daily Confirmed Cases by County
![](images/stl_daily_cases.png)

## STL-Farmington MSA New Daily Deaths by County
![](images/stl_daily_deaths.png)

## STL-Farmington MSA Cumulative Deaths by County
![](images/stl_cumulative_deaths.png)

<a name="msa-counties"></a>
## Metropolitan Statistical Area (MSA) Counties
<!-- county_table start -->
| MSA | State | County | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|---|---|
| Kansas City | Kansas | Johnson | 733 | 53652 | 254 | 195 | 220 |
| St. Louis-Farmington | Missouri | St. Louis | 1917 | 87345 | 138 | 163 | 249 |
| Kansas City | Missouri | Jackson | 370 | 29845 | 55 | 62 | 93 |
| St. Louis-Farmington | Illinois | Madison | 449 | 27616 | 49 | 60 | 93 |
| St. Louis-Farmington | Illinois | St. Clair | 462 | 25063 | 48 | 57 | 81 |
| Kansas City | Kansas | Wyandotte | 264 | 18935 | 40 | 37 | 45 |
| St. Louis-Farmington | Missouri | St. Charles | 405 | 32668 | 40 | 54 | 66 |
| Kansas City | Missouri | Kansas City | 496 | 36524 | 38 | 40 | 79 |
| St. Louis-Farmington | Missouri | St. Louis City | 412 | 21208 | 37 | 38 | 48 |
| Springfield | Missouri | Greene | 416 | 23197 | 24 | 36 | 53 |
| St. Louis-Farmington | Missouri | Jefferson | 204 | 18851 | 20 | 23 | 42 |
| Kansas City | Kansas | Leavenworth | 76 | 6680 | 17 | 21 | 27 |
| Columbia-Jefferson City | Missouri | Boone | 77 | 15810 | 15 | 18 | 32 |
| Kansas City | Missouri | Clay | 143 | 7807 | 12 | 11 | 20 |
| St. Louis-Farmington | Missouri | Franklin | 153 | 8348 | 12 | 13 | 19 |
| Joplin | Missouri | Jasper | 214 | 12109 | 11 | 16 | 30 |
| Kansas City | Missouri | Cass | 84 | 7162 | 10 | 12 | 20 |
| Missouri non-MSA | Missouri | Butler | 33 | 3419 | 9 | 9 | 9 |
| St. Louis-Farmington | Missouri | Lincoln | 32 | 4264 | 8 | 8 | 10 |
| St. Louis-Farmington | Illinois | Monroe | 80 | 4022 | 7 | 8 | 13 |
| St. Louis-Farmington | Missouri | St. Francois | 102 | 7549 | 7 | 7 | 10 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 114 | 7485 | 6 | 8 | 14 |
| St. Louis-Farmington | Illinois | Macoupin | 78 | 4312 | 6 | 7 | 13 |
| Springfield | Missouri | Christian | 75 | 6820 | 6 | 8 | 15 |
| Columbia-Jefferson City | Missouri | Callaway | 43 | 4451 | 6 | 6 | 9 |
| Missouri non-MSA | Missouri | Johnson | 43 | 3840 | 6 | 7 | 8 |
| Kansas City | Missouri | Ray | 23 | 1498 | 6 | 4 | 5 |
| Kansas City | Kansas | Miami | 39 | 2592 | 5 | 5 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 73 | 3794 | 5 | 5 | 6 |
| St. Joseph | Missouri | Buchanan | 129 | 6923 | 5 | 5 | 11 |
| Columbia-Jefferson City | Missouri | Cole | 114 | 8549 | 5 | 6 | 11 |
| Missouri non-MSA | Missouri | Phelps | 121 | 2983 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Taney | 82 | 4542 | 4 | 5 | 9 |
| Kansas City | Missouri | Platte | 42 | 3068 | 4 | 5 | 8 |
| Joplin | Missouri | Newton | 64 | 4057 | 3 | 5 | 7 |
| St. Louis-Farmington | Illinois | Jersey | 45 | 2473 | 3 | 4 | 7 |
| Kansas City | Missouri | Lafayette | 53 | 2527 | 3 | 4 | 6 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1885 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Pettis | 75 | 4755 | 3 | 4 | 8 |
| St. Louis-Farmington | Missouri | Warren | 17 | 2079 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 24 | 2555 | 3 | 2 | 2 |
| St. Louis-Farmington | Illinois | Clinton | 89 | 5540 | 3 | 6 | 14 |
| Missouri non-MSA | Missouri | Stone | 36 | 2013 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Benton | 25 | 1443 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Perry | 24 | 2037 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Pulaski | 43 | 2973 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Henry | 36 | 1726 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Barry | 44 | 2175 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 14 | 1612 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Vernon | 39 | 1383 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Saline | 35 | 2413 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 71 | 2741 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Barton | 12 | 955 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Marion | 41 | 2639 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Washington | 45 | 2116 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2295 | 1 | 1 | 4 |
| Missouri non-MSA | Missouri | Howell | 42 | 2790 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Livingston | 36 | 1322 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Miller | 49 | 2312 | 1 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Cooper | 24 | 1684 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Adair | 16 | 2054 | 1 | 2 | 4 |
| Springfield | Missouri | Webster | 49 | 2987 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | McDonald | 25 | 1911 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2403 | 1 | 2 | 3 |
| Kansas City | Missouri | Clinton | 64 | 1519 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 6 | 469 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Laclede | 64 | 2908 | 1 | 1 | 4 |
| Missouri non-MSA | Missouri | Camden | 80 | 3698 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | Mississippi | 24 | 1255 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Grundy | 34 | 827 | 1 | 0 | 1 |
| St. Joseph | Missouri | Andrew | 17 | 1279 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Macon | 13 | 1200 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Pike | 21 | 1483 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 28 | 1408 | 1 | 0 | 1 |
| Springfield | Missouri | Polk | 30 | 2136 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Texas | 22 | 1534 | 1 | 1 | 1 |
| Kansas City | Kansas | Linn | 8 | 743 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Audrain | 57 | 2066 | 1 | 1 | 3 |
| Columbia-Jefferson City | Missouri | Osage | 12 | 1393 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Scotland | 3 | 257 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 14 | 850 | 1 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 442 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carroll | 22 | 832 | 1 | 1 | 2 |
| St. Joseph | Missouri | DeKalb | 26 | 916 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 38 | 872 | 1 | 1 | 2 |
| Kansas City | Missouri | Bates | 22 | 1069 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Crawford | 29 | 2034 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Morgan | 39 | 1620 | 0 | 0 | 1 |
| St. Joseph | Kansas | Doniphan | 20 | 929 | 0 | 1 | 2 |
| Kansas City | Missouri | Caldwell | 10 | 639 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 567 | 0 | 1 | 0 |
| Springfield | Missouri | Dallas | 22 | 818 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Dent | 16 | 816 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Randolph | 28 | 1806 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 6 | 415 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 27 | 1365 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Ozark | 12 | 547 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 473 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 7 | 533 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 10 | 589 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 5 | 464 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1051 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Harrison | 14 | 826 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Cedar | 17 | 666 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Lewis | 5 | 628 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 29 | 1677 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Daviess | 11 | 585 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 478 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 746 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 10 | 813 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dade | 13 | 417 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 141 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 177 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 5 | 711 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 12 | 754 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Oregon | 3 | 672 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Holt | 10 | 366 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 23 | 765 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 260 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 20 | 733 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Hickory | 13 | 466 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 176 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 11 | 540 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 574 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 223 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 3 | 263 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 16 | 1342 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 6 | 349 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 8 | 417 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | New Madrid | 45 | 1764 | 0 | 0 | 1 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
* 1/17/2021: including cumulative deaths plots
* 1/4/2021: small fix for including 2021 data
* 7/20/2020:
  * update table insertion code
  * fix cases vs. deaths total header bug
  * include MSA totals table
  * added STL-Farmington County-level Deaths & Cases plots
  * including release notes in missouri_analysis.md
* 7/19/2020: 
  * code refactor
  * updating color scheme for plots
  * updating county numbers to table to include
  latest new daily case average numbers and
  sorting by last 7-day average
* 6/19/2020: Added description of MSAs & CSAs
* 6/16/2020: Including individual county totals (only) in analysis md table
* 6/11/2020:
  * Updated MSA definitions
  * Including table of individual county case counts
* 6/7/2020: Creating markdown & script
  * Including list of county-MSA/CSA associations to markdown
  * Including cumulative totals in MSA/CSA plots
* 5/30/2020: including plots of cumulative cases/deaths in jupyter notebook
* 5/17/2020: Initial analysis jupyter notebook created
* 4/4/2020: Cloned JHU CSSE Repository and set up development environment

### To-Do (updated 1/17/2021)
- [ ] Verify county population data

#### Analysis Page
- [x] Update description to accurately reflect CSA vs. MSA
- [x] Make table for CSA info
- [x] Include 7, 14, & 30 day changes for each county
- [ ] Plot top CSAs (for latest daily case change) with testing data
- [x] Analysis breakdown of St. Louis-Farmington counties
- [x] Include release notes and to-do list
- [ ] ~~Update color scheme~~, plot markers, and line thickness
- [ ] Include table of contents

#### Analysis Script
- [x] Simplify data ingestion and summarization functionality
- [x] Simplify plotting functionality
- [x] Include ability to update markdown with table between markdown sections
