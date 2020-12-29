# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/29/2020  
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
| St. Louis-Farmington | 3239 | 196388 | 1201 | 1460 | 1717 |
| Kansas City | 1527 | 131953 | 933 | 1036 | 1166 |
| Missouri non-MSA | 1315 | 89973 | 488 | 594 | 722 |
| Springfield | 372 | 28403 | 169 | 215 | 240 |
| Columbia-Jefferson City | 193 | 28886 | 139 | 172 | 200 |
| Joplin | 197 | 13133 | 55 | 61 | 67 |
| Cape Girardeau-Sikeston | 172 | 10909 | 51 | 58 | 74 |
| St. Joseph | 128 | 8437 | 36 | 43 | 66 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1342 | 67459 | 368 | 473 | 557 |
| Kansas City | Kansas | Johnson | 418 | 37875 | 271 | 337 | 371 |
| Kansas City | Missouri | Kansas City | 349 | 29454 | 170 | 187 | 216 |
| St. Louis-Farmington | Missouri | St. Charles | 281 | 26571 | 157 | 196 | 228 |
| Kansas City | Missouri | Jackson | 230 | 22842 | 155 | 161 | 196 |
| St. Louis-Farmington | Illinois | Madison | 382 | 20434 | 149 | 176 | 207 |
| St. Louis-Farmington | Illinois | St. Clair | 338 | 18545 | 133 | 145 | 178 |
| Kansas City | Kansas | Wyandotte | 194 | 15206 | 129 | 117 | 126 |
| Springfield | Missouri | Greene | 251 | 18280 | 110 | 136 | 152 |
| St. Louis-Farmington | Missouri | Jefferson | 126 | 14685 | 88 | 105 | 128 |
| St. Louis-Farmington | Missouri | St. Louis City | 294 | 16596 | 87 | 109 | 127 |
| Columbia-Jefferson City | Missouri | Boone | 42 | 13069 | 72 | 87 | 95 |
| Kansas City | Missouri | Clay | 95 | 6103 | 44 | 43 | 51 |
| Kansas City | Missouri | Cass | 53 | 5395 | 42 | 50 | 55 |
| Joplin | Missouri | Jasper | 154 | 9755 | 41 | 46 | 53 |
| St. Louis-Farmington | Missouri | Franklin | 109 | 6363 | 38 | 48 | 53 |
| St. Louis-Farmington | Missouri | St. Francois | 68 | 6365 | 37 | 41 | 44 |
| Springfield | Missouri | Christian | 44 | 5322 | 35 | 48 | 53 |
| Missouri non-MSA | Missouri | Pulaski | 27 | 2503 | 31 | 24 | 30 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 95 | 6329 | 31 | 37 | 44 |
| Columbia-Jefferson City | Missouri | Cole | 85 | 7458 | 28 | 33 | 45 |
| St. Louis-Farmington | Illinois | Monroe | 57 | 3011 | 27 | 30 | 31 |
| Kansas City | Kansas | Leavenworth | 38 | 4939 | 25 | 36 | 40 |
| St. Louis-Farmington | Illinois | Clinton | 80 | 4352 | 25 | 30 | 35 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3460 | 23 | 30 | 35 |
| St. Joseph | Missouri | Buchanan | 91 | 5924 | 23 | 26 | 45 |
| Kansas City | Kansas | Miami | 11 | 1725 | 22 | 22 | 23 |
| St. Louis-Farmington | Illinois | Jersey | 39 | 1935 | 21 | 19 | 23 |
| Columbia-Jefferson City | Missouri | Callaway | 19 | 3663 | 21 | 25 | 29 |
| Kansas City | Missouri | Platte | 20 | 2302 | 19 | 21 | 22 |
| Missouri non-MSA | Missouri | Camden | 60 | 3074 | 19 | 19 | 21 |
| St. Louis-Farmington | Illinois | Macoupin | 74 | 3155 | 19 | 25 | 32 |
| Missouri non-MSA | Missouri | Phelps | 82 | 2409 | 18 | 19 | 22 |
| Missouri non-MSA | Missouri | Adair | 4 | 1562 | 18 | 18 | 16 |
| Missouri non-MSA | Missouri | Johnson | 28 | 3181 | 18 | 20 | 23 |
| Missouri non-MSA | Missouri | Taney | 51 | 3692 | 17 | 19 | 28 |
| Missouri non-MSA | Missouri | Crawford | 19 | 1648 | 16 | 16 | 15 |
| Cape Girardeau-Sikeston | Missouri | Scott | 59 | 3298 | 16 | 16 | 22 |
| Kansas City | Missouri | Lafayette | 38 | 2014 | 15 | 16 | 17 |
| Missouri non-MSA | Missouri | Audrain | 32 | 1602 | 14 | 16 | 17 |
| Joplin | Missouri | Newton | 43 | 3378 | 13 | 15 | 13 |
| Springfield | Missouri | Webster | 38 | 2347 | 13 | 17 | 18 |
| Missouri non-MSA | Missouri | Laclede | 44 | 2452 | 13 | 16 | 22 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1600 | 12 | 14 | 13 |
| Missouri non-MSA | Missouri | Butler | 14 | 2757 | 12 | 14 | 21 |
| Kansas City | Missouri | Ray | 8 | 1077 | 11 | 13 | 13 |
| Missouri non-MSA | Missouri | Howell | 36 | 2243 | 11 | 12 | 22 |
| Missouri non-MSA | Missouri | Pettis | 60 | 3883 | 11 | 24 | 40 |
| Missouri non-MSA | Missouri | Marion | 24 | 2279 | 10 | 11 | 17 |
| St. Louis-Farmington | Illinois | Bond | 16 | 1491 | 10 | 10 | 15 |
| Missouri non-MSA | Missouri | Saline | 21 | 1958 | 10 | 12 | 13 |
| Missouri non-MSA | Missouri | Randolph | 15 | 1579 | 9 | 10 | 13 |
| Missouri non-MSA | Missouri | Miller | 42 | 1983 | 9 | 15 | 16 |
| Missouri non-MSA | Missouri | Lawrence | 47 | 2261 | 8 | 10 | 12 |
| Missouri non-MSA | Missouri | Pike | 14 | 1252 | 8 | 9 | 12 |
| Missouri non-MSA | Missouri | Madison | 10 | 1161 | 8 | 9 | 9 |
| Missouri non-MSA | Missouri | Texas | 16 | 1310 | 8 | 11 | 12 |
| Missouri non-MSA | Missouri | Wright | 23 | 1024 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Stone | 24 | 1572 | 7 | 11 | 13 |
| Missouri non-MSA | Missouri | Iron | 1 | 391 | 7 | 6 | 5 |
| Springfield | Missouri | Polk | 21 | 1768 | 7 | 9 | 13 |
| Missouri non-MSA | Missouri | Washington | 39 | 1735 | 7 | 8 | 10 |
| Missouri non-MSA | Missouri | Dunklin | 15 | 2042 | 7 | 13 | 12 |
| Kansas City | Missouri | Bates | 10 | 786 | 7 | 8 | 8 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 3 | 1387 | 7 | 9 | 11 |
| Missouri non-MSA | Missouri | Barry | 35 | 1765 | 6 | 9 | 11 |
| Missouri non-MSA | Missouri | Vernon | 16 | 951 | 6 | 9 | 9 |
| Kansas City | Missouri | Clinton | 56 | 1211 | 6 | 8 | 11 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1628 | 6 | 8 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 29 | 1576 | 6 | 6 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1161 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Perry | 19 | 1824 | 5 | 9 | 10 |
| Missouri non-MSA | Missouri | Henry | 21 | 1400 | 5 | 9 | 11 |
| Missouri non-MSA | Missouri | Livingston | 21 | 998 | 5 | 8 | 7 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1465 | 5 | 9 | 10 |
| Kansas City | Kansas | Linn | 3 | 487 | 5 | 5 | 6 |
| St. Joseph | Missouri | Andrew | 14 | 1064 | 5 | 7 | 9 |
| Missouri non-MSA | Missouri | Macon | 8 | 890 | 5 | 8 | 7 |
| Missouri non-MSA | Missouri | Ralls | 6 | 638 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Wayne | 6 | 656 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Morgan | 21 | 1414 | 4 | 8 | 11 |
| Kansas City | Missouri | Caldwell | 4 | 537 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Carroll | 14 | 641 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Grundy | 22 | 661 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Stoddard | 32 | 1993 | 4 | 7 | 12 |
| Missouri non-MSA | Missouri | Harrison | 7 | 609 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 29 | 656 | 4 | 5 | 6 |
| St. Joseph | Missouri | DeKalb | 18 | 752 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Dent | 7 | 681 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Douglas | 19 | 599 | 4 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Moniteau | 17 | 1460 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Daviess | 9 | 460 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Ripley | 8 | 658 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Monroe | 5 | 501 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Oregon | 3 | 524 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Montgomery | 9 | 480 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2286 | 3 | 7 | 10 |
| St. Joseph | Kansas | Doniphan | 5 | 697 | 3 | 6 | 6 |
| Missouri non-MSA | Missouri | Gentry | 16 | 592 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Barton | 9 | 752 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Lewis | 3 | 525 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Clark | 4 | 365 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Benton | 16 | 1157 | 2 | 7 | 13 |
| Missouri non-MSA | Missouri | Ozark | 4 | 370 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Chariton | 2 | 320 | 2 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 11 | 947 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Maries | 6 | 453 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Pemiscot | 20 | 1257 | 2 | 4 | 6 |
| Missouri non-MSA | Missouri | St. Clair | 4 | 440 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 648 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Dade | 8 | 362 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 196 | 2 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 610 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Cedar | 8 | 500 | 2 | 2 | 2 |
| Springfield | Missouri | Dallas | 18 | 686 | 2 | 2 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 335 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 11 | 1109 | 1 | 4 | 8 |
| Missouri non-MSA | Missouri | Linn | 11 | 406 | 1 | 1 | 3 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 366 | 1 | 1 | 4 |
| Missouri non-MSA | Missouri | Hickory | 9 | 421 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 6 | 366 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shannon | 9 | 407 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shelby | 3 | 286 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Putnam | 1 | 197 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 1 | 125 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 115 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 221 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 323 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Atchison | 5 | 259 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 225 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 147 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
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
