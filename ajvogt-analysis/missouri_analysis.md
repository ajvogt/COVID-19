# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/25/2020  
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
| St. Louis-Farmington | 2264 | 136334 | 2299 | 2357 | 1853 |
| Kansas City | 1140 | 91772 | 1431 | 1427 | 1133 |
| Missouri non-MSA | 819 | 65346 | 973 | 1050 | 900 |
| Columbia-Jefferson City | 107 | 21875 | 327 | 369 | 330 |
| Springfield | 237 | 20366 | 249 | 259 | 228 |
| Cape Girardeau-Sikeston | 111 | 8229 | 147 | 154 | 121 |
| Joplin | 144 | 10770 | 142 | 151 | 120 |
| St. Joseph | 77 | 6130 | 105 | 98 | 75 |
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
| St. Louis-Farmington | Missouri | St. Louis | 965 | 47884 | 720 | 776 | 609 |
| Kansas City | Kansas | Johnson | 283 | 25025 | 434 | 445 | 348 |
| St. Louis-Farmington | Missouri | St. Charles | 202 | 18651 | 339 | 341 | 269 |
| Kansas City | Missouri | Kansas City | 269 | 21884 | 319 | 308 | 255 |
| St. Louis-Farmington | Illinois | Madison | 229 | 13291 | 255 | 263 | 204 |
| Kansas City | Missouri | Jackson | 175 | 16106 | 246 | 258 | 208 |
| St. Louis-Farmington | Illinois | St. Clair | 255 | 12340 | 208 | 196 | 147 |
| St. Louis-Farmington | Missouri | Jefferson | 103 | 10106 | 189 | 196 | 154 |
| St. Louis-Farmington | Missouri | St. Louis City | 235 | 12114 | 163 | 156 | 126 |
| Springfield | Missouri | Greene | 169 | 13160 | 161 | 165 | 143 |
| Kansas City | Kansas | Wyandotte | 177 | 10924 | 137 | 117 | 84 |
| Columbia-Jefferson City | Missouri | Boone | 23 | 9772 | 135 | 153 | 127 |
| Joplin | Missouri | Jasper | 106 | 7889 | 107 | 115 | 91 |
| Columbia-Jefferson City | Missouri | Cole | 49 | 5837 | 99 | 107 | 97 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 64 | 4713 | 84 | 89 | 69 |
| St. Louis-Farmington | Missouri | St. Francois | 43 | 4795 | 78 | 80 | 66 |
| Kansas City | Missouri | Clay | 64 | 4325 | 71 | 73 | 61 |
| St. Joseph | Missouri | Buchanan | 56 | 4394 | 68 | 62 | 48 |
| St. Louis-Farmington | Missouri | Franklin | 71 | 4507 | 67 | 73 | 63 |
| Kansas City | Missouri | Cass | 39 | 3525 | 63 | 65 | 50 |
| St. Louis-Farmington | Illinois | Macoupin | 17 | 1988 | 59 | 55 | 39 |
| St. Louis-Farmington | Illinois | Clinton | 56 | 3035 | 55 | 52 | 42 |
| Cape Girardeau-Sikeston | Missouri | Scott | 37 | 2489 | 50 | 48 | 36 |
| Springfield | Missouri | Christian | 23 | 3565 | 47 | 49 | 44 |
| St. Louis-Farmington | Missouri | Lincoln | 9 | 2254 | 46 | 47 | 36 |
| St. Louis-Farmington | Illinois | Monroe | 44 | 1931 | 42 | 42 | 33 |
| Columbia-Jefferson City | Missouri | Callaway | 8 | 2637 | 42 | 47 | 48 |
| Kansas City | Kansas | Leavenworth | 29 | 3503 | 42 | 42 | 29 |
| Missouri non-MSA | Missouri | Taney | 40 | 2685 | 38 | 38 | 33 |
| Missouri non-MSA | Missouri | Phelps | 40 | 1600 | 38 | 35 | 25 |
| Joplin | Missouri | Newton | 38 | 2881 | 35 | 35 | 29 |
| Missouri non-MSA | Missouri | Butler | 9 | 2009 | 34 | 30 | 29 |
| Missouri non-MSA | Missouri | Johnson | 15 | 2353 | 31 | 34 | 29 |
| Missouri non-MSA | Missouri | Camden | 45 | 2342 | 31 | 31 | 25 |
| Missouri non-MSA | Missouri | Marion | 16 | 1662 | 29 | 29 | 25 |
| Missouri non-MSA | Missouri | Stoddard | 20 | 1518 | 28 | 30 | 21 |
| Kansas City | Missouri | Platte | 14 | 1559 | 27 | 24 | 19 |
| Springfield | Missouri | Webster | 24 | 1741 | 26 | 24 | 20 |
| St. Louis-Farmington | Illinois | Jersey | 23 | 1149 | 26 | 25 | 22 |
| Missouri non-MSA | Missouri | Washington | 23 | 1353 | 25 | 27 | 23 |
| Missouri non-MSA | Missouri | Pulaski | 17 | 1509 | 24 | 21 | 18 |
| St. Louis-Farmington | Missouri | Warren | 2 | 1128 | 24 | 24 | 17 |
| Missouri non-MSA | Missouri | Lawrence | 37 | 1822 | 23 | 27 | 24 |
| Missouri non-MSA | Missouri | Perry | 12 | 1484 | 22 | 27 | 22 |
| Missouri non-MSA | Missouri | Henry | 10 | 1020 | 22 | 27 | 21 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 807 | 21 | 20 | 12 |
| Missouri non-MSA | Missouri | Laclede | 30 | 1703 | 21 | 19 | 17 |
| Kansas City | Missouri | Lafayette | 29 | 1410 | 21 | 21 | 20 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1888 | 21 | 28 | 25 |
| Missouri non-MSA | Missouri | Pike | 8 | 841 | 21 | 21 | 16 |
| Missouri non-MSA | Missouri | Miller | 24 | 1429 | 20 | 20 | 19 |
| Missouri non-MSA | Missouri | Macon | 3 | 618 | 20 | 19 | 13 |
| Missouri non-MSA | Missouri | Saline | 12 | 1510 | 19 | 22 | 19 |
| Kansas City | Kansas | Miami | 2 | 923 | 19 | 17 | 12 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 996 | 19 | 22 | 20 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 1270 | 18 | 21 | 16 |
| Missouri non-MSA | Missouri | Adair | 3 | 1032 | 18 | 21 | 17 |
| Missouri non-MSA | Missouri | Barry | 23 | 1389 | 17 | 21 | 19 |
| Missouri non-MSA | Missouri | Randolph | 5 | 1130 | 16 | 22 | 17 |
| Missouri non-MSA | Missouri | Crawford | 12 | 1117 | 16 | 19 | 16 |
| Missouri non-MSA | Missouri | Audrain | 12 | 990 | 16 | 16 | 13 |
| St. Joseph | Missouri | Andrew | 9 | 753 | 15 | 14 | 10 |
| Missouri non-MSA | Missouri | Stone | 15 | 1126 | 15 | 17 | 14 |
| Columbia-Jefferson City | Missouri | Cooper | 7 | 1115 | 14 | 18 | 16 |
| Missouri non-MSA | Missouri | Madison | 7 | 817 | 14 | 13 | 11 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1164 | 14 | 19 | 18 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1608 | 14 | 17 | 16 |
| St. Louis-Farmington | Illinois | Bond | 10 | 936 | 13 | 15 | 14 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 896 | 13 | 15 | 14 |
| Kansas City | Missouri | Bates | 9 | 499 | 13 | 12 | 8 |
| St. Joseph | Kansas | Doniphan | 2 | 434 | 12 | 11 | 7 |
| Missouri non-MSA | Missouri | Pettis | 32 | 2590 | 12 | 23 | 33 |
| Missouri non-MSA | Missouri | Ralls | 1 | 434 | 12 | 11 | 7 |
| Missouri non-MSA | Missouri | Morgan | 12 | 1021 | 12 | 12 | 12 |
| Missouri non-MSA | Missouri | Dent | 4 | 478 | 11 | 10 | 7 |
| Missouri non-MSA | Missouri | Howell | 26 | 1540 | 10 | 11 | 13 |
| Missouri non-MSA | Missouri | Carroll | 5 | 403 | 10 | 8 | 7 |
| Kansas City | Missouri | Ray | 4 | 638 | 10 | 13 | 12 |
| Missouri non-MSA | Missouri | Vernon | 6 | 636 | 9 | 10 | 10 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 8 | 779 | 9 | 11 | 10 |
| Kansas City | Missouri | Clinton | 44 | 833 | 9 | 12 | 11 |
| St. Joseph | Missouri | DeKalb | 10 | 549 | 9 | 9 | 8 |
| Missouri non-MSA | Missouri | Texas | 7 | 922 | 9 | 11 | 11 |
| Missouri non-MSA | Missouri | Pemiscot | 16 | 1027 | 8 | 11 | 10 |
| Missouri non-MSA | Missouri | Gentry | 11 | 394 | 8 | 8 | 7 |
| Missouri non-MSA | Missouri | Grundy | 14 | 481 | 8 | 10 | 7 |
| Missouri non-MSA | Missouri | Livingston | 13 | 746 | 8 | 8 | 6 |
| Kansas City | Missouri | Caldwell | 1 | 360 | 8 | 8 | 6 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 225 | 8 | 7 | 5 |
| Springfield | Missouri | Polk | 12 | 1322 | 8 | 11 | 13 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 454 | 8 | 9 | 7 |
| Missouri non-MSA | Missouri | Monroe | 3 | 352 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Wayne | 3 | 466 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Clark | 3 | 287 | 7 | 7 | 5 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 305 | 7 | 8 | 6 |
| Missouri non-MSA | Missouri | Holt | 3 | 256 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Harrison | 2 | 377 | 7 | 9 | 6 |
| Missouri non-MSA | Missouri | McDonald | 16 | 1377 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Ripley | 5 | 480 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Lewis | 2 | 423 | 7 | 7 | 7 |
| Springfield | Missouri | Dallas | 9 | 578 | 6 | 8 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 436 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Sullivan | 6 | 546 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Iron | 0 | 223 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Cedar | 6 | 430 | 6 | 8 | 6 |
| Missouri non-MSA | Missouri | Linn | 10 | 297 | 5 | 5 | 4 |
| Kansas City | Kansas | Linn | 1 | 258 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Maries | 3 | 344 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Wright | 14 | 742 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Barton | 4 | 610 | 5 | 7 | 6 |
| Missouri non-MSA | Missouri | Atchison | 1 | 196 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Benton | 8 | 735 | 5 | 10 | 8 |
| Missouri non-MSA | Missouri | Montgomery | 5 | 309 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Carter | 5 | 278 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Chariton | 0 | 224 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Dade | 6 | 278 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Scotland | 1 | 177 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Douglas | 15 | 394 | 4 | 3 | 3 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 248 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Oregon | 0 | 356 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Putnam | 1 | 126 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 186 | 3 | 4 | 2 |
| Missouri non-MSA | Missouri | Daviess | 8 | 315 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Hickory | 6 | 352 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Ozark | 2 | 278 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Mercer | 0 | 79 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 159 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Knox | 1 | 132 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 67 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 330 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 124 | 2 | 2 | 2 |
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
