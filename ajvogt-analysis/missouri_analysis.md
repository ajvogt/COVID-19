# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/27/2021  
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
| St. Louis-Farmington | 4020 | 236298 | 1095 | 1131 | 1362 |
| Kansas City | 2047 | 161661 | 849 | 871 | 1058 |
| Missouri non-MSA | 1686 | 104855 | 319 | 359 | 505 |
| Springfield | 530 | 34146 | 118 | 131 | 195 |
| Columbia-Jefferson City | 261 | 32843 | 88 | 96 | 134 |
| Joplin | 252 | 15273 | 52 | 58 | 73 |
| St. Joseph | 170 | 9687 | 29 | 30 | 43 |
| Cape Girardeau-Sikeston | 201 | 12200 | 25 | 30 | 44 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1655 | 81758 | 389 | 403 | 487 |
| Kansas City | Kansas | Johnson | 632 | 48309 | 328 | 347 | 386 |
| St. Louis-Farmington | Illinois | Madison | 487 | 25542 | 163 | 164 | 173 |
| Kansas City | Missouri | Kansas City | 435 | 34888 | 143 | 141 | 185 |
| Kansas City | Missouri | Jackson | 305 | 27751 | 139 | 135 | 167 |
| St. Louis-Farmington | Illinois | St. Clair | 457 | 23211 | 124 | 139 | 159 |
| St. Louis-Farmington | Missouri | St. Charles | 344 | 31147 | 108 | 119 | 155 |
| Springfield | Missouri | Greene | 377 | 21973 | 75 | 84 | 125 |
| St. Louis-Farmington | Missouri | Jefferson | 168 | 17908 | 74 | 83 | 109 |
| St. Louis-Farmington | Missouri | St. Louis City | 310 | 18063 | 70 | 43 | 51 |
| Kansas City | Kansas | Wyandotte | 225 | 17860 | 63 | 76 | 100 |
| Columbia-Jefferson City | Missouri | Boone | 61 | 15062 | 52 | 53 | 67 |
| Joplin | Missouri | Jasper | 192 | 11397 | 41 | 45 | 56 |
| Kansas City | Missouri | Cass | 68 | 6727 | 38 | 39 | 45 |
| St. Louis-Farmington | Missouri | Franklin | 131 | 7896 | 33 | 39 | 51 |
| Kansas City | Kansas | Leavenworth | 53 | 6011 | 33 | 35 | 39 |
| Kansas City | Missouri | Clay | 122 | 7343 | 32 | 32 | 42 |
| St. Louis-Farmington | Illinois | Macoupin | 98 | 4056 | 29 | 28 | 30 |
| Kansas City | Kansas | Miami | 22 | 2420 | 28 | 20 | 25 |
| Springfield | Missouri | Christian | 62 | 6483 | 26 | 27 | 39 |
| St. Louis-Farmington | Illinois | Clinton | 87 | 5208 | 25 | 26 | 28 |
| St. Louis-Farmington | Illinois | Monroe | 71 | 3720 | 19 | 19 | 24 |
| St. Joseph | Missouri | Buchanan | 119 | 6691 | 17 | 19 | 25 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 110 | 7139 | 15 | 18 | 27 |
| St. Louis-Farmington | Missouri | St. Francois | 83 | 7282 | 14 | 17 | 31 |
| Columbia-Jefferson City | Missouri | Cole | 104 | 8271 | 14 | 15 | 27 |
| Missouri non-MSA | Missouri | Taney | 68 | 4333 | 13 | 15 | 21 |
| St. Louis-Farmington | Illinois | Jersey | 62 | 2317 | 13 | 13 | 13 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 4008 | 12 | 13 | 18 |
| Missouri non-MSA | Missouri | Pettis | 69 | 4555 | 11 | 14 | 22 |
| Missouri non-MSA | Missouri | Butler | 23 | 3178 | 11 | 11 | 14 |
| Joplin | Missouri | Newton | 60 | 3876 | 11 | 12 | 16 |
| Springfield | Missouri | Webster | 46 | 2877 | 10 | 12 | 18 |
| Columbia-Jefferson City | Missouri | Callaway | 34 | 4217 | 10 | 12 | 18 |
| Missouri non-MSA | Missouri | Johnson | 35 | 3622 | 10 | 11 | 15 |
| Missouri non-MSA | Missouri | Macon | 10 | 1140 | 9 | 8 | 8 |
| Kansas City | Missouri | Lafayette | 46 | 2362 | 9 | 8 | 12 |
| St. Louis-Farmington | Missouri | Warren | 12 | 1942 | 9 | 9 | 11 |
| Missouri non-MSA | Missouri | Adair | 7 | 1945 | 9 | 10 | 13 |
| Missouri non-MSA | Missouri | Camden | 73 | 3575 | 9 | 10 | 17 |
| Missouri non-MSA | Missouri | Howell | 41 | 2702 | 9 | 11 | 15 |
| Kansas City | Missouri | Platte | 34 | 2854 | 8 | 10 | 18 |
| Kansas City | Missouri | Ray | 17 | 1378 | 8 | 7 | 10 |
| Missouri non-MSA | Missouri | Lawrence | 61 | 2609 | 8 | 5 | 11 |
| Missouri non-MSA | Missouri | Saline | 30 | 2300 | 8 | 8 | 11 |
| Missouri non-MSA | Missouri | Laclede | 56 | 2793 | 7 | 8 | 11 |
| St. Louis-Farmington | Illinois | Bond | 26 | 1789 | 7 | 6 | 10 |
| Missouri non-MSA | Missouri | Phelps | 107 | 2861 | 7 | 11 | 15 |
| Missouri non-MSA | Missouri | Audrain | 49 | 2003 | 7 | 6 | 13 |
| Missouri non-MSA | Missouri | Marion | 36 | 2569 | 7 | 6 | 9 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2319 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Washington | 41 | 2047 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2203 | 6 | 6 | 7 |
| Cape Girardeau-Sikeston | Missouri | Scott | 71 | 3633 | 6 | 8 | 11 |
| Missouri non-MSA | Missouri | Crawford | 23 | 1961 | 6 | 6 | 10 |
| Missouri non-MSA | Missouri | Miller | 45 | 2262 | 6 | 6 | 9 |
| Missouri non-MSA | Missouri | Livingston | 26 | 1237 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | Barry | 41 | 2082 | 6 | 10 | 10 |
| Kansas City | Missouri | Bates | 16 | 1008 | 5 | 4 | 7 |
| Missouri non-MSA | Missouri | Harrison | 11 | 773 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Stone | 29 | 1886 | 5 | 7 | 10 |
| Missouri non-MSA | Missouri | Henry | 28 | 1621 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Carroll | 18 | 773 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | McDonald | 24 | 1855 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Linn | 10 | 517 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Vernon | 31 | 1317 | 4 | 5 | 12 |
| Columbia-Jefferson City | Missouri | Osage | 10 | 1338 | 4 | 4 | 6 |
| St. Joseph | Kansas | Doniphan | 12 | 874 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Pike | 17 | 1427 | 4 | 5 | 6 |
| Kansas City | Missouri | Clinton | 60 | 1450 | 4 | 4 | 7 |
| Kansas City | Kansas | Linn | 4 | 688 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Pulaski | 34 | 2892 | 4 | 6 | 13 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 12 | 1549 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Perry | 22 | 1982 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Ozark | 10 | 513 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Wright | 24 | 1300 | 3 | 5 | 9 |
| St. Joseph | Missouri | Andrew | 16 | 1238 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | St. Clair | 6 | 539 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Gasconade | 33 | 823 | 3 | 4 | 5 |
| St. Joseph | Missouri | DeKalb | 23 | 884 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2501 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | Benton | 20 | 1370 | 3 | 4 | 7 |
| Missouri non-MSA | Missouri | Mississippi | 21 | 1204 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 41 | 1728 | 3 | 2 | 5 |
| Missouri non-MSA | Missouri | Madison | 13 | 1316 | 3 | 2 | 5 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1643 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Wayne | 9 | 781 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Gentry | 19 | 706 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Ripley | 10 | 769 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Douglas | 23 | 737 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Barton | 9 | 903 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Daviess | 10 | 551 | 2 | 2 | 3 |
| Springfield | Missouri | Polk | 25 | 2038 | 2 | 4 | 9 |
| Missouri non-MSA | Missouri | Chariton | 3 | 400 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 9 | 631 | 2 | 3 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1624 | 2 | 4 | 5 |
| Springfield | Missouri | Dallas | 20 | 775 | 2 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 407 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Morgan | 34 | 1584 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1370 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dent | 10 | 788 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 255 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Grundy | 30 | 792 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Ralls | 10 | 733 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Oregon | 3 | 651 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Texas | 21 | 1489 | 2 | 3 | 6 |
| Missouri non-MSA | Missouri | Randolph | 24 | 1778 | 2 | 5 | 6 |
| Kansas City | Missouri | Caldwell | 8 | 612 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 6 | 433 | 1 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 688 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Dade | 12 | 407 | 1 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 5 | 451 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 12 | 737 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 5 | 341 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 514 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Lewis | 3 | 617 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Monroe | 7 | 572 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Holt | 10 | 355 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 216 | 1 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1021 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 2 | 169 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 1 | 457 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Worth | 1 | 136 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 548 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Carter | 8 | 408 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 452 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 2 | 159 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Hickory | 10 | 456 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 255 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 236 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 287 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
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
