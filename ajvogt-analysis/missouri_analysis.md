# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/25/2020  
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
| St. Louis-Farmington | 3183 | 192765 | 1626 | 1754 | 1881 |
| Kansas City | 1516 | 128636 | 1182 | 1190 | 1228 |
| Missouri non-MSA | 1310 | 88622 | 666 | 729 | 775 |
| Springfield | 373 | 27901 | 232 | 258 | 251 |
| Columbia-Jefferson City | 193 | 28450 | 194 | 193 | 219 |
| Joplin | 197 | 12986 | 73 | 66 | 73 |
| Cape Girardeau-Sikeston | 170 | 10707 | 60 | 64 | 82 |
| St. Joseph | 127 | 8297 | 49 | 53 | 72 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1334 | 66284 | 536 | 577 | 613 |
| Kansas City | Kansas | Johnson | 413 | 36727 | 394 | 398 | 390 |
| St. Louis-Farmington | Missouri | St. Charles | 276 | 26110 | 233 | 235 | 248 |
| St. Louis-Farmington | Illinois | Madison | 372 | 20065 | 194 | 217 | 225 |
| Kansas City | Missouri | Kansas City | 348 | 28800 | 193 | 201 | 230 |
| Kansas City | Missouri | Jackson | 230 | 22368 | 183 | 184 | 208 |
| Springfield | Missouri | Greene | 251 | 17962 | 148 | 165 | 160 |
| Kansas City | Kansas | Wyandotte | 193 | 14857 | 146 | 148 | 131 |
| St. Louis-Farmington | Illinois | St. Clair | 326 | 18048 | 137 | 164 | 190 |
| St. Louis-Farmington | Missouri | St. Louis City | 291 | 16382 | 130 | 136 | 142 |
| St. Louis-Farmington | Missouri | Jefferson | 126 | 14413 | 116 | 124 | 143 |
| Columbia-Jefferson City | Missouri | Boone | 42 | 12872 | 99 | 101 | 103 |
| Kansas City | Missouri | Cass | 52 | 5259 | 55 | 57 | 57 |
| St. Louis-Farmington | Missouri | Franklin | 109 | 6233 | 54 | 55 | 57 |
| Springfield | Missouri | Christian | 45 | 5210 | 52 | 58 | 54 |
| Joplin | Missouri | Jasper | 154 | 9634 | 52 | 50 | 58 |
| Kansas City | Missouri | Clay | 93 | 5951 | 48 | 49 | 54 |
| St. Louis-Farmington | Missouri | St. Francois | 68 | 6245 | 47 | 50 | 48 |
| Missouri non-MSA | Missouri | Pulaski | 27 | 2481 | 39 | 30 | 32 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 94 | 6209 | 39 | 42 | 49 |
| Kansas City | Kansas | Leavenworth | 38 | 4823 | 38 | 39 | 44 |
| Columbia-Jefferson City | Missouri | Cole | 85 | 7351 | 37 | 37 | 50 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3388 | 34 | 37 | 37 |
| St. Louis-Farmington | Illinois | Clinton | 79 | 4307 | 33 | 36 | 42 |
| St. Louis-Farmington | Illinois | Monroe | 56 | 2928 | 33 | 34 | 33 |
| St. Joseph | Missouri | Buchanan | 91 | 5848 | 28 | 33 | 48 |
| Columbia-Jefferson City | Missouri | Callaway | 19 | 3596 | 27 | 26 | 31 |
| Kansas City | Kansas | Miami | 10 | 1648 | 27 | 25 | 24 |
| St. Louis-Farmington | Illinois | Macoupin | 63 | 3102 | 26 | 30 | 37 |
| Kansas City | Missouri | Platte | 20 | 2231 | 23 | 21 | 22 |
| Missouri non-MSA | Missouri | Phelps | 82 | 2355 | 22 | 20 | 25 |
| Missouri non-MSA | Missouri | Johnson | 28 | 3118 | 22 | 22 | 25 |
| Missouri non-MSA | Missouri | Pettis | 60 | 3873 | 22 | 42 | 42 |
| Missouri non-MSA | Missouri | Taney | 51 | 3642 | 22 | 25 | 31 |
| Missouri non-MSA | Missouri | Audrain | 31 | 1556 | 21 | 18 | 18 |
| Joplin | Missouri | Newton | 43 | 3352 | 21 | 16 | 15 |
| Kansas City | Missouri | Lafayette | 38 | 1970 | 21 | 17 | 18 |
| Missouri non-MSA | Missouri | Camden | 60 | 3008 | 21 | 19 | 22 |
| St. Louis-Farmington | Illinois | Jersey | 35 | 1861 | 19 | 20 | 23 |
| Missouri non-MSA | Missouri | Laclede | 44 | 2416 | 19 | 22 | 23 |
| Springfield | Missouri | Webster | 38 | 2306 | 19 | 19 | 18 |
| Missouri non-MSA | Missouri | Howell | 36 | 2229 | 18 | 37 | 22 |
| Missouri non-MSA | Missouri | Crawford | 19 | 1588 | 18 | 17 | 15 |
| Missouri non-MSA | Missouri | Adair | 4 | 1512 | 18 | 19 | 16 |
| Cape Girardeau-Sikeston | Missouri | Scott | 59 | 3229 | 16 | 16 | 24 |
| Kansas City | Missouri | Ray | 8 | 1047 | 16 | 15 | 13 |
| Missouri non-MSA | Missouri | Saline | 21 | 1940 | 16 | 15 | 14 |
| Missouri non-MSA | Missouri | Miller | 42 | 1959 | 15 | 17 | 17 |
| Missouri non-MSA | Missouri | Texas | 16 | 1282 | 15 | 14 | 12 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1565 | 15 | 15 | 14 |
| Missouri non-MSA | Missouri | Butler | 14 | 2721 | 14 | 18 | 23 |
| Missouri non-MSA | Missouri | Henry | 21 | 1388 | 14 | 11 | 12 |
| Missouri non-MSA | Missouri | Marion | 24 | 2251 | 13 | 13 | 19 |
| St. Louis-Farmington | Illinois | Bond | 16 | 1480 | 12 | 14 | 18 |
| Missouri non-MSA | Missouri | Lawrence | 47 | 2241 | 12 | 12 | 13 |
| Missouri non-MSA | Missouri | Stone | 24 | 1545 | 12 | 13 | 13 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1451 | 11 | 11 | 11 |
| Missouri non-MSA | Missouri | Pike | 14 | 1226 | 11 | 10 | 12 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 3 | 1363 | 11 | 11 | 12 |
| Missouri non-MSA | Missouri | Randolph | 15 | 1546 | 11 | 12 | 13 |
| Missouri non-MSA | Missouri | Washington | 36 | 1714 | 10 | 9 | 12 |
| Kansas City | Missouri | Clinton | 56 | 1195 | 10 | 11 | 12 |
| Missouri non-MSA | Missouri | Barry | 35 | 1741 | 10 | 10 | 11 |
| Missouri non-MSA | Missouri | Vernon | 16 | 929 | 10 | 10 | 9 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1605 | 10 | 8 | 7 |
| Springfield | Missouri | Polk | 21 | 1746 | 9 | 11 | 14 |
| St. Joseph | Kansas | Doniphan | 5 | 673 | 9 | 6 | 7 |
| Kansas City | Missouri | Bates | 10 | 763 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2286 | 8 | 8 | 13 |
| Missouri non-MSA | Missouri | Dunklin | 15 | 2023 | 8 | 14 | 13 |
| Missouri non-MSA | Missouri | Wright | 23 | 994 | 8 | 10 | 8 |
| Missouri non-MSA | Missouri | Livingston | 21 | 983 | 8 | 9 | 7 |
| Missouri non-MSA | Missouri | Carroll | 14 | 631 | 8 | 8 | 7 |
| St. Joseph | Missouri | Andrew | 13 | 1043 | 8 | 8 | 9 |
| Columbia-Jefferson City | Missouri | Moniteau | 17 | 1446 | 8 | 7 | 9 |
| Missouri non-MSA | Missouri | Madison | 10 | 1129 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | New Madrid | 29 | 1562 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | Morgan | 21 | 1398 | 7 | 11 | 12 |
| Kansas City | Kansas | Linn | 3 | 475 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Macon | 8 | 880 | 7 | 8 | 8 |
| Missouri non-MSA | Missouri | Iron | 1 | 374 | 7 | 7 | 5 |
| Missouri non-MSA | Missouri | Perry | 19 | 1800 | 7 | 9 | 10 |
| Missouri non-MSA | Missouri | Benton | 16 | 1152 | 7 | 11 | 13 |
| Missouri non-MSA | Missouri | Douglas | 19 | 590 | 6 | 7 | 6 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1133 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 29 | 645 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Stoddard | 32 | 1971 | 6 | 10 | 15 |
| Missouri non-MSA | Missouri | Harrison | 7 | 594 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Ralls | 6 | 628 | 6 | 5 | 6 |
| Kansas City | Missouri | Caldwell | 4 | 522 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Mississippi | 11 | 1103 | 5 | 7 | 9 |
| Missouri non-MSA | Missouri | Wayne | 6 | 640 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Grundy | 22 | 648 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Gentry | 16 | 580 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Pemiscot | 20 | 1254 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Montgomery | 8 | 468 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Dent | 7 | 670 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 638 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 9 | 453 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Oregon | 3 | 513 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Monroe | 5 | 492 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Chariton | 2 | 314 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 4 | 428 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Dade | 8 | 356 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 601 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Barton | 9 | 738 | 3 | 4 | 4 |
| St. Joseph | Missouri | DeKalb | 18 | 733 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Maries | 6 | 446 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Lewis | 3 | 514 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Clark | 4 | 360 | 2 | 1 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 11 | 938 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Ripley | 8 | 642 | 2 | 4 | 5 |
| Springfield | Missouri | Dallas | 18 | 677 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Cedar | 8 | 491 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shannon | 9 | 402 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 3 | 282 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Carter | 6 | 364 | 1 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 6 | 331 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Ozark | 4 | 361 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 187 | 1 | 3 | 2 |
| Missouri non-MSA | Missouri | Linn | 11 | 401 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Putnam | 1 | 194 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Scotland | 3 | 224 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 9 | 415 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 124 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 218 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 319 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Worth | 1 | 111 | 0 | 1 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 3 | 354 | 0 | 2 | 4 |
| Missouri non-MSA | Missouri | Knox | 1 | 147 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 5 | 256 | 0 | 0 | 2 |
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
