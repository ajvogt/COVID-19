# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/26/2020  
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
| St. Louis-Farmington | 3199 | 193385 | 1447 | 1691 | 1817 |
| Kansas City | 1517 | 129199 | 943 | 1111 | 1179 |
| Missouri non-MSA | 1313 | 89057 | 613 | 760 | 760 |
| Springfield | 373 | 28013 | 209 | 266 | 247 |
| Columbia-Jefferson City | 193 | 28646 | 187 | 207 | 212 |
| Joplin | 197 | 13030 | 67 | 69 | 70 |
| Cape Girardeau-Sikeston | 170 | 10772 | 56 | 68 | 81 |
| St. Joseph | 127 | 8328 | 41 | 55 | 70 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1334 | 66284 | 446 | 525 | 583 |
| Kansas City | Kansas | Johnson | 413 | 36727 | 234 | 326 | 359 |
| St. Louis-Farmington | Missouri | St. Charles | 281 | 26232 | 199 | 244 | 242 |
| Kansas City | Missouri | Kansas City | 349 | 29001 | 193 | 215 | 227 |
| Kansas City | Missouri | Jackson | 230 | 22542 | 183 | 187 | 207 |
| St. Louis-Farmington | Illinois | Madison | 373 | 20181 | 178 | 207 | 220 |
| St. Louis-Farmington | Illinois | St. Clair | 331 | 18188 | 139 | 158 | 189 |
| Springfield | Missouri | Greene | 251 | 18026 | 131 | 169 | 156 |
| St. Louis-Farmington | Missouri | St. Louis City | 291 | 16382 | 130 | 127 | 136 |
| Kansas City | Kansas | Wyandotte | 193 | 14857 | 107 | 121 | 122 |
| St. Louis-Farmington | Missouri | Jefferson | 126 | 14494 | 104 | 130 | 137 |
| Columbia-Jefferson City | Missouri | Boone | 42 | 12969 | 97 | 108 | 99 |
| Kansas City | Missouri | Cass | 52 | 5316 | 54 | 61 | 58 |
| St. Louis-Farmington | Missouri | Franklin | 109 | 6271 | 50 | 58 | 56 |
| Springfield | Missouri | Christian | 45 | 5241 | 49 | 60 | 54 |
| Joplin | Missouri | Jasper | 154 | 9668 | 48 | 52 | 55 |
| Kansas City | Missouri | Clay | 93 | 6006 | 47 | 53 | 53 |
| St. Louis-Farmington | Missouri | St. Francois | 68 | 6273 | 39 | 52 | 46 |
| Missouri non-MSA | Missouri | Pulaski | 27 | 2487 | 38 | 31 | 32 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 94 | 6244 | 35 | 44 | 48 |
| Columbia-Jefferson City | Missouri | Cole | 85 | 7389 | 34 | 39 | 48 |
| St. Louis-Farmington | Illinois | Monroe | 56 | 2954 | 32 | 34 | 33 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3413 | 30 | 39 | 36 |
| St. Louis-Farmington | Illinois | Clinton | 80 | 4322 | 29 | 33 | 40 |
| Columbia-Jefferson City | Missouri | Callaway | 19 | 3625 | 26 | 28 | 31 |
| St. Joseph | Missouri | Buchanan | 91 | 5869 | 25 | 35 | 47 |
| Missouri non-MSA | Missouri | Phelps | 82 | 2381 | 23 | 22 | 24 |
| St. Louis-Farmington | Illinois | Macoupin | 66 | 3114 | 23 | 27 | 35 |
| Missouri non-MSA | Missouri | Johnson | 28 | 3145 | 22 | 24 | 24 |
| Kansas City | Missouri | Platte | 20 | 2257 | 22 | 23 | 22 |
| Missouri non-MSA | Missouri | Camden | 60 | 3027 | 21 | 21 | 21 |
| Kansas City | Missouri | Lafayette | 38 | 1988 | 21 | 18 | 18 |
| Missouri non-MSA | Missouri | Crawford | 19 | 1608 | 19 | 18 | 15 |
| Missouri non-MSA | Missouri | Adair | 4 | 1534 | 19 | 20 | 16 |
| Kansas City | Kansas | Miami | 10 | 1648 | 19 | 22 | 22 |
| Joplin | Missouri | Newton | 43 | 3362 | 18 | 16 | 14 |
| Missouri non-MSA | Missouri | Laclede | 44 | 2420 | 18 | 22 | 23 |
| St. Louis-Farmington | Illinois | Jersey | 36 | 1867 | 18 | 19 | 22 |
| Missouri non-MSA | Missouri | Taney | 51 | 3650 | 17 | 26 | 31 |
| Kansas City | Kansas | Leavenworth | 38 | 4823 | 17 | 34 | 40 |
| Missouri non-MSA | Missouri | Audrain | 31 | 1573 | 17 | 19 | 18 |
| Springfield | Missouri | Webster | 38 | 2313 | 17 | 20 | 18 |
| Missouri non-MSA | Missouri | Howell | 36 | 2232 | 16 | 37 | 22 |
| Cape Girardeau-Sikeston | Missouri | Scott | 59 | 3255 | 16 | 17 | 24 |
| Missouri non-MSA | Missouri | Saline | 21 | 1951 | 15 | 16 | 14 |
| Missouri non-MSA | Missouri | Miller | 42 | 1969 | 15 | 18 | 17 |
| Missouri non-MSA | Missouri | Pettis | 60 | 3876 | 14 | 42 | 41 |
| Missouri non-MSA | Missouri | Butler | 14 | 2733 | 14 | 18 | 22 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1572 | 14 | 15 | 14 |
| Kansas City | Missouri | Ray | 8 | 1057 | 13 | 15 | 13 |
| Missouri non-MSA | Missouri | Marion | 24 | 2258 | 13 | 13 | 19 |
| Missouri non-MSA | Missouri | Stone | 24 | 1553 | 11 | 13 | 14 |
| St. Louis-Farmington | Illinois | Bond | 16 | 1484 | 11 | 13 | 16 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1459 | 11 | 12 | 11 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 3 | 1375 | 11 | 12 | 12 |
| Missouri non-MSA | Missouri | Lawrence | 47 | 2247 | 11 | 12 | 13 |
| Missouri non-MSA | Missouri | Pike | 14 | 1235 | 10 | 11 | 12 |
| Missouri non-MSA | Missouri | Barry | 35 | 1750 | 10 | 11 | 11 |
| Missouri non-MSA | Missouri | Randolph | 15 | 1556 | 10 | 12 | 13 |
| Missouri non-MSA | Missouri | Washington | 39 | 1720 | 9 | 9 | 11 |
| Kansas City | Missouri | Clinton | 56 | 1205 | 9 | 12 | 11 |
| Missouri non-MSA | Missouri | Texas | 16 | 1285 | 9 | 14 | 11 |
| Springfield | Missouri | Polk | 21 | 1755 | 9 | 12 | 13 |
| Missouri non-MSA | Missouri | Vernon | 16 | 934 | 9 | 10 | 9 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2286 | 8 | 8 | 12 |
| Kansas City | Missouri | Bates | 10 | 770 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1609 | 8 | 8 | 7 |
| Missouri non-MSA | Missouri | Henry | 21 | 1392 | 8 | 11 | 12 |
| Missouri non-MSA | Missouri | Dunklin | 15 | 2026 | 8 | 14 | 13 |
| Missouri non-MSA | Missouri | Iron | 1 | 376 | 7 | 7 | 5 |
| Missouri non-MSA | Missouri | Madison | 10 | 1137 | 7 | 9 | 10 |
| Missouri non-MSA | Missouri | Wright | 23 | 999 | 7 | 10 | 8 |
| Missouri non-MSA | Missouri | Morgan | 21 | 1402 | 7 | 11 | 12 |
| Missouri non-MSA | Missouri | Livingston | 21 | 987 | 7 | 9 | 7 |
| Missouri non-MSA | Missouri | Perry | 19 | 1810 | 7 | 10 | 10 |
| St. Joseph | Missouri | Andrew | 13 | 1048 | 7 | 8 | 9 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1143 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Carroll | 14 | 634 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 29 | 1566 | 6 | 8 | 9 |
| Missouri non-MSA | Missouri | Macon | 8 | 885 | 6 | 9 | 8 |
| Missouri non-MSA | Missouri | Gasconade | 29 | 652 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Douglas | 19 | 595 | 6 | 8 | 6 |
| Missouri non-MSA | Missouri | Ralls | 6 | 631 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Benton | 16 | 1156 | 6 | 12 | 13 |
| Columbia-Jefferson City | Missouri | Moniteau | 17 | 1453 | 6 | 7 | 9 |
| St. Joseph | Kansas | Doniphan | 5 | 673 | 5 | 6 | 7 |
| Kansas City | Missouri | Caldwell | 4 | 527 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Dent | 7 | 675 | 5 | 5 | 6 |
| Kansas City | Kansas | Linn | 3 | 475 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Stoddard | 32 | 1978 | 5 | 10 | 14 |
| Missouri non-MSA | Missouri | Montgomery | 8 | 472 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 20 | 1255 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Wayne | 6 | 642 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Harrison | 7 | 598 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Daviess | 9 | 454 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Grundy | 22 | 649 | 4 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 608 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Gentry | 16 | 583 | 3 | 6 | 6 |
| Missouri non-MSA | Missouri | Chariton | 2 | 316 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 643 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Oregon | 3 | 517 | 3 | 7 | 5 |
| Missouri non-MSA | Missouri | Barton | 9 | 744 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Monroe | 5 | 494 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Mississippi | 11 | 1105 | 3 | 7 | 9 |
| Missouri non-MSA | Missouri | Dade | 8 | 358 | 3 | 2 | 2 |
| St. Joseph | Missouri | DeKalb | 18 | 738 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Clark | 4 | 364 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Ripley | 8 | 649 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Lewis | 3 | 517 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Maries | 6 | 450 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 4 | 430 | 2 | 3 | 4 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 11 | 940 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Ozark | 4 | 363 | 2 | 3 | 2 |
| Springfield | Missouri | Dallas | 18 | 678 | 2 | 3 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 6 | 333 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 191 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Cedar | 8 | 494 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 6 | 365 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 11 | 402 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Shannon | 9 | 403 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 3 | 283 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Hickory | 9 | 418 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Worth | 1 | 114 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mercer | 1 | 124 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 195 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 225 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 322 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 218 | 0 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 3 | 354 | 0 | 2 | 4 |
| Missouri non-MSA | Missouri | Knox | 1 | 147 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 5 | 258 | 0 | 0 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
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
