# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/19/2020  
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
| St. Louis-Farmington | 2121 | 122622 | 2442 | 2238 | 1546 |
| Kansas City | 1052 | 84044 | 1452 | 1352 | 978 |
| Missouri non-MSA | 746 | 59361 | 1143 | 1060 | 807 |
| Columbia-Jefferson City | 87 | 19990 | 416 | 410 | 304 |
| Springfield | 221 | 18870 | 265 | 249 | 207 |
| Cape Girardeau-Sikeston | 101 | 7372 | 158 | 144 | 103 |
| Joplin | 139 | 9957 | 156 | 142 | 108 |
| St. Joseph | 69 | 5477 | 88 | 85 | 63 |
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
| St. Louis-Farmington | Missouri | St. Louis | 921 | 43581 | 846 | 729 | 511 |
| Kansas City | Kansas | Johnson | 252 | 22826 | 431 | 413 | 304 |
| St. Louis-Farmington | Missouri | St. Charles | 175 | 16662 | 350 | 318 | 230 |
| Kansas City | Missouri | Kansas City | 249 | 20045 | 314 | 296 | 210 |
| Kansas City | Missouri | Jackson | 165 | 14701 | 283 | 264 | 183 |
| St. Louis-Farmington | Illinois | Madison | 201 | 11826 | 267 | 265 | 167 |
| St. Louis-Farmington | Missouri | Jefferson | 96 | 8968 | 202 | 188 | 126 |
| St. Louis-Farmington | Missouri | St. Louis City | 230 | 11150 | 176 | 146 | 106 |
| St. Louis-Farmington | Illinois | St. Clair | 247 | 11018 | 174 | 171 | 115 |
| Columbia-Jefferson City | Missouri | Boone | 16 | 9029 | 172 | 171 | 113 |
| Springfield | Missouri | Greene | 162 | 12192 | 167 | 158 | 128 |
| Joplin | Missouri | Jasper | 102 | 7284 | 121 | 111 | 82 |
| Columbia-Jefferson City | Missouri | Cole | 38 | 5228 | 116 | 111 | 90 |
| Kansas City | Kansas | Wyandotte | 167 | 10235 | 105 | 92 | 73 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 59 | 4220 | 89 | 87 | 59 |
| Kansas City | Missouri | Clay | 60 | 3954 | 86 | 76 | 55 |
| St. Louis-Farmington | Missouri | St. Francois | 36 | 4323 | 85 | 79 | 56 |
| St. Louis-Farmington | Missouri | Franklin | 58 | 4067 | 73 | 71 | 57 |
| Kansas City | Missouri | Cass | 36 | 3152 | 71 | 60 | 42 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 2408 | 55 | 57 | 46 |
| St. Joseph | Missouri | Buchanan | 50 | 3970 | 53 | 56 | 40 |
| Springfield | Missouri | Christian | 20 | 3279 | 52 | 49 | 39 |
| St. Louis-Farmington | Illinois | Clinton | 55 | 2727 | 51 | 52 | 38 |
| Cape Girardeau-Sikeston | Missouri | Scott | 33 | 2205 | 50 | 41 | 31 |
| St. Louis-Farmington | Missouri | Lincoln | 8 | 1972 | 49 | 42 | 30 |
| St. Louis-Farmington | Illinois | Macoupin | 16 | 1630 | 47 | 50 | 29 |
| Kansas City | Kansas | Leavenworth | 27 | 3297 | 41 | 37 | 25 |
| St. Louis-Farmington | Illinois | Monroe | 43 | 1659 | 39 | 39 | 27 |
| Missouri non-MSA | Missouri | Taney | 37 | 2445 | 39 | 35 | 29 |
| Joplin | Missouri | Newton | 37 | 2673 | 35 | 31 | 26 |
| Missouri non-MSA | Missouri | Phelps | 38 | 1361 | 35 | 28 | 19 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1755 | 34 | 29 | 24 |
| Missouri non-MSA | Missouri | Johnson | 12 | 2165 | 34 | 35 | 25 |
| Missouri non-MSA | Missouri | Stoddard | 17 | 1363 | 34 | 27 | 20 |
| Missouri non-MSA | Missouri | Pettis | 29 | 2509 | 33 | 45 | 35 |
| Missouri non-MSA | Missouri | Henry | 9 | 878 | 33 | 28 | 17 |
| Missouri non-MSA | Missouri | Marion | 15 | 1499 | 32 | 30 | 22 |
| Missouri non-MSA | Missouri | Perry | 8 | 1336 | 32 | 30 | 19 |
| Missouri non-MSA | Missouri | Lawrence | 33 | 1679 | 31 | 30 | 23 |
| Missouri non-MSA | Missouri | Washington | 22 | 1189 | 30 | 30 | 19 |
| Missouri non-MSA | Missouri | Randolph | 5 | 1039 | 30 | 22 | 17 |
| Missouri non-MSA | Missouri | Butler | 8 | 1799 | 29 | 25 | 25 |
| Missouri non-MSA | Missouri | Camden | 44 | 2147 | 29 | 29 | 23 |
| St. Louis-Farmington | Illinois | Jersey | 23 | 1001 | 27 | 34 | 18 |
| St. Louis-Farmington | Missouri | Warren | 2 | 987 | 26 | 20 | 13 |
| Missouri non-MSA | Missouri | Saline | 12 | 1386 | 26 | 23 | 16 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 1168 | 26 | 21 | 15 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 877 | 25 | 25 | 19 |
| Missouri non-MSA | Missouri | Barry | 22 | 1276 | 24 | 22 | 18 |
| Missouri non-MSA | Missouri | Adair | 0 | 925 | 24 | 23 | 15 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1540 | 24 | 21 | 18 |
| Missouri non-MSA | Missouri | Pike | 8 | 713 | 24 | 21 | 13 |
| Springfield | Missouri | Webster | 23 | 1594 | 23 | 21 | 18 |
| Missouri non-MSA | Missouri | Crawford | 10 | 1015 | 23 | 20 | 15 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1080 | 23 | 23 | 19 |
| Kansas City | Missouri | Platte | 14 | 1402 | 23 | 21 | 16 |
| Columbia-Jefferson City | Missouri | Cooper | 6 | 1031 | 21 | 23 | 15 |
| Missouri non-MSA | Missouri | Pulaski | 14 | 1353 | 20 | 17 | 15 |
| Kansas City | Missouri | Lafayette | 28 | 1278 | 19 | 21 | 18 |
| Missouri non-MSA | Missouri | Stone | 14 | 1031 | 19 | 17 | 13 |
| Missouri non-MSA | Missouri | Miller | 23 | 1298 | 19 | 20 | 17 |
| Missouri non-MSA | Missouri | Laclede | 29 | 1574 | 17 | 19 | 16 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 664 | 17 | 12 | 9 |
| Missouri non-MSA | Missouri | Macon | 2 | 489 | 17 | 15 | 9 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 810 | 16 | 15 | 13 |
| St. Louis-Farmington | Illinois | Bond | 10 | 863 | 16 | 20 | 13 |
| Missouri non-MSA | Missouri | Audrain | 11 | 889 | 16 | 14 | 11 |
| Kansas City | Missouri | Clinton | 39 | 779 | 16 | 13 | 11 |
| Kansas City | Kansas | Miami | 2 | 823 | 15 | 14 | 10 |
| Kansas City | Missouri | Ray | 3 | 581 | 15 | 16 | 11 |
| Missouri non-MSA | Missouri | Benton | 7 | 702 | 15 | 13 | 8 |
| St. Joseph | Missouri | Andrew | 8 | 658 | 14 | 11 | 8 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 7 | 725 | 14 | 11 | 9 |
| Missouri non-MSA | Missouri | Pemiscot | 16 | 974 | 13 | 13 | 10 |
| Missouri non-MSA | Missouri | Texas | 7 | 862 | 13 | 14 | 11 |
| Missouri non-MSA | Missouri | Howell | 25 | 1476 | 13 | 11 | 15 |
| Springfield | Missouri | Polk | 11 | 1271 | 12 | 11 | 13 |
| Missouri non-MSA | Missouri | Madison | 7 | 720 | 12 | 11 | 9 |
| Missouri non-MSA | Missouri | Harrison | 1 | 329 | 12 | 8 | 5 |
| Missouri non-MSA | Missouri | Morgan | 9 | 944 | 12 | 12 | 12 |
| Missouri non-MSA | Missouri | Grundy | 12 | 430 | 12 | 9 | 6 |
| Kansas City | Missouri | Bates | 8 | 414 | 11 | 9 | 6 |
| Missouri non-MSA | Missouri | Vernon | 5 | 572 | 11 | 13 | 9 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 259 | 11 | 8 | 5 |
| Missouri non-MSA | Missouri | Dent | 4 | 402 | 11 | 8 | 5 |
| St. Joseph | Kansas | Doniphan | 2 | 363 | 10 | 9 | 6 |
| Missouri non-MSA | Missouri | Ralls | 1 | 363 | 10 | 9 | 5 |
| Kansas City | Missouri | Caldwell | 1 | 320 | 10 | 8 | 5 |
| Missouri non-MSA | Missouri | Cedar | 4 | 392 | 10 | 8 | 6 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 404 | 9 | 8 | 5 |
| St. Joseph | Missouri | DeKalb | 9 | 486 | 9 | 8 | 7 |
| Missouri non-MSA | Missouri | Ripley | 5 | 436 | 9 | 9 | 7 |
| Missouri non-MSA | Missouri | Livingston | 11 | 690 | 9 | 7 | 4 |
| Missouri non-MSA | Missouri | Barton | 4 | 573 | 9 | 8 | 5 |
| Springfield | Missouri | Dallas | 5 | 534 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Gentry | 11 | 335 | 9 | 8 | 5 |
| Missouri non-MSA | Missouri | Sullivan | 5 | 508 | 8 | 7 | 7 |
| Missouri non-MSA | Missouri | Lewis | 2 | 380 | 8 | 9 | 6 |
| Missouri non-MSA | Missouri | Chariton | 0 | 199 | 8 | 8 | 4 |
| Kansas City | Kansas | Linn | 1 | 237 | 8 | 6 | 4 |
| Missouri non-MSA | Missouri | Carroll | 4 | 337 | 7 | 7 | 5 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 188 | 7 | 6 | 3 |
| Missouri non-MSA | Missouri | Monroe | 3 | 308 | 6 | 7 | 5 |
| Missouri non-MSA | Missouri | Clark | 2 | 238 | 6 | 7 | 4 |
| Missouri non-MSA | Missouri | Dade | 5 | 252 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Linn | 10 | 264 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Wright | 11 | 705 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Atchison | 1 | 157 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 390 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Maries | 2 | 308 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Iron | 0 | 190 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Montgomery | 5 | 275 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Holt | 2 | 208 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | McDonald | 15 | 1332 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Wayne | 3 | 423 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Oregon | 0 | 333 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Scotland | 1 | 149 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Hickory | 4 | 332 | 4 | 4 | 5 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 222 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Carter | 4 | 244 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Knox | 1 | 118 | 4 | 3 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 169 | 3 | 4 | 2 |
| Missouri non-MSA | Missouri | Daviess | 6 | 294 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Putnam | 1 | 103 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 146 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Douglas | 14 | 367 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 112 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Shannon | 10 | 319 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Ozark | 1 | 264 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 53 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 63 | 1 | 1 | 1 |
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
