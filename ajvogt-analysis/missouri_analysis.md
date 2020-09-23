# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 09/23/2020  
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
| St. Louis-Farmington | 1563 | 60674 | 524 | 551 | 562 |
| Missouri non-MSA | 252 | 22665 | 421 | 390 | 335 |
| Kansas City | 561 | 41963 | 351 | 343 | 349 |
| Springfield | 29 | 8124 | 169 | 174 | 156 |
| Columbia-Jefferson City | 24 | 7416 | 86 | 117 | 133 |
| Joplin | 61 | 4969 | 78 | 81 | 61 |
| Cape Girardeau-Sikeston | 28 | 2765 | 49 | 54 | 41 |
| St. Joseph | 17 | 2263 | 40 | 37 | 28 |
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
| St. Louis-Farmington | Missouri | St. Louis | 782 | 23137 | 149 | 164 | 175 |
| Springfield | Missouri | Greene | 19 | 5597 | 103 | 109 | 107 |
| Kansas City | Kansas | Johnson | 143 | 10320 | 100 | 95 | 100 |
| St. Louis-Farmington | Missouri | St. Charles | 115 | 7321 | 75 | 74 | 70 |
| Kansas City | Missouri | Kansas City | 107 | 10710 | 65 | 62 | 76 |
| Kansas City | Missouri | Jackson | 92 | 7064 | 65 | 70 | 67 |
| St. Louis-Farmington | Missouri | Jefferson | 53 | 3950 | 59 | 57 | 56 |
| Joplin | Missouri | Jasper | 47 | 3590 | 56 | 63 | 49 |
| St. Louis-Farmington | Illinois | Madison | 131 | 5414 | 56 | 59 | 61 |
| St. Louis-Farmington | Illinois | St. Clair | 187 | 6339 | 42 | 42 | 48 |
| Columbia-Jefferson City | Missouri | Boone | 6 | 4466 | 40 | 64 | 84 |
| Kansas City | Kansas | Wyandotte | 134 | 6725 | 31 | 31 | 34 |
| St. Louis-Farmington | Missouri | St. Louis City | 195 | 6886 | 31 | 31 | 32 |
| Springfield | Missouri | Christian | 3 | 1279 | 30 | 30 | 25 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 10 | 1548 | 29 | 32 | 23 |
| St. Joseph | Missouri | Buchanan | 14 | 1805 | 29 | 26 | 20 |
| St. Louis-Farmington | Missouri | St. Francois | 9 | 1949 | 28 | 42 | 38 |
| St. Louis-Farmington | Missouri | Franklin | 28 | 1573 | 28 | 28 | 23 |
| Columbia-Jefferson City | Missouri | Cole | 7 | 1398 | 23 | 26 | 22 |
| Joplin | Missouri | Newton | 14 | 1379 | 21 | 17 | 12 |
| Springfield | Missouri | Webster | 3 | 575 | 21 | 19 | 13 |
| Missouri non-MSA | Missouri | Camden | 10 | 863 | 20 | 17 | 13 |
| Missouri non-MSA | Missouri | Laclede | 3 | 572 | 19 | 16 | 10 |
| Kansas City | Missouri | Cass | 19 | 1420 | 18 | 18 | 15 |
| Kansas City | Missouri | Lafayette | 2 | 476 | 18 | 14 | 8 |
| Missouri non-MSA | Missouri | Pettis | 10 | 1043 | 17 | 13 | 10 |
| Missouri non-MSA | Missouri | Johnson | 4 | 1020 | 16 | 20 | 15 |
| St. Louis-Farmington | Illinois | Clinton | 20 | 1084 | 16 | 15 | 16 |
| Missouri non-MSA | Missouri | Howell | 3 | 541 | 15 | 14 | 11 |
| Missouri non-MSA | Missouri | Dunklin | 6 | 751 | 14 | 12 | 10 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 555 | 14 | 11 | 8 |
| Missouri non-MSA | Missouri | Pulaski | 5 | 590 | 14 | 11 | 8 |
| Kansas City | Missouri | Clay | 40 | 1743 | 14 | 16 | 16 |
| Kansas City | Kansas | Leavenworth | 11 | 1923 | 14 | 13 | 11 |
| Missouri non-MSA | Missouri | Wright | 0 | 259 | 13 | 10 | 6 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 466 | 13 | 10 | 6 |
| Missouri non-MSA | Missouri | Butler | 4 | 583 | 13 | 10 | 7 |
| Missouri non-MSA | Missouri | Morgan | 1 | 306 | 12 | 10 | 6 |
| Missouri non-MSA | Missouri | Taney | 28 | 1142 | 11 | 11 | 9 |
| Missouri non-MSA | Missouri | Miller | 1 | 454 | 11 | 10 | 8 |
| Springfield | Missouri | Polk | 3 | 493 | 10 | 10 | 7 |
| Missouri non-MSA | Missouri | Texas | 2 | 280 | 10 | 8 | 6 |
| Missouri non-MSA | Missouri | Perry | 4 | 605 | 10 | 11 | 10 |
| Cape Girardeau-Sikeston | Missouri | Scott | 16 | 827 | 10 | 9 | 9 |
| Missouri non-MSA | Missouri | Crawford | 2 | 362 | 9 | 10 | 7 |
| Missouri non-MSA | Missouri | Phelps | 5 | 419 | 9 | 10 | 8 |
| Missouri non-MSA | Missouri | Benton | 2 | 251 | 9 | 6 | 3 |
| Kansas City | Missouri | Platte | 10 | 643 | 8 | 7 | 6 |
| St. Louis-Farmington | Illinois | Macoupin | 7 | 498 | 8 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Callaway | 2 | 589 | 8 | 10 | 11 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 1 | 317 | 7 | 11 | 7 |
| Missouri non-MSA | Missouri | Saline | 9 | 676 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 9 | 486 | 7 | 7 | 6 |
| St. Louis-Farmington | Illinois | Bond | 4 | 294 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Stone | 4 | 406 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 9 | 726 | 6 | 6 | 15 |
| St. Louis-Farmington | Illinois | Monroe | 15 | 627 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Barry | 6 | 452 | 5 | 5 | 4 |
| St. Joseph | Missouri | Andrew | 1 | 230 | 5 | 5 | 4 |
| St. Louis-Farmington | Missouri | Lincoln | 3 | 722 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Wayne | 0 | 192 | 5 | 6 | 4 |
| St. Louis-Farmington | Missouri | Warren | 0 | 451 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Audrain | 2 | 411 | 5 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Cooper | 2 | 389 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Washington | 10 | 342 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Madison | 0 | 284 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Macon | 0 | 146 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Randolph | 3 | 224 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Dent | 1 | 129 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | McDonald | 11 | 1049 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Grundy | 2 | 173 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Douglas | 3 | 169 | 4 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 4 | 281 | 4 | 5 | 3 |
| Kansas City | Kansas | Miami | 1 | 328 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Vernon | 1 | 162 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Carter | 1 | 83 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Livingston | 1 | 388 | 4 | 3 | 10 |
| Missouri non-MSA | Missouri | Adair | 0 | 322 | 4 | 3 | 3 |
| Springfield | Missouri | Dallas | 1 | 180 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Ozark | 0 | 117 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 183 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 0 | 94 | 3 | 3 | 2 |
| St. Louis-Farmington | Illinois | Jersey | 14 | 385 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Marion | 14 | 634 | 3 | 5 | 9 |
| St. Joseph | Missouri | DeKalb | 2 | 123 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Barton | 0 | 175 | 3 | 4 | 3 |
| Kansas City | Missouri | Clinton | 0 | 206 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Cedar | 0 | 91 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Pike | 3 | 229 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 15 | 509 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Mississippi | 3 | 289 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Oregon | 0 | 101 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shannon | 1 | 87 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 4 | 167 | 2 | 2 | 2 |
| Kansas City | Missouri | Caldwell | 1 | 78 | 2 | 2 | 1 |
| Kansas City | Missouri | Bates | 1 | 101 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 17 | 157 | 2 | 4 | 3 |
| St. Joseph | Kansas | Doniphan | 0 | 105 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 1 | 83 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 47 | 2 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 165 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 2 | 88 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 128 | 1 | 2 | 1 |
| Kansas City | Missouri | Ray | 0 | 158 | 1 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 1 | 73 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Linn | 1 | 63 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 54 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 37 | 1 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 44 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 72 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 145 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Lewis | 2 | 77 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 117 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 52 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carroll | 1 | 136 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 144 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 61 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 68 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 29 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 86 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 60 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 101 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 1 | 49 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 75 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 185 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 28 | 0 | 0 | 0 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
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
