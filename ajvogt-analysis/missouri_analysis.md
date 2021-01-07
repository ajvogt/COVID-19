# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/07/2021  
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


## Missouri New Daily Deaths by Metropolitan Statistcal Areas
![](images/mo_daily_deaths.png)

## Missouri New Daily Confirmed Cases by Metropolitan Statistcal Areas
![](images/mo_daily_cases.png)

## Missouri Metropolitan Statistical Area Totals
<!-- msa_table start -->
| MSA | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|
| St. Louis-Farmington | 3465 | 209948 | 1432 | 1348 | 1571 |
| Kansas City | 1722 | 142299 | 1096 | 1030 | 1127 |
| Missouri non-MSA | 1481 | 95588 | 625 | 559 | 657 |
| Springfield | 428 | 30705 | 276 | 218 | 239 |
| Columbia-Jefferson City | 218 | 30480 | 163 | 162 | 178 |
| Joplin | 226 | 13974 | 93 | 76 | 73 |
| Cape Girardeau-Sikeston | 185 | 11392 | 60 | 53 | 60 |
| St. Joseph | 141 | 8906 | 49 | 46 | 53 |
<!-- msa_table end -->

## STL-Farmington MSA New Daily Deaths by County
![](images/stl_daily_deaths.png)

## STL-Farmington MSA New Daily Confirmed Cases by County
![](images/stl_daily_cases.png)

<a name="msa-counties"></a>
## Metropolitan Statistical Area (MSA) Counties
<!-- county_table start -->
| MSA | State | County | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|---|---|
| St. Louis-Farmington | Missouri | St. Louis | 1408 | 71901 | 440 | 436 | 513 |
| Kansas City | Kansas | Johnson | 517 | 41357 | 356 | 330 | 371 |
| Kansas City | Missouri | Kansas City | 363 | 31386 | 228 | 202 | 201 |
| St. Louis-Farmington | Missouri | St. Charles | 299 | 28191 | 182 | 162 | 202 |
| Kansas City | Missouri | Jackson | 260 | 24441 | 179 | 166 | 177 |
| Springfield | Missouri | Greene | 289 | 19761 | 176 | 140 | 152 |
| St. Louis-Farmington | Illinois | Madison | 418 | 22058 | 175 | 161 | 190 |
| St. Louis-Farmington | Illinois | St. Clair | 372 | 20027 | 166 | 154 | 162 |
| St. Louis-Farmington | Missouri | Jefferson | 150 | 15878 | 139 | 112 | 119 |
| Kansas City | Kansas | Wyandotte | 201 | 16285 | 101 | 102 | 129 |
| Columbia-Jefferson City | Missouri | Boone | 50 | 13828 | 81 | 78 | 89 |
| Joplin | Missouri | Jasper | 167 | 10387 | 72 | 58 | 56 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17400 | 70 | 84 | 110 |
| St. Louis-Farmington | Missouri | Franklin | 115 | 6930 | 66 | 54 | 54 |
| Springfield | Missouri | Christian | 53 | 5780 | 54 | 44 | 51 |
| Kansas City | Missouri | Clay | 107 | 6526 | 45 | 47 | 48 |
| Kansas City | Missouri | Cass | 58 | 5807 | 44 | 43 | 51 |
| St. Louis-Farmington | Missouri | St. Francois | 75 | 6755 | 42 | 39 | 44 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 103 | 6651 | 38 | 35 | 38 |
| St. Louis-Farmington | Illinois | Clinton | 81 | 4663 | 34 | 28 | 33 |
| Columbia-Jefferson City | Missouri | Cole | 93 | 7816 | 34 | 36 | 36 |
| Kansas City | Kansas | Leavenworth | 46 | 5279 | 33 | 32 | 38 |
| St. Joseph | Missouri | Buchanan | 99 | 6201 | 30 | 27 | 33 |
| Missouri non-MSA | Missouri | Taney | 56 | 3907 | 28 | 21 | 24 |
| Missouri non-MSA | Missouri | Vernon | 24 | 1151 | 26 | 17 | 12 |
| Kansas City | Kansas | Miami | 15 | 2002 | 26 | 25 | 25 |
| St. Louis-Farmington | Illinois | Monroe | 61 | 3276 | 26 | 28 | 30 |
| St. Louis-Farmington | Illinois | Macoupin | 89 | 3413 | 25 | 24 | 28 |
| Springfield | Missouri | Webster | 43 | 2555 | 25 | 19 | 19 |
| Columbia-Jefferson City | Missouri | Callaway | 25 | 3913 | 24 | 24 | 25 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3666 | 23 | 22 | 30 |
| Missouri non-MSA | Missouri | Phelps | 89 | 2597 | 23 | 19 | 20 |
| Missouri non-MSA | Missouri | Pettis | 66 | 4170 | 23 | 23 | 39 |
| Kansas City | Missouri | Platte | 23 | 2542 | 22 | 24 | 22 |
| Joplin | Missouri | Newton | 59 | 3587 | 21 | 18 | 17 |
| Missouri non-MSA | Missouri | Camden | 64 | 3258 | 20 | 20 | 20 |
| Missouri non-MSA | Missouri | Howell | 38 | 2418 | 20 | 16 | 24 |
| Missouri non-MSA | Missouri | Lawrence | 57 | 2418 | 20 | 13 | 12 |
| Missouri non-MSA | Missouri | Butler | 16 | 2907 | 17 | 14 | 17 |
| Cape Girardeau-Sikeston | Missouri | Scott | 63 | 3417 | 17 | 14 | 16 |
| Springfield | Missouri | Polk | 24 | 1894 | 16 | 11 | 12 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3316 | 16 | 16 | 19 |
| Missouri non-MSA | Missouri | Adair | 5 | 1698 | 16 | 15 | 17 |
| Missouri non-MSA | Missouri | Wright | 24 | 1145 | 15 | 11 | 10 |
| Missouri non-MSA | Missouri | Laclede | 48 | 2587 | 15 | 14 | 18 |
| Missouri non-MSA | Missouri | Stone | 27 | 1701 | 15 | 12 | 12 |
| Missouri non-MSA | Missouri | Crawford | 20 | 1782 | 14 | 15 | 15 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1724 | 14 | 12 | 13 |
| Kansas City | Missouri | Lafayette | 42 | 2152 | 13 | 14 | 16 |
| Missouri non-MSA | Missouri | Saline | 26 | 2079 | 13 | 11 | 13 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2381 | 13 | 7 | 8 |
| Missouri non-MSA | Missouri | Marion | 30 | 2410 | 13 | 11 | 14 |
| Missouri non-MSA | Missouri | Barry | 37 | 1863 | 13 | 9 | 10 |
| Missouri non-MSA | Missouri | Miller | 42 | 2099 | 13 | 11 | 14 |
| St. Louis-Farmington | Illinois | Jersey | 44 | 2057 | 13 | 14 | 18 |
| Kansas City | Missouri | Ray | 9 | 1191 | 12 | 11 | 13 |
| Kansas City | Missouri | Bates | 13 | 886 | 12 | 9 | 9 |
| Missouri non-MSA | Missouri | Pulaski | 29 | 2598 | 11 | 9 | 20 |
| Missouri non-MSA | Missouri | Benton | 16 | 1250 | 11 | 7 | 12 |
| Missouri non-MSA | Missouri | Texas | 18 | 1395 | 10 | 9 | 11 |
| Missouri non-MSA | Missouri | Audrain | 41 | 1841 | 10 | 21 | 20 |
| Missouri non-MSA | Missouri | Washington | 41 | 1838 | 10 | 9 | 9 |
| St. Joseph | Missouri | Andrew | 15 | 1148 | 10 | 7 | 8 |
| St. Louis-Farmington | Illinois | Bond | 18 | 1609 | 9 | 9 | 13 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2133 | 9 | 8 | 11 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 8 | 1459 | 8 | 8 | 9 |
| Kansas City | Kansas | Linn | 3 | 579 | 8 | 7 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 18 | 1538 | 8 | 7 | 7 |
| Kansas City | Missouri | Clinton | 59 | 1302 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | Macon | 10 | 965 | 8 | 6 | 7 |
| Missouri non-MSA | Missouri | Madison | 11 | 1240 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Henry | 24 | 1470 | 7 | 6 | 9 |
| Missouri non-MSA | Missouri | Perry | 19 | 1893 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | McDonald | 21 | 1703 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Randolph | 19 | 1645 | 7 | 7 | 10 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2056 | 7 | 6 | 8 |
| Missouri non-MSA | Missouri | Cedar | 9 | 552 | 7 | 4 | 3 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1227 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Morgan | 24 | 1484 | 6 | 6 | 10 |
| Missouri non-MSA | Missouri | Gasconade | 30 | 709 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Douglas | 20 | 650 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 38 | 1647 | 5 | 6 | 7 |
| St. Joseph | Kansas | Doniphan | 7 | 762 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 21 | 1304 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Barton | 8 | 797 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Harrison | 10 | 654 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Gentry | 16 | 635 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Carroll | 18 | 682 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 481 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Pike | 16 | 1301 | 5 | 6 | 8 |
| Missouri non-MSA | Missouri | Oregon | 3 | 563 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Livingston | 24 | 1064 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Ralls | 7 | 687 | 4 | 4 | 5 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1517 | 4 | 5 | 8 |
| Missouri non-MSA | Missouri | Ripley | 9 | 695 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Wayne | 7 | 690 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Grundy | 25 | 702 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 521 | 4 | 4 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 641 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Lewis | 3 | 564 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Dent | 9 | 722 | 3 | 4 | 4 |
| Springfield | Missouri | Dallas | 19 | 715 | 3 | 2 | 2 |
| St. Joseph | Missouri | DeKalb | 20 | 795 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Ozark | 4 | 398 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Monroe | 6 | 538 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Maries | 7 | 478 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 4 | 311 | 3 | 2 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 400 | 3 | 3 | 3 |
| Kansas City | Missouri | Caldwell | 6 | 564 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 10 | 675 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 18 | 1152 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Chariton | 3 | 346 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 9 | 486 | 2 | 3 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 357 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 215 | 2 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 967 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Iron | 1 | 417 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Hickory | 9 | 440 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 6 | 384 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Shannon | 9 | 419 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 5 | 380 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Mercer | 1 | 139 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 10 | 376 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 233 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 233 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 156 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 9 | 330 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Linn | 10 | 420 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Atchison | 5 | 262 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 201 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 122 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
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

### To-Do (updated 7/20/2020)

#### Analysis Page
- [ ] Update description to accurately reflect CSA vs. MSA
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
