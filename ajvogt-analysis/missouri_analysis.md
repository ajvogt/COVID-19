# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/07/2020  
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
| St. Louis-Farmington | 2578 | 161075 | 2051 | 2087 | 2188 |
| Kansas City | 1251 | 106499 | 1274 | 1255 | 1296 |
| Missouri non-MSA | 940 | 75282 | 888 | 825 | 955 |
| Springfield | 288 | 23305 | 275 | 242 | 250 |
| Columbia-Jefferson City | 126 | 24941 | 261 | 254 | 323 |
| Cape Girardeau-Sikeston | 122 | 9524 | 111 | 107 | 131 |
| St. Joseph | 94 | 7203 | 95 | 94 | 93 |
| Joplin | 162 | 11745 | 78 | 79 | 118 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1098 | 55883 | 651 | 680 | 709 |
| Kansas City | Kansas | Johnson | 309 | 29272 | 363 | 384 | 380 |
| St. Louis-Farmington | Missouri | St. Charles | 219 | 21943 | 282 | 276 | 307 |
| Kansas City | Missouri | Kansas City | 304 | 25124 | 273 | 264 | 290 |
| Kansas City | Missouri | Jackson | 190 | 18944 | 258 | 232 | 248 |
| St. Louis-Farmington | Illinois | Madison | 285 | 16167 | 255 | 235 | 246 |
| St. Louis-Farmington | Illinois | St. Clair | 279 | 14887 | 211 | 212 | 198 |
| Springfield | Missouri | Greene | 212 | 15045 | 174 | 156 | 159 |
| St. Louis-Farmington | Missouri | Jefferson | 108 | 12170 | 170 | 174 | 184 |
| St. Louis-Farmington | Missouri | St. Louis City | 257 | 13963 | 143 | 158 | 153 |
| Columbia-Jefferson City | Missouri | Boone | 25 | 11046 | 105 | 99 | 132 |
| Kansas City | Kansas | Wyandotte | 184 | 12096 | 97 | 111 | 99 |
| Columbia-Jefferson City | Missouri | Cole | 60 | 6674 | 74 | 75 | 91 |
| St. Joseph | Missouri | Buchanan | 66 | 5128 | 69 | 62 | 62 |
| Kansas City | Missouri | Clay | 76 | 5045 | 66 | 52 | 66 |
| Joplin | Missouri | Jasper | 124 | 8677 | 64 | 62 | 92 |
| Kansas City | Missouri | Cass | 40 | 4215 | 64 | 58 | 60 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 66 | 5465 | 61 | 61 | 77 |
| St. Louis-Farmington | Missouri | Franklin | 91 | 5221 | 60 | 60 | 68 |
| Springfield | Missouri | Christian | 24 | 4172 | 59 | 48 | 50 |
| Missouri non-MSA | Missouri | Pulaski | 24 | 1941 | 46 | 33 | 26 |
| St. Louis-Farmington | Missouri | St. Francois | 47 | 5381 | 45 | 50 | 67 |
| St. Louis-Farmington | Illinois | Clinton | 65 | 3617 | 44 | 48 | 50 |
| Missouri non-MSA | Missouri | Taney | 39 | 3148 | 43 | 37 | 38 |
| Missouri non-MSA | Missouri | Pettis | 36 | 2970 | 41 | 28 | 30 |
| Columbia-Jefferson City | Missouri | Callaway | 11 | 3110 | 41 | 39 | 45 |
| St. Louis-Farmington | Illinois | Macoupin | 27 | 2518 | 40 | 44 | 49 |
| St. Louis-Farmington | Missouri | Lincoln | 13 | 2723 | 40 | 40 | 43 |
| Kansas City | Kansas | Leavenworth | 32 | 4001 | 38 | 42 | 39 |
| Cape Girardeau-Sikeston | Missouri | Scott | 42 | 2914 | 37 | 35 | 40 |
| St. Louis-Farmington | Illinois | Monroe | 48 | 2337 | 37 | 38 | 38 |
| Missouri non-MSA | Missouri | Butler | 9 | 2359 | 31 | 28 | 29 |
| Missouri non-MSA | Missouri | Phelps | 50 | 1982 | 30 | 31 | 32 |
| Missouri non-MSA | Missouri | Laclede | 33 | 2010 | 29 | 24 | 22 |
| Kansas City | Missouri | Platte | 17 | 1856 | 28 | 24 | 23 |
| St. Louis-Farmington | Illinois | Jersey | 25 | 1472 | 28 | 26 | 25 |
| Missouri non-MSA | Missouri | Marion | 18 | 1957 | 26 | 24 | 27 |
| Missouri non-MSA | Missouri | Camden | 49 | 2626 | 25 | 23 | 27 |
| Missouri non-MSA | Missouri | Johnson | 16 | 2697 | 23 | 26 | 31 |
| Missouri non-MSA | Missouri | Miller | 26 | 1653 | 23 | 17 | 19 |
| Missouri non-MSA | Missouri | Stoddard | 24 | 1783 | 22 | 22 | 25 |
| St. Louis-Farmington | Illinois | Bond | 12 | 1192 | 20 | 19 | 18 |
| Missouri non-MSA | Missouri | Randolph | 9 | 1334 | 19 | 15 | 19 |
| Springfield | Missouri | Polk | 15 | 1513 | 19 | 14 | 13 |
| Missouri non-MSA | Missouri | Audrain | 15 | 1222 | 19 | 19 | 17 |
| Kansas City | Kansas | Miami | 3 | 1143 | 18 | 19 | 16 |
| Kansas City | Missouri | Lafayette | 30 | 1657 | 18 | 20 | 21 |
| Springfield | Missouri | Webster | 27 | 1949 | 18 | 17 | 20 |
| Missouri non-MSA | Missouri | Stone | 19 | 1297 | 17 | 13 | 15 |
| Missouri non-MSA | Missouri | Washington | 27 | 1540 | 17 | 15 | 24 |
| Missouri non-MSA | Missouri | Nodaway | 14 | 2107 | 16 | 18 | 23 |
| Missouri non-MSA | Missouri | Pike | 10 | 1029 | 16 | 15 | 19 |
| Missouri non-MSA | Missouri | Lawrence | 39 | 2019 | 16 | 16 | 23 |
| Missouri non-MSA | Missouri | Benton | 11 | 885 | 16 | 11 | 11 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1169 | 15 | 15 | 19 |
| Missouri non-MSA | Missouri | Mississippi | 7 | 976 | 15 | 19 | 15 |
| Missouri non-MSA | Missouri | Morgan | 13 | 1174 | 15 | 12 | 12 |
| Missouri non-MSA | Missouri | Crawford | 14 | 1294 | 14 | 14 | 17 |
| Missouri non-MSA | Missouri | Henry | 12 | 1187 | 14 | 14 | 22 |
| Kansas City | Missouri | Clinton | 47 | 984 | 14 | 11 | 12 |
| Missouri non-MSA | Missouri | Barry | 29 | 1538 | 14 | 12 | 18 |
| Missouri non-MSA | Missouri | Perry | 12 | 1632 | 13 | 14 | 21 |
| Kansas City | Missouri | Ray | 6 | 789 | 13 | 11 | 13 |
| Joplin | Missouri | Newton | 38 | 3068 | 13 | 16 | 25 |
| Missouri non-MSA | Missouri | Adair | 3 | 1168 | 13 | 11 | 17 |
| St. Louis-Farmington | Missouri | Warren | 3 | 1309 | 13 | 16 | 19 |
| Missouri non-MSA | Missouri | Vernon | 10 | 757 | 13 | 9 | 11 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1316 | 13 | 12 | 17 |
| Missouri non-MSA | Missouri | Texas | 10 | 1048 | 12 | 10 | 11 |
| St. Joseph | Missouri | Andrew | 11 | 888 | 12 | 11 | 12 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1777 | 12 | 13 | 16 |
| Columbia-Jefferson City | Missouri | Cooper | 9 | 1247 | 11 | 10 | 15 |
| Missouri non-MSA | Missouri | Saline | 12 | 1662 | 11 | 13 | 18 |
| Missouri non-MSA | Missouri | Howell | 31 | 1661 | 11 | 10 | 11 |
| Columbia-Jefferson City | Missouri | Osage | 4 | 1011 | 10 | 10 | 12 |
| Missouri non-MSA | Missouri | Madison | 9 | 960 | 10 | 12 | 13 |
| Missouri non-MSA | Missouri | Pemiscot | 19 | 1151 | 10 | 9 | 11 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 10 | 869 | 9 | 7 | 9 |
| Missouri non-MSA | Missouri | Wright | 15 | 828 | 8 | 7 | 6 |
| Missouri non-MSA | Missouri | Dent | 4 | 576 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Ripley | 8 | 571 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Harrison | 3 | 453 | 8 | 6 | 8 |
| Missouri non-MSA | Missouri | Carroll | 7 | 490 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Macon | 3 | 734 | 8 | 10 | 14 |
| Missouri non-MSA | Missouri | New Madrid | 24 | 1417 | 8 | 12 | 17 |
| Missouri non-MSA | Missouri | Gentry | 13 | 471 | 8 | 6 | 8 |
| Missouri non-MSA | Missouri | Ralls | 2 | 525 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | Gasconade | 25 | 526 | 7 | 8 | 6 |
| Kansas City | Missouri | Bates | 9 | 603 | 7 | 9 | 10 |
| St. Joseph | Missouri | DeKalb | 15 | 640 | 7 | 9 | 8 |
| Missouri non-MSA | Missouri | McDonald | 16 | 1453 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Livingston | 16 | 831 | 6 | 6 | 7 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 292 | 6 | 5 | 5 |
| St. Joseph | Kansas | Doniphan | 2 | 547 | 6 | 11 | 10 |
| Missouri non-MSA | Missouri | Wayne | 3 | 534 | 6 | 5 | 6 |
| Kansas City | Kansas | Linn | 1 | 337 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Shelby | 1 | 246 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Daviess | 8 | 374 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Grundy | 14 | 548 | 5 | 4 | 7 |
| Kansas City | Missouri | Caldwell | 3 | 433 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 373 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Lewis | 2 | 464 | 5 | 3 | 6 |
| Missouri non-MSA | Missouri | Maries | 4 | 396 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Douglas | 15 | 466 | 4 | 5 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 537 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Barton | 5 | 659 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Oregon | 2 | 402 | 4 | 3 | 4 |
| Springfield | Missouri | Dallas | 10 | 626 | 4 | 4 | 6 |
| Missouri non-MSA | Missouri | Carter | 6 | 321 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Linn | 11 | 346 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Clark | 4 | 324 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Chariton | 0 | 264 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Monroe | 3 | 414 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Iron | 1 | 258 | 3 | 2 | 4 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 369 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Holt | 4 | 288 | 3 | 3 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 4 | 276 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dade | 8 | 305 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Scotland | 1 | 201 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Putnam | 1 | 175 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Hickory | 6 | 384 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Atchison | 3 | 228 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 196 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 3 | 311 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 88 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Cedar | 7 | 456 | 2 | 2 | 6 |
| Missouri non-MSA | Missouri | Shannon | 9 | 354 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 6 | 579 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 142 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 92 | 1 | 1 | 1 |
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
