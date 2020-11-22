# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/22/2020  
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
| St. Louis-Farmington | 2178 | 129614 | 2260 | 2293 | 1715 |
| Kansas City | 1099 | 88086 | 1360 | 1414 | 1063 |
| Missouri non-MSA | 761 | 62894 | 932 | 1077 | 881 |
| Columbia-Jefferson City | 88 | 21046 | 295 | 376 | 325 |
| Springfield | 230 | 19672 | 236 | 257 | 220 |
| Cape Girardeau-Sikeston | 104 | 7906 | 142 | 156 | 115 |
| Joplin | 141 | 10495 | 130 | 152 | 119 |
| St. Joseph | 72 | 5749 | 78 | 91 | 68 |
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
| St. Louis-Farmington | Missouri | St. Louis | 944 | 45635 | 753 | 744 | 559 |
| Kansas City | Kansas | Johnson | 271 | 23891 | 420 | 430 | 324 |
| St. Louis-Farmington | Missouri | St. Charles | 186 | 17715 | 312 | 331 | 255 |
| Kansas City | Missouri | Kansas City | 255 | 21042 | 279 | 314 | 237 |
| St. Louis-Farmington | Illinois | Madison | 216 | 12653 | 268 | 262 | 189 |
| Kansas City | Missouri | Jackson | 171 | 15478 | 247 | 266 | 197 |
| St. Louis-Farmington | Illinois | St. Clair | 251 | 11679 | 195 | 184 | 130 |
| St. Louis-Farmington | Missouri | Jefferson | 96 | 9555 | 189 | 195 | 142 |
| Springfield | Missouri | Greene | 169 | 12699 | 149 | 162 | 136 |
| St. Louis-Farmington | Missouri | St. Louis City | 230 | 11550 | 137 | 148 | 114 |
| Columbia-Jefferson City | Missouri | Boone | 17 | 9516 | 123 | 158 | 124 |
| Kansas City | Kansas | Wyandotte | 177 | 10535 | 120 | 100 | 77 |
| Joplin | Missouri | Jasper | 104 | 7699 | 100 | 118 | 91 |
| Columbia-Jefferson City | Missouri | Cole | 38 | 5523 | 85 | 104 | 95 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 59 | 4523 | 80 | 93 | 66 |
| Kansas City | Missouri | Clay | 61 | 4213 | 80 | 79 | 60 |
| St. Louis-Farmington | Missouri | St. Francois | 36 | 4597 | 72 | 82 | 63 |
| St. Louis-Farmington | Missouri | Franklin | 59 | 4330 | 70 | 75 | 63 |
| Kansas City | Missouri | Cass | 36 | 3338 | 61 | 65 | 46 |
| St. Louis-Farmington | Illinois | Macoupin | 17 | 1874 | 59 | 58 | 37 |
| St. Louis-Farmington | Illinois | Clinton | 56 | 2910 | 56 | 54 | 40 |
| St. Joseph | Missouri | Buchanan | 53 | 4151 | 49 | 60 | 44 |
| Cape Girardeau-Sikeston | Missouri | Scott | 36 | 2382 | 48 | 47 | 34 |
| Springfield | Missouri | Christian | 22 | 3444 | 47 | 51 | 43 |
| Kansas City | Kansas | Leavenworth | 27 | 3408 | 44 | 41 | 27 |
| St. Louis-Farmington | Missouri | Lincoln | 8 | 2114 | 42 | 45 | 34 |
| Columbia-Jefferson City | Missouri | Callaway | 7 | 2520 | 38 | 49 | 47 |
| Missouri non-MSA | Missouri | Taney | 37 | 2562 | 36 | 36 | 31 |
| Missouri non-MSA | Missouri | Stoddard | 19 | 1459 | 33 | 30 | 21 |
| St. Louis-Farmington | Illinois | Monroe | 44 | 1748 | 32 | 36 | 28 |
| Missouri non-MSA | Missouri | Johnson | 12 | 2301 | 32 | 35 | 29 |
| Missouri non-MSA | Missouri | Phelps | 38 | 1508 | 31 | 34 | 24 |
| Missouri non-MSA | Missouri | Butler | 8 | 1934 | 30 | 31 | 28 |
| Joplin | Missouri | Newton | 37 | 2796 | 29 | 33 | 28 |
| Missouri non-MSA | Missouri | Camden | 44 | 2281 | 29 | 33 | 25 |
| Missouri non-MSA | Missouri | Marion | 15 | 1593 | 28 | 32 | 24 |
| Missouri non-MSA | Missouri | Nodaway | 11 | 1826 | 27 | 26 | 25 |
| Missouri non-MSA | Missouri | Lawrence | 33 | 1772 | 26 | 30 | 25 |
| St. Louis-Farmington | Illinois | Jersey | 23 | 1078 | 25 | 25 | 20 |
| Missouri non-MSA | Missouri | Henry | 9 | 964 | 24 | 28 | 20 |
| Springfield | Missouri | Webster | 23 | 1673 | 23 | 23 | 19 |
| Missouri non-MSA | Missouri | Perry | 8 | 1423 | 23 | 29 | 21 |
| Missouri non-MSA | Missouri | Washington | 22 | 1299 | 23 | 29 | 22 |
| Missouri non-MSA | Missouri | Barry | 22 | 1351 | 23 | 23 | 20 |
| Kansas City | Missouri | Platte | 14 | 1487 | 22 | 22 | 18 |
| St. Louis-Farmington | Missouri | Warren | 2 | 1057 | 22 | 22 | 15 |
| Missouri non-MSA | Missouri | Pulaski | 15 | 1447 | 21 | 20 | 18 |
| Missouri non-MSA | Missouri | Pike | 8 | 797 | 20 | 21 | 15 |
| Kansas City | Missouri | Lafayette | 29 | 1355 | 19 | 21 | 19 |
| Missouri non-MSA | Missouri | Miller | 23 | 1390 | 19 | 20 | 19 |
| Missouri non-MSA | Missouri | Adair | 1 | 997 | 18 | 23 | 17 |
| Missouri non-MSA | Missouri | Laclede | 29 | 1659 | 18 | 20 | 18 |
| Missouri non-MSA | Missouri | Saline | 12 | 1464 | 18 | 24 | 18 |
| Missouri non-MSA | Missouri | Macon | 2 | 565 | 17 | 17 | 12 |
| Kansas City | Kansas | Miami | 2 | 866 | 17 | 15 | 11 |
| Missouri non-MSA | Missouri | Randolph | 5 | 1106 | 16 | 22 | 18 |
| Missouri non-MSA | Missouri | Mississippi | 6 | 696 | 16 | 13 | 9 |
| Missouri non-MSA | Missouri | Crawford | 11 | 1077 | 16 | 20 | 16 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 1228 | 16 | 22 | 16 |
| Missouri non-MSA | Missouri | Dunklin | 13 | 1578 | 16 | 18 | 17 |
| Missouri non-MSA | Missouri | Pettis | 29 | 2564 | 16 | 32 | 35 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1120 | 15 | 22 | 19 |
| Missouri non-MSA | Missouri | Stone | 15 | 1070 | 15 | 16 | 13 |
| St. Louis-Farmington | Illinois | Bond | 10 | 907 | 14 | 18 | 14 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 929 | 14 | 22 | 19 |
| Columbia-Jefferson City | Missouri | Cooper | 6 | 1082 | 13 | 19 | 16 |
| Missouri non-MSA | Missouri | Audrain | 11 | 938 | 12 | 15 | 12 |
| St. Joseph | Missouri | Andrew | 8 | 702 | 12 | 13 | 9 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 848 | 12 | 14 | 13 |
| Missouri non-MSA | Missouri | Morgan | 9 | 989 | 11 | 12 | 12 |
| Kansas City | Missouri | Clinton | 42 | 814 | 11 | 13 | 12 |
| Missouri non-MSA | Missouri | Madison | 7 | 773 | 11 | 13 | 10 |
| Kansas City | Missouri | Bates | 8 | 460 | 11 | 11 | 7 |
| St. Joseph | Kansas | Doniphan | 2 | 391 | 9 | 10 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 7 | 760 | 9 | 12 | 10 |
| Kansas City | Missouri | Ray | 4 | 607 | 9 | 15 | 11 |
| Missouri non-MSA | Missouri | Howell | 26 | 1505 | 9 | 11 | 14 |
| Missouri non-MSA | Missouri | Vernon | 5 | 603 | 9 | 11 | 9 |
| Missouri non-MSA | Missouri | Pemiscot | 16 | 1012 | 9 | 13 | 10 |
| Missouri non-MSA | Missouri | Dent | 4 | 442 | 9 | 9 | 6 |
| Missouri non-MSA | Missouri | Ralls | 1 | 400 | 9 | 10 | 6 |
| Missouri non-MSA | Missouri | Grundy | 13 | 468 | 9 | 10 | 7 |
| Springfield | Missouri | Polk | 11 | 1297 | 9 | 11 | 12 |
| Missouri non-MSA | Missouri | Texas | 7 | 891 | 8 | 12 | 11 |
| Missouri non-MSA | Missouri | Cedar | 4 | 418 | 8 | 9 | 6 |
| Kansas City | Missouri | Caldwell | 1 | 344 | 8 | 8 | 6 |
| Missouri non-MSA | Missouri | Livingston | 11 | 730 | 8 | 8 | 5 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 212 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Harrison | 1 | 357 | 7 | 9 | 5 |
| Missouri non-MSA | Missouri | Sullivan | 6 | 537 | 7 | 7 | 8 |
| St. Joseph | Missouri | DeKalb | 9 | 505 | 7 | 7 | 8 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 290 | 7 | 9 | 5 |
| Missouri non-MSA | Missouri | Carroll | 5 | 368 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Lewis | 2 | 410 | 7 | 9 | 7 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 437 | 7 | 8 | 6 |
| Springfield | Missouri | Dallas | 5 | 559 | 7 | 8 | 7 |
| Kansas City | Kansas | Linn | 1 | 248 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Benton | 8 | 722 | 6 | 11 | 8 |
| Missouri non-MSA | Missouri | Monroe | 3 | 339 | 6 | 8 | 6 |
| Missouri non-MSA | Missouri | Gentry | 11 | 369 | 6 | 9 | 6 |
| Missouri non-MSA | Missouri | Wayne | 3 | 450 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | Clark | 2 | 269 | 6 | 7 | 5 |
| Missouri non-MSA | Missouri | Holt | 2 | 232 | 6 | 5 | 4 |
| Missouri non-MSA | Missouri | Carter | 4 | 272 | 5 | 4 | 3 |
| Missouri non-MSA | Missouri | Chariton | 0 | 217 | 5 | 7 | 5 |
| Missouri non-MSA | Missouri | Iron | 0 | 206 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Barton | 4 | 595 | 5 | 8 | 6 |
| Missouri non-MSA | Missouri | Atchison | 1 | 184 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Wright | 12 | 724 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Maries | 2 | 330 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Scotland | 1 | 170 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | McDonald | 15 | 1352 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 405 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Linn | 10 | 283 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Ripley | 5 | 453 | 4 | 8 | 7 |
| Missouri non-MSA | Missouri | Oregon | 0 | 346 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Dade | 5 | 268 | 4 | 6 | 4 |
| Missouri non-MSA | Missouri | Montgomery | 5 | 292 | 4 | 4 | 5 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 241 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Douglas | 15 | 381 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Knox | 1 | 124 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 152 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Shelby | 1 | 177 | 2 | 4 | 2 |
| Missouri non-MSA | Missouri | Daviess | 7 | 306 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Mercer | 0 | 76 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Ozark | 2 | 274 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Hickory | 4 | 344 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Putnam | 1 | 110 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 59 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 323 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 119 | 1 | 2 | 2 |
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
