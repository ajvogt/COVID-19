# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/05/2021  
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
| St. Louis-Farmington | 3378 | 207574 | 1598 | 1399 | 1614 |
| Kansas City | 1609 | 139824 | 1124 | 1028 | 1140 |
| Missouri non-MSA | 1383 | 94515 | 648 | 568 | 669 |
| Springfield | 405 | 30069 | 238 | 203 | 235 |
| Columbia-Jefferson City | 198 | 30135 | 178 | 159 | 180 |
| Joplin | 222 | 13780 | 92 | 73 | 69 |
| St. Joseph | 138 | 8824 | 55 | 45 | 56 |
| Cape Girardeau-Sikeston | 178 | 11253 | 49 | 50 | 62 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1392 | 71447 | 569 | 469 | 538 |
| Kansas City | Kansas | Johnson | 456 | 40379 | 357 | 314 | 370 |
| Kansas City | Missouri | Kansas City | 356 | 31010 | 222 | 196 | 208 |
| St. Louis-Farmington | Illinois | Madison | 402 | 21688 | 179 | 164 | 192 |
| St. Louis-Farmington | Missouri | St. Charles | 290 | 27820 | 178 | 167 | 204 |
| Kansas City | Missouri | Jackson | 245 | 24069 | 175 | 165 | 180 |
| St. Louis-Farmington | Illinois | St. Clair | 361 | 19746 | 171 | 152 | 168 |
| Springfield | Missouri | Greene | 278 | 19334 | 150 | 130 | 149 |
| St. Louis-Farmington | Missouri | Jefferson | 134 | 15572 | 126 | 107 | 119 |
| Kansas City | Kansas | Wyandotte | 198 | 16029 | 117 | 123 | 131 |
| St. Louis-Farmington | Missouri | St. Louis City | 302 | 17347 | 107 | 97 | 117 |
| Columbia-Jefferson City | Missouri | Boone | 44 | 13638 | 81 | 76 | 89 |
| Joplin | Missouri | Jasper | 163 | 10238 | 69 | 55 | 53 |
| St. Louis-Farmington | Missouri | Franklin | 113 | 6819 | 65 | 51 | 55 |
| Springfield | Missouri | Christian | 49 | 5671 | 49 | 42 | 52 |
| Kansas City | Missouri | Clay | 98 | 6427 | 46 | 45 | 48 |
| Kansas City | Missouri | Cass | 55 | 5712 | 45 | 43 | 52 |
| St. Louis-Farmington | Missouri | St. Francois | 69 | 6681 | 45 | 41 | 44 |
| Columbia-Jefferson City | Missouri | Cole | 86 | 7745 | 41 | 34 | 37 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 99 | 6576 | 35 | 33 | 39 |
| Kansas City | Kansas | Leavenworth | 39 | 5183 | 34 | 30 | 39 |
| Missouri non-MSA | Missouri | Pettis | 61 | 4119 | 33 | 22 | 38 |
| Missouri non-MSA | Missouri | Audrain | 32 | 1834 | 33 | 23 | 21 |
| St. Joseph | Missouri | Buchanan | 98 | 6153 | 32 | 27 | 36 |
| St. Louis-Farmington | Illinois | Clinton | 80 | 4573 | 31 | 28 | 32 |
| St. Louis-Farmington | Illinois | Monroe | 61 | 3228 | 31 | 29 | 30 |
| Kansas City | Kansas | Miami | 15 | 1941 | 30 | 26 | 26 |
| Columbia-Jefferson City | Missouri | Callaway | 20 | 3869 | 29 | 25 | 26 |
| St. Louis-Farmington | Illinois | Macoupin | 82 | 3357 | 28 | 24 | 28 |
| Kansas City | Missouri | Platte | 23 | 2503 | 28 | 24 | 22 |
| Missouri non-MSA | Missouri | Vernon | 19 | 1139 | 26 | 16 | 13 |
| Missouri non-MSA | Missouri | Phelps | 86 | 2576 | 23 | 21 | 20 |
| Joplin | Missouri | Newton | 59 | 3542 | 23 | 18 | 15 |
| Missouri non-MSA | Missouri | Taney | 52 | 3851 | 22 | 20 | 24 |
| St. Louis-Farmington | Missouri | Lincoln | 19 | 3612 | 21 | 22 | 30 |
| Missouri non-MSA | Missouri | Howell | 37 | 2391 | 21 | 16 | 24 |
| Springfield | Missouri | Webster | 39 | 2494 | 21 | 17 | 18 |
| Missouri non-MSA | Missouri | Camden | 63 | 3217 | 20 | 20 | 20 |
| Missouri non-MSA | Missouri | Butler | 15 | 2879 | 17 | 14 | 18 |
| Missouri non-MSA | Missouri | Crawford | 19 | 1765 | 16 | 16 | 16 |
| Missouri non-MSA | Missouri | Marion | 24 | 2394 | 16 | 13 | 15 |
| Kansas City | Missouri | Lafayette | 40 | 2125 | 15 | 15 | 16 |
| Missouri non-MSA | Missouri | Saline | 23 | 2068 | 15 | 12 | 13 |
| Missouri non-MSA | Missouri | Johnson | 31 | 3290 | 15 | 16 | 20 |
| Missouri non-MSA | Missouri | Lawrence | 52 | 2370 | 15 | 12 | 12 |
| Missouri non-MSA | Missouri | Adair | 4 | 1670 | 15 | 16 | 16 |
| Missouri non-MSA | Missouri | Laclede | 46 | 2559 | 15 | 14 | 19 |
| Missouri non-MSA | Missouri | Wright | 24 | 1121 | 13 | 10 | 9 |
| St. Louis-Farmington | Illinois | Jersey | 43 | 2032 | 13 | 17 | 20 |
| Missouri non-MSA | Missouri | Miller | 41 | 2074 | 13 | 11 | 14 |
| Springfield | Missouri | Polk | 21 | 1859 | 13 | 10 | 11 |
| Missouri non-MSA | Missouri | Stone | 24 | 1663 | 13 | 10 | 12 |
| Missouri non-MSA | Missouri | Washington | 39 | 1825 | 12 | 10 | 9 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1690 | 12 | 12 | 12 |
| Kansas City | Missouri | Ray | 8 | 1166 | 12 | 12 | 13 |
| Missouri non-MSA | Missouri | Pulaski | 28 | 2590 | 12 | 22 | 23 |
| Kansas City | Missouri | Bates | 12 | 872 | 12 | 9 | 9 |
| Kansas City | Missouri | Clinton | 56 | 1295 | 12 | 9 | 10 |
| St. Louis-Farmington | Illinois | Bond | 17 | 1567 | 10 | 10 | 12 |
| Missouri non-MSA | Missouri | Madison | 10 | 1235 | 10 | 9 | 9 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1698 | 10 | 8 | 8 |
| Missouri non-MSA | Missouri | Dunklin | 15 | 2112 | 10 | 8 | 11 |
| Columbia-Jefferson City | Missouri | Moniteau | 17 | 1529 | 9 | 7 | 7 |
| St. Joseph | Missouri | Andrew | 14 | 1133 | 9 | 7 | 8 |
| Cape Girardeau-Sikeston | Missouri | Scott | 60 | 3367 | 9 | 13 | 16 |
| Missouri non-MSA | Missouri | Benton | 16 | 1225 | 9 | 6 | 11 |
| Missouri non-MSA | Missouri | Texas | 18 | 1378 | 9 | 8 | 11 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 5 | 1452 | 9 | 8 | 10 |
| Missouri non-MSA | Missouri | Barry | 36 | 1829 | 9 | 8 | 10 |
| Kansas City | Kansas | Linn | 3 | 550 | 9 | 7 | 7 |
| Missouri non-MSA | Missouri | Henry | 22 | 1462 | 8 | 7 | 9 |
| Missouri non-MSA | Missouri | Morgan | 24 | 1475 | 8 | 6 | 10 |
| Missouri non-MSA | Missouri | Livingston | 24 | 1054 | 8 | 6 | 8 |
| Missouri non-MSA | Missouri | Macon | 10 | 946 | 8 | 6 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 31 | 1631 | 7 | 7 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1216 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Perry | 19 | 1876 | 7 | 6 | 8 |
| Missouri non-MSA | Missouri | Randolph | 17 | 1631 | 7 | 8 | 10 |
| Missouri non-MSA | Missouri | Stoddard | 34 | 2044 | 7 | 5 | 9 |
| St. Joseph | Kansas | Doniphan | 7 | 746 | 7 | 5 | 6 |
| Missouri non-MSA | Missouri | Cedar | 8 | 549 | 7 | 4 | 3 |
| Missouri non-MSA | Missouri | Pike | 14 | 1298 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Ralls | 7 | 681 | 6 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1507 | 6 | 5 | 8 |
| Missouri non-MSA | Missouri | Gasconade | 29 | 697 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Harrison | 10 | 650 | 5 | 5 | 7 |
| St. Joseph | Missouri | DeKalb | 19 | 792 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Douglas | 19 | 638 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Dent | 8 | 719 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | St. Clair | 5 | 477 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 17 | 1146 | 5 | 3 | 6 |
| Missouri non-MSA | Missouri | Carroll | 18 | 677 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 513 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 21 | 1290 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Monroe | 5 | 533 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Lewis | 3 | 557 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Ripley | 8 | 689 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Wayne | 6 | 686 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Oregon | 3 | 554 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Gentry | 16 | 622 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Grundy | 23 | 691 | 4 | 4 | 5 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 395 | 4 | 2 | 3 |
| Missouri non-MSA | Missouri | Barton | 8 | 778 | 3 | 3 | 4 |
| Kansas City | Missouri | Caldwell | 5 | 563 | 3 | 4 | 4 |
| Springfield | Missouri | Dallas | 18 | 711 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Chariton | 3 | 343 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 4 | 392 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Maries | 6 | 474 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 3 | 631 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Daviess | 9 | 481 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 10 | 668 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Iron | 1 | 411 | 2 | 5 | 5 |
| Missouri non-MSA | Missouri | Shelby | 4 | 303 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Carter | 6 | 382 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 9 | 437 | 2 | 1 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 963 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 209 | 1 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 347 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 5 | 377 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Mercer | 1 | 136 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 230 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 155 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 9 | 414 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Dade | 9 | 369 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shannon | 9 | 414 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Scotland | 3 | 232 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 330 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 122 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 201 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 5 | 261 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2286 | 0 | 1 | 6 |
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
