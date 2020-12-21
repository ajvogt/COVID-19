# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/21/2020  
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
| St. Louis-Farmington | 3054 | 186589 | 1772 | 1822 | 1977 |
| Kansas City | 1413 | 123541 | 1166 | 1217 | 1211 |
| Missouri non-MSA | 1185 | 85830 | 676 | 753 | 805 |
| Springfield | 338 | 26932 | 255 | 259 | 251 |
| Columbia-Jefferson City | 171 | 27717 | 198 | 198 | 232 |
| Cape Girardeau-Sikeston | 160 | 10476 | 67 | 68 | 92 |
| Joplin | 185 | 12706 | 67 | 68 | 79 |
| St. Joseph | 121 | 8089 | 49 | 63 | 80 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1281 | 64375 | 615 | 606 | 649 |
| Kansas City | Kansas | Johnson | 385 | 35086 | 417 | 415 | 373 |
| St. Louis-Farmington | Missouri | St. Charles | 261 | 25312 | 241 | 240 | 266 |
| St. Louis-Farmington | Illinois | Madison | 355 | 19267 | 214 | 221 | 229 |
| Kansas City | Missouri | Kansas City | 327 | 28006 | 195 | 205 | 244 |
| St. Louis-Farmington | Illinois | St. Clair | 325 | 17501 | 165 | 186 | 201 |
| Kansas City | Missouri | Jackson | 207 | 21519 | 158 | 183 | 210 |
| Springfield | Missouri | Greene | 238 | 17306 | 156 | 161 | 159 |
| Kansas City | Kansas | Wyandotte | 190 | 14105 | 135 | 143 | 119 |
| St. Louis-Farmington | Missouri | St. Louis City | 282 | 15865 | 127 | 135 | 149 |
| St. Louis-Farmington | Missouri | Jefferson | 121 | 13958 | 119 | 127 | 153 |
| Columbia-Jefferson City | Missouri | Boone | 36 | 12492 | 102 | 103 | 103 |
| Springfield | Missouri | Christian | 35 | 5010 | 60 | 59 | 54 |
| Kansas City | Missouri | Cass | 46 | 5060 | 58 | 60 | 59 |
| Joplin | Missouri | Jasper | 145 | 9440 | 51 | 54 | 63 |
| St. Louis-Farmington | Missouri | Franklin | 106 | 5993 | 51 | 55 | 58 |
| Kansas City | Kansas | Leavenworth | 36 | 4698 | 50 | 49 | 43 |
| St. Louis-Farmington | Missouri | St. Francois | 58 | 6070 | 48 | 49 | 52 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 91 | 6059 | 45 | 42 | 55 |
| Kansas City | Missouri | Clay | 87 | 5747 | 42 | 50 | 54 |
| Missouri non-MSA | Missouri | Pettis | 50 | 3799 | 38 | 59 | 42 |
| St. Louis-Farmington | Illinois | Monroe | 56 | 2808 | 36 | 33 | 36 |
| St. Louis-Farmington | Illinois | Clinton | 77 | 4156 | 35 | 38 | 42 |
| Columbia-Jefferson City | Missouri | Cole | 77 | 7192 | 34 | 37 | 58 |
| St. Louis-Farmington | Missouri | Lincoln | 17 | 3246 | 34 | 37 | 39 |
| St. Louis-Farmington | Illinois | Macoupin | 57 | 3004 | 32 | 34 | 39 |
| St. Joseph | Missouri | Buchanan | 86 | 5727 | 30 | 42 | 54 |
| Columbia-Jefferson City | Missouri | Callaway | 17 | 3495 | 28 | 27 | 33 |
| Kansas City | Kansas | Miami | 7 | 1514 | 25 | 26 | 21 |
| Missouri non-MSA | Missouri | Johnson | 25 | 3039 | 23 | 24 | 25 |
| Kansas City | Missouri | Platte | 19 | 2138 | 22 | 20 | 22 |
| Missouri non-MSA | Missouri | Taney | 47 | 3553 | 21 | 28 | 34 |
| Springfield | Missouri | Webster | 35 | 2238 | 21 | 20 | 19 |
| Missouri non-MSA | Missouri | Audrain | 23 | 1493 | 20 | 19 | 19 |
| St. Louis-Farmington | Illinois | Jersey | 34 | 1768 | 20 | 21 | 23 |
| Missouri non-MSA | Missouri | Miller | 42 | 1902 | 20 | 17 | 17 |
| Missouri non-MSA | Missouri | Camden | 58 | 2922 | 20 | 21 | 22 |
| Missouri non-MSA | Missouri | Adair | 4 | 1426 | 19 | 18 | 15 |
| Missouri non-MSA | Missouri | Phelps | 76 | 2256 | 19 | 19 | 26 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1984 | 19 | 14 | 14 |
| Missouri non-MSA | Missouri | Laclede | 39 | 2329 | 17 | 22 | 23 |
| Missouri non-MSA | Missouri | Pulaski | 26 | 2262 | 16 | 22 | 28 |
| Missouri non-MSA | Missouri | Texas | 13 | 1249 | 16 | 14 | 12 |
| St. Louis-Farmington | Missouri | Warren | 8 | 1497 | 15 | 13 | 15 |
| Joplin | Missouri | Newton | 40 | 3266 | 15 | 14 | 16 |
| Cape Girardeau-Sikeston | Missouri | Scott | 53 | 3167 | 15 | 18 | 28 |
| Missouri non-MSA | Missouri | Stone | 23 | 1505 | 15 | 14 | 14 |
| Kansas City | Missouri | Lafayette | 36 | 1879 | 15 | 15 | 18 |
| Kansas City | Missouri | Ray | 7 | 977 | 15 | 13 | 12 |
| Missouri non-MSA | Missouri | Butler | 12 | 2646 | 15 | 20 | 25 |
| Missouri non-MSA | Missouri | Crawford | 15 | 1494 | 13 | 14 | 14 |
| Missouri non-MSA | Missouri | Marion | 23 | 2197 | 13 | 17 | 21 |
| Springfield | Missouri | Polk | 16 | 1709 | 13 | 14 | 13 |
| Missouri non-MSA | Missouri | Saline | 16 | 1857 | 13 | 13 | 13 |
| Missouri non-MSA | Missouri | Benton | 15 | 1134 | 13 | 17 | 14 |
| Columbia-Jefferson City | Missouri | Cooper | 17 | 1414 | 12 | 11 | 11 |
| Missouri non-MSA | Missouri | Perry | 15 | 1771 | 12 | 9 | 13 |
| Missouri non-MSA | Missouri | Henry | 19 | 1349 | 12 | 11 | 13 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2190 | 12 | 12 | 14 |
| Missouri non-MSA | Missouri | Howell | 35 | 2144 | 12 | 34 | 21 |
| Missouri non-MSA | Missouri | Morgan | 16 | 1374 | 11 | 14 | 13 |
| Missouri non-MSA | Missouri | Barry | 35 | 1706 | 11 | 12 | 12 |
| St. Louis-Farmington | Illinois | Bond | 15 | 1416 | 11 | 16 | 17 |
| Missouri non-MSA | Missouri | Macon | 5 | 851 | 11 | 8 | 10 |
| Missouri non-MSA | Missouri | Livingston | 19 | 953 | 11 | 8 | 7 |
| Missouri non-MSA | Missouri | Stoddard | 31 | 1948 | 10 | 11 | 17 |
| Kansas City | Missouri | Clinton | 50 | 1156 | 10 | 12 | 11 |
| Missouri non-MSA | Missouri | Randolph | 15 | 1503 | 10 | 12 | 14 |
| Missouri non-MSA | Missouri | Vernon | 13 | 877 | 10 | 8 | 9 |
| Missouri non-MSA | Missouri | Pike | 11 | 1178 | 10 | 10 | 13 |
| Missouri non-MSA | Missouri | Madison | 10 | 1097 | 10 | 9 | 12 |
| Missouri non-MSA | Missouri | Wright | 19 | 953 | 8 | 8 | 7 |
| Kansas City | Missouri | Bates | 10 | 723 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1309 | 8 | 10 | 13 |
| Missouri non-MSA | Missouri | New Madrid | 26 | 1532 | 8 | 8 | 10 |
| Missouri non-MSA | Missouri | Washington | 34 | 1671 | 8 | 9 | 13 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1110 | 8 | 7 | 9 |
| St. Joseph | Missouri | Andrew | 13 | 1011 | 7 | 8 | 11 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1558 | 7 | 7 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 16 | 1422 | 7 | 7 | 10 |
| Missouri non-MSA | Missouri | Harrison | 7 | 579 | 7 | 9 | 7 |
| Missouri non-MSA | Missouri | Mississippi | 10 | 1088 | 7 | 8 | 13 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2224 | 6 | 8 | 14 |
| Missouri non-MSA | Missouri | Gentry | 15 | 563 | 6 | 6 | 6 |
| Kansas City | Kansas | Linn | 3 | 438 | 6 | 7 | 6 |
| Missouri non-MSA | Missouri | Carroll | 9 | 593 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Douglas | 19 | 557 | 6 | 6 | 6 |
| St. Joseph | Kansas | Doniphan | 5 | 632 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | Gasconade | 29 | 613 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 452 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Dent | 6 | 648 | 6 | 5 | 7 |
| Missouri non-MSA | Missouri | Iron | 1 | 329 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Wayne | 4 | 614 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 20 | 1231 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Ralls | 4 | 599 | 4 | 5 | 6 |
| Kansas City | Missouri | Caldwell | 3 | 495 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Grundy | 19 | 628 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Barton | 7 | 725 | 4 | 4 | 4 |
| St. Joseph | Missouri | DeKalb | 17 | 719 | 4 | 5 | 7 |
| Missouri non-MSA | Missouri | Ripley | 8 | 627 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Monroe | 5 | 473 | 4 | 4 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 592 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Daviess | 9 | 429 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 178 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 4 | 418 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 618 | 3 | 2 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 11 | 928 | 3 | 4 | 6 |
| Springfield | Missouri | Dallas | 14 | 669 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Oregon | 3 | 495 | 3 | 6 | 5 |
| Missouri non-MSA | Missouri | Maries | 6 | 433 | 3 | 2 | 3 |
| Missouri non-MSA | Missouri | Chariton | 2 | 298 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Lewis | 2 | 501 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Shannon | 9 | 395 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 279 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Cedar | 8 | 483 | 2 | 1 | 2 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 353 | 2 | 4 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 5 | 322 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Dade | 8 | 338 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 11 | 392 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Mercer | 1 | 119 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 6 | 354 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Scotland | 3 | 217 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 215 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Putnam | 1 | 188 | 1 | 0 | 2 |
| Missouri non-MSA | Missouri | Holt | 7 | 316 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Ozark | 4 | 349 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Clark | 4 | 344 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 6 | 410 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Atchison | 4 | 255 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 1 | 146 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 106 | 0 | 1 | 1 |
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
