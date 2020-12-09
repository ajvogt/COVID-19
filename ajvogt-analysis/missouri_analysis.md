# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/09/2020  
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
| St. Louis-Farmington | 2637 | 164611 | 2035 | 2019 | 2179 |
| Kansas City | 1276 | 109113 | 1305 | 1238 | 1298 |
| Missouri non-MSA | 994 | 76594 | 867 | 803 | 926 |
| Springfield | 299 | 23823 | 274 | 246 | 251 |
| Columbia-Jefferson City | 139 | 25223 | 256 | 239 | 301 |
| Cape Girardeau-Sikeston | 127 | 9650 | 101 | 101 | 126 |
| St. Joseph | 100 | 7432 | 96 | 93 | 94 |
| Joplin | 166 | 11879 | 83 | 79 | 112 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1109 | 57091 | 667 | 657 | 715 |
| Kansas City | Kansas | Johnson | 312 | 30199 | 397 | 369 | 380 |
| St. Louis-Farmington | Missouri | St. Charles | 228 | 22376 | 266 | 266 | 299 |
| Kansas City | Missouri | Kansas City | 313 | 25544 | 261 | 261 | 287 |
| St. Louis-Farmington | Illinois | Madison | 298 | 16537 | 243 | 231 | 246 |
| Kansas City | Missouri | Jackson | 193 | 19335 | 239 | 230 | 245 |
| St. Louis-Farmington | Illinois | St. Clair | 284 | 15326 | 223 | 213 | 202 |
| Springfield | Missouri | Greene | 215 | 15367 | 171 | 157 | 160 |
| St. Louis-Farmington | Missouri | Jefferson | 111 | 12408 | 155 | 164 | 180 |
| St. Louis-Farmington | Missouri | St. Louis City | 263 | 14255 | 152 | 152 | 154 |
| Kansas City | Kansas | Wyandotte | 184 | 12407 | 125 | 105 | 104 |
| Columbia-Jefferson City | Missouri | Boone | 28 | 11188 | 114 | 101 | 124 |
| Joplin | Missouri | Jasper | 127 | 8783 | 67 | 63 | 87 |
| St. Joseph | Missouri | Buchanan | 67 | 5280 | 67 | 63 | 62 |
| Kansas City | Missouri | Cass | 41 | 4319 | 64 | 56 | 61 |
| Columbia-Jefferson City | Missouri | Cole | 65 | 6728 | 64 | 63 | 85 |
| Springfield | Missouri | Christian | 28 | 4295 | 59 | 52 | 50 |
| St. Louis-Farmington | Missouri | Franklin | 95 | 5341 | 58 | 59 | 66 |
| Kansas City | Missouri | Clay | 80 | 5119 | 57 | 56 | 66 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 70 | 5530 | 53 | 58 | 73 |
| Missouri non-MSA | Missouri | Pettis | 38 | 3060 | 52 | 33 | 29 |
| Missouri non-MSA | Missouri | Pulaski | 24 | 1995 | 47 | 34 | 27 |
| Kansas City | Kansas | Leavenworth | 34 | 4138 | 45 | 45 | 40 |
| St. Louis-Farmington | Illinois | Clinton | 66 | 3684 | 43 | 46 | 50 |
| St. Louis-Farmington | Missouri | St. Francois | 51 | 5453 | 42 | 47 | 64 |
| Missouri non-MSA | Missouri | Taney | 42 | 3215 | 40 | 37 | 37 |
| St. Louis-Farmington | Missouri | Lincoln | 13 | 2784 | 39 | 37 | 42 |
| Columbia-Jefferson City | Missouri | Callaway | 13 | 3150 | 39 | 36 | 41 |
| St. Louis-Farmington | Illinois | Macoupin | 28 | 2593 | 38 | 43 | 49 |
| St. Louis-Farmington | Illinois | Monroe | 50 | 2378 | 36 | 31 | 37 |
| Cape Girardeau-Sikeston | Missouri | Scott | 43 | 2962 | 35 | 33 | 40 |
| Missouri non-MSA | Missouri | Laclede | 35 | 2055 | 30 | 25 | 21 |
| St. Louis-Farmington | Illinois | Jersey | 25 | 1529 | 29 | 27 | 26 |
| Missouri non-MSA | Missouri | Phelps | 53 | 2022 | 28 | 30 | 31 |
| Missouri non-MSA | Missouri | Butler | 10 | 2407 | 28 | 28 | 29 |
| Missouri non-MSA | Missouri | Camden | 51 | 2671 | 26 | 23 | 27 |
| Missouri non-MSA | Missouri | Johnson | 19 | 2744 | 25 | 27 | 30 |
| Missouri non-MSA | Missouri | Marion | 20 | 1992 | 24 | 23 | 26 |
| Kansas City | Missouri | Platte | 17 | 1893 | 24 | 23 | 23 |
| Missouri non-MSA | Missouri | Miller | 27 | 1679 | 22 | 17 | 18 |
| Kansas City | Kansas | Miami | 3 | 1229 | 22 | 21 | 18 |
| Springfield | Missouri | Polk | 15 | 1545 | 21 | 15 | 13 |
| Missouri non-MSA | Missouri | Stoddard | 25 | 1809 | 20 | 20 | 25 |
| St. Louis-Farmington | Illinois | Bond | 12 | 1228 | 20 | 20 | 19 |
| Missouri non-MSA | Missouri | Audrain | 16 | 1251 | 20 | 18 | 17 |
| Springfield | Missouri | Webster | 28 | 1989 | 19 | 17 | 20 |
| Missouri non-MSA | Missouri | Benton | 11 | 911 | 18 | 12 | 11 |
| Kansas City | Missouri | Lafayette | 31 | 1690 | 17 | 20 | 20 |
| Missouri non-MSA | Missouri | Randolph | 9 | 1352 | 17 | 15 | 18 |
| Missouri non-MSA | Missouri | Stone | 19 | 1326 | 17 | 14 | 15 |
| Missouri non-MSA | Missouri | Morgan | 14 | 1202 | 16 | 12 | 12 |
| Kansas City | Missouri | Clinton | 48 | 1014 | 15 | 12 | 12 |
| Joplin | Missouri | Newton | 39 | 3096 | 15 | 15 | 24 |
| Missouri non-MSA | Missouri | Nodaway | 16 | 2118 | 15 | 16 | 22 |
| Missouri non-MSA | Missouri | Pike | 11 | 1042 | 14 | 14 | 18 |
| Missouri non-MSA | Missouri | Crawford | 14 | 1317 | 14 | 14 | 16 |
| Missouri non-MSA | Missouri | Adair | 3 | 1193 | 13 | 11 | 17 |
| Missouri non-MSA | Missouri | Mississippi | 7 | 984 | 13 | 12 | 15 |
| Missouri non-MSA | Missouri | Texas | 10 | 1060 | 12 | 9 | 10 |
| Kansas City | Missouri | Ray | 6 | 809 | 12 | 12 | 13 |
| Missouri non-MSA | Missouri | Washington | 27 | 1564 | 12 | 15 | 21 |
| Missouri non-MSA | Missouri | Vernon | 13 | 774 | 12 | 9 | 10 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2044 | 12 | 15 | 22 |
| Missouri non-MSA | Missouri | Barry | 31 | 1560 | 12 | 12 | 17 |
| St. Louis-Farmington | Missouri | Warren | 3 | 1327 | 12 | 14 | 19 |
| Missouri non-MSA | Missouri | Henry | 14 | 1199 | 12 | 12 | 20 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1331 | 12 | 11 | 17 |
| Columbia-Jefferson City | Missouri | Cooper | 10 | 1259 | 12 | 10 | 14 |
| Missouri non-MSA | Missouri | Saline | 14 | 1688 | 12 | 12 | 18 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1180 | 12 | 13 | 17 |
| St. Joseph | Missouri | Andrew | 12 | 911 | 11 | 11 | 12 |
| Missouri non-MSA | Missouri | Madison | 10 | 987 | 11 | 12 | 13 |
| Missouri non-MSA | Missouri | Howell | 32 | 1681 | 11 | 10 | 11 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1798 | 11 | 13 | 15 |
| Missouri non-MSA | Missouri | Perry | 13 | 1644 | 11 | 11 | 20 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1026 | 10 | 9 | 12 |
| Missouri non-MSA | Missouri | Harrison | 4 | 477 | 10 | 7 | 8 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 10 | 878 | 10 | 7 | 9 |
| St. Joseph | Kansas | Doniphan | 5 | 587 | 10 | 10 | 10 |
| Missouri non-MSA | Missouri | McDonald | 16 | 1477 | 9 | 7 | 6 |
| Kansas City | Missouri | Bates | 9 | 622 | 9 | 8 | 10 |
| Missouri non-MSA | Missouri | Gentry | 14 | 487 | 9 | 6 | 8 |
| Missouri non-MSA | Missouri | Carroll | 8 | 506 | 9 | 7 | 8 |
| Missouri non-MSA | Missouri | Pemiscot | 19 | 1164 | 8 | 9 | 11 |
| Missouri non-MSA | Missouri | Wright | 15 | 843 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Dent | 5 | 586 | 8 | 7 | 9 |
| Missouri non-MSA | Missouri | Livingston | 16 | 844 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Ralls | 2 | 542 | 7 | 7 | 9 |
| Missouri non-MSA | Missouri | New Madrid | 25 | 1431 | 7 | 11 | 16 |
| Missouri non-MSA | Missouri | Wayne | 3 | 556 | 7 | 6 | 6 |
| St. Joseph | Missouri | DeKalb | 16 | 654 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | Grundy | 14 | 558 | 6 | 5 | 7 |
| Missouri non-MSA | Missouri | Macon | 4 | 738 | 6 | 8 | 13 |
| Kansas City | Kansas | Linn | 2 | 353 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Lewis | 2 | 473 | 6 | 3 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 25 | 534 | 6 | 7 | 6 |
| Kansas City | Missouri | Caldwell | 3 | 442 | 5 | 5 | 6 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 301 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | St. Clair | 2 | 378 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Shelby | 1 | 250 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Daviess | 8 | 380 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Ripley | 8 | 577 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Barton | 6 | 666 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Iron | 1 | 269 | 4 | 3 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 541 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Douglas | 16 | 476 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 381 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Monroe | 5 | 424 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Linn | 11 | 353 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Maries | 4 | 400 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Carter | 6 | 323 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Chariton | 0 | 268 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Clark | 4 | 327 | 3 | 2 | 5 |
| Missouri non-MSA | Missouri | Holt | 5 | 292 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 361 | 3 | 2 | 2 |
| Springfield | Missouri | Dallas | 13 | 627 | 3 | 3 | 6 |
| Missouri non-MSA | Missouri | Atchison | 4 | 234 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Oregon | 2 | 406 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Ozark | 3 | 314 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 7 | 586 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Worth | 0 | 89 | 2 | 1 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 4 | 280 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 196 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 6 | 388 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dade | 8 | 307 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Cedar | 8 | 459 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | Putnam | 1 | 175 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 143 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Scotland | 1 | 202 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Mercer | 1 | 93 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 137 | 0 | 0 | 1 |
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
