# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/06/2021  
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
| St. Louis-Farmington | 3442 | 208881 | 1538 | 1392 | 1593 |
| Kansas City | 1714 | 140325 | 1120 | 1033 | 1127 |
| Missouri non-MSA | 1464 | 95121 | 652 | 575 | 661 |
| Springfield | 426 | 30444 | 263 | 217 | 237 |
| Columbia-Jefferson City | 218 | 30232 | 169 | 161 | 176 |
| Joplin | 225 | 13844 | 94 | 76 | 69 |
| Cape Girardeau-Sikeston | 184 | 11326 | 56 | 51 | 60 |
| St. Joseph | 140 | 8861 | 53 | 45 | 55 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1406 | 71901 | 525 | 473 | 533 |
| Kansas City | Kansas | Johnson | 517 | 40380 | 357 | 314 | 370 |
| Kansas City | Missouri | Kansas City | 361 | 31191 | 221 | 199 | 202 |
| St. Louis-Farmington | Illinois | Madison | 411 | 21825 | 181 | 161 | 188 |
| St. Louis-Farmington | Illinois | St. Clair | 364 | 19881 | 179 | 151 | 166 |
| St. Louis-Farmington | Missouri | St. Charles | 298 | 27990 | 178 | 167 | 201 |
| Kansas City | Missouri | Jackson | 258 | 24252 | 176 | 169 | 176 |
| Springfield | Missouri | Greene | 287 | 19596 | 168 | 141 | 151 |
| St. Louis-Farmington | Missouri | Jefferson | 150 | 15716 | 133 | 110 | 118 |
| Kansas City | Kansas | Wyandotte | 201 | 16029 | 117 | 123 | 131 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17380 | 82 | 91 | 113 |
| Columbia-Jefferson City | Missouri | Boone | 50 | 13683 | 78 | 78 | 87 |
| Joplin | Missouri | Jasper | 166 | 10287 | 70 | 57 | 53 |
| St. Louis-Farmington | Missouri | Franklin | 115 | 6859 | 64 | 51 | 54 |
| Springfield | Missouri | Christian | 53 | 5735 | 53 | 45 | 52 |
| Kansas City | Missouri | Clay | 103 | 6475 | 46 | 45 | 47 |
| St. Louis-Farmington | Missouri | St. Francois | 75 | 6719 | 44 | 40 | 44 |
| Kansas City | Missouri | Cass | 58 | 5750 | 43 | 43 | 51 |
| Columbia-Jefferson City | Missouri | Cole | 93 | 7771 | 40 | 35 | 36 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 103 | 6620 | 37 | 34 | 38 |
| Kansas City | Kansas | Leavenworth | 46 | 5183 | 34 | 30 | 39 |
| St. Joseph | Missouri | Buchanan | 98 | 6183 | 32 | 27 | 35 |
| St. Louis-Farmington | Illinois | Clinton | 80 | 4600 | 31 | 27 | 32 |
| Kansas City | Kansas | Miami | 15 | 1941 | 30 | 26 | 26 |
| Missouri non-MSA | Missouri | Audrain | 41 | 1835 | 29 | 22 | 20 |
| St. Louis-Farmington | Illinois | Monroe | 61 | 3250 | 29 | 28 | 30 |
| Missouri non-MSA | Missouri | Taney | 56 | 3894 | 28 | 21 | 24 |
| Kansas City | Missouri | Platte | 23 | 2521 | 28 | 24 | 22 |
| Columbia-Jefferson City | Missouri | Callaway | 25 | 3886 | 27 | 25 | 25 |
| Missouri non-MSA | Missouri | Vernon | 24 | 1144 | 26 | 17 | 12 |
| St. Louis-Farmington | Illinois | Macoupin | 86 | 3379 | 25 | 23 | 28 |
| Springfield | Missouri | Webster | 43 | 2532 | 24 | 18 | 19 |
| Joplin | Missouri | Newton | 59 | 3557 | 24 | 18 | 16 |
| Missouri non-MSA | Missouri | Pettis | 66 | 4145 | 23 | 22 | 39 |
| Missouri non-MSA | Missouri | Phelps | 89 | 2589 | 23 | 21 | 20 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3639 | 23 | 22 | 30 |
| Missouri non-MSA | Missouri | Camden | 64 | 3227 | 20 | 19 | 20 |
| Missouri non-MSA | Missouri | Lawrence | 57 | 2407 | 20 | 13 | 12 |
| Missouri non-MSA | Missouri | Howell | 38 | 2403 | 19 | 16 | 24 |
| Missouri non-MSA | Missouri | Butler | 16 | 2895 | 17 | 15 | 17 |
| Missouri non-MSA | Missouri | Laclede | 46 | 2575 | 17 | 14 | 18 |
| Missouri non-MSA | Missouri | Stone | 25 | 1694 | 16 | 12 | 13 |
| Missouri non-MSA | Missouri | Crawford | 20 | 1776 | 15 | 16 | 16 |
| Missouri non-MSA | Missouri | Wright | 24 | 1138 | 15 | 11 | 10 |
| Missouri non-MSA | Missouri | Adair | 5 | 1681 | 15 | 15 | 17 |
| Cape Girardeau-Sikeston | Missouri | Scott | 62 | 3392 | 15 | 13 | 15 |
| Kansas City | Missouri | Lafayette | 42 | 2140 | 15 | 14 | 16 |
| Missouri non-MSA | Missouri | Saline | 26 | 2075 | 14 | 12 | 13 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3297 | 14 | 16 | 20 |
| Missouri non-MSA | Missouri | Marion | 30 | 2403 | 14 | 12 | 14 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1707 | 13 | 13 | 13 |
| Missouri non-MSA | Missouri | Miller | 41 | 2083 | 13 | 11 | 14 |
| St. Louis-Farmington | Illinois | Jersey | 44 | 2046 | 13 | 15 | 19 |
| Springfield | Missouri | Polk | 24 | 1867 | 13 | 10 | 11 |
| Missouri non-MSA | Missouri | Barry | 37 | 1856 | 12 | 9 | 10 |
| Missouri non-MSA | Missouri | Washington | 41 | 1836 | 12 | 10 | 9 |
| Kansas City | Missouri | Ray | 9 | 1176 | 12 | 11 | 12 |
| Missouri non-MSA | Missouri | Nodaway | 20 | 2372 | 12 | 7 | 8 |
| Missouri non-MSA | Missouri | Pulaski | 29 | 2595 | 11 | 17 | 21 |
| Kansas City | Missouri | Bates | 13 | 876 | 11 | 9 | 9 |
| Missouri non-MSA | Missouri | Benton | 16 | 1244 | 11 | 7 | 11 |
| Kansas City | Missouri | Clinton | 59 | 1297 | 10 | 8 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2129 | 9 | 9 | 11 |
| Missouri non-MSA | Missouri | Texas | 19 | 1383 | 9 | 9 | 11 |
| St. Joseph | Missouri | Andrew | 15 | 1140 | 9 | 7 | 8 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 6 | 1455 | 9 | 8 | 9 |
| Columbia-Jefferson City | Missouri | Moniteau | 18 | 1533 | 9 | 7 | 7 |
| Missouri non-MSA | Missouri | McDonald | 21 | 1701 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Madison | 11 | 1238 | 9 | 9 | 9 |
| Kansas City | Kansas | Linn | 3 | 550 | 9 | 7 | 7 |
| St. Louis-Farmington | Illinois | Bond | 17 | 1589 | 8 | 9 | 13 |
| Missouri non-MSA | Missouri | Henry | 24 | 1466 | 8 | 7 | 9 |
| Missouri non-MSA | Missouri | Morgan | 24 | 1480 | 8 | 6 | 10 |
| Missouri non-MSA | Missouri | Macon | 10 | 946 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Livingston | 24 | 1055 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Randolph | 18 | 1634 | 7 | 8 | 10 |
| St. Joseph | Kansas | Doniphan | 7 | 746 | 7 | 5 | 6 |
| Missouri non-MSA | Missouri | Cedar | 9 | 551 | 7 | 4 | 3 |
| Missouri non-MSA | Missouri | Perry | 19 | 1885 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2046 | 6 | 5 | 8 |
| Missouri non-MSA | Missouri | Gasconade | 30 | 705 | 6 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1217 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Harrison | 10 | 653 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Douglas | 19 | 648 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Pike | 16 | 1300 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Carroll | 18 | 679 | 5 | 4 | 6 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1508 | 5 | 5 | 8 |
| Missouri non-MSA | Missouri | Barton | 8 | 794 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 21 | 1298 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Ralls | 7 | 682 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Oregon | 3 | 561 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 477 | 5 | 3 | 3 |
| St. Joseph | Missouri | DeKalb | 20 | 792 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 32 | 1635 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Lewis | 3 | 559 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 519 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Ripley | 9 | 691 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Monroe | 6 | 536 | 4 | 4 | 4 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 400 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Grundy | 24 | 693 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Wayne | 7 | 687 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Dent | 9 | 722 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Mississippi | 18 | 1148 | 4 | 3 | 5 |
| Springfield | Missouri | Dallas | 19 | 714 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Gentry | 16 | 623 | 4 | 3 | 5 |
| Kansas City | Missouri | Caldwell | 6 | 564 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Chariton | 3 | 346 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Ozark | 4 | 396 | 3 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 634 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Maries | 7 | 476 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 9 | 485 | 2 | 3 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 965 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 10 | 671 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Shelby | 4 | 307 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 213 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Iron | 1 | 413 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Carter | 6 | 383 | 2 | 1 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 349 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 5 | 378 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Hickory | 9 | 437 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Dade | 10 | 372 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 135 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 232 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 9 | 416 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Linn | 10 | 416 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Scotland | 3 | 233 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 330 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 155 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 122 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 201 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 5 | 261 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
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
