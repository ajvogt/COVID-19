# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/15/2020  
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
| St. Louis-Farmington | 2790 | 175946 | 1877 | 1966 | 2071 |
| Kansas City | 1327 | 117447 | 1280 | 1293 | 1296 |
| Missouri non-MSA | 1052 | 81654 | 828 | 834 | 842 |
| Springfield | 315 | 25393 | 267 | 258 | 245 |
| Columbia-Jefferson City | 140 | 26476 | 193 | 224 | 249 |
| Cape Girardeau-Sikeston | 149 | 10085 | 72 | 88 | 105 |
| St. Joseph | 106 | 7822 | 72 | 80 | 87 |
| Joplin | 174 | 12272 | 72 | 72 | 89 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1153 | 60837 | 619 | 644 | 682 |
| Kansas City | Kansas | Johnson | 346 | 33144 | 420 | 408 | 406 |
| St. Louis-Farmington | Missouri | St. Charles | 234 | 23816 | 241 | 256 | 276 |
| St. Louis-Farmington | Illinois | Madison | 329 | 17969 | 231 | 240 | 239 |
| Kansas City | Missouri | Kansas City | 316 | 26835 | 214 | 236 | 258 |
| Kansas City | Missouri | Jackson | 197 | 20584 | 208 | 228 | 227 |
| St. Louis-Farmington | Illinois | St. Clair | 310 | 16508 | 195 | 209 | 206 |
| Springfield | Missouri | Greene | 229 | 16366 | 169 | 163 | 157 |
| Kansas City | Kansas | Wyandotte | 184 | 13568 | 165 | 145 | 129 |
| St. Louis-Farmington | Missouri | St. Louis City | 271 | 15070 | 141 | 145 | 149 |
| St. Louis-Farmington | Missouri | Jefferson | 113 | 13202 | 130 | 146 | 165 |
| Columbia-Jefferson City | Missouri | Boone | 29 | 11841 | 99 | 106 | 106 |
| Missouri non-MSA | Missouri | Pettis | 38 | 3535 | 79 | 60 | 36 |
| Kansas City | Missouri | Cass | 41 | 4690 | 63 | 62 | 59 |
| Springfield | Missouri | Christian | 29 | 4647 | 60 | 56 | 51 |
| Joplin | Missouri | Jasper | 135 | 9110 | 59 | 60 | 70 |
| Kansas City | Missouri | Clay | 81 | 5488 | 58 | 58 | 61 |
| Missouri non-MSA | Missouri | Howell | 34 | 2073 | 57 | 34 | 21 |
| St. Louis-Farmington | Missouri | Franklin | 96 | 5690 | 57 | 57 | 61 |
| St. Louis-Farmington | Missouri | St. Francois | 51 | 5786 | 53 | 48 | 56 |
| St. Joseph | Missouri | Buchanan | 72 | 5552 | 52 | 56 | 58 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 89 | 5798 | 43 | 50 | 61 |
| Kansas City | Kansas | Leavenworth | 35 | 4435 | 42 | 44 | 44 |
| Columbia-Jefferson City | Missouri | Cole | 65 | 6993 | 40 | 52 | 69 |
| St. Louis-Farmington | Illinois | Clinton | 72 | 3926 | 39 | 42 | 47 |
| St. Louis-Farmington | Missouri | Lincoln | 13 | 3033 | 38 | 39 | 40 |
| St. Louis-Farmington | Illinois | Macoupin | 46 | 2795 | 35 | 37 | 44 |
| Missouri non-MSA | Missouri | Taney | 46 | 3423 | 34 | 37 | 37 |
| St. Louis-Farmington | Illinois | Monroe | 55 | 2580 | 32 | 35 | 35 |
| Missouri non-MSA | Missouri | Laclede | 38 | 2223 | 26 | 28 | 23 |
| Missouri non-MSA | Missouri | Pulaski | 24 | 2158 | 25 | 36 | 28 |
| Missouri non-MSA | Missouri | Johnson | 22 | 2899 | 25 | 25 | 27 |
| Missouri non-MSA | Missouri | Butler | 10 | 2561 | 25 | 27 | 27 |
| Columbia-Jefferson City | Missouri | Callaway | 13 | 3313 | 25 | 32 | 35 |
| Kansas City | Kansas | Miami | 7 | 1404 | 25 | 23 | 21 |
| Missouri non-MSA | Missouri | Camden | 51 | 2802 | 24 | 23 | 24 |
| Missouri non-MSA | Missouri | Benton | 11 | 1053 | 23 | 19 | 12 |
| St. Louis-Farmington | Illinois | Jersey | 28 | 1658 | 23 | 25 | 25 |
| Missouri non-MSA | Missouri | Marion | 20 | 2118 | 21 | 22 | 24 |
| Missouri non-MSA | Missouri | Phelps | 60 | 2134 | 19 | 24 | 28 |
| Cape Girardeau-Sikeston | Missouri | Scott | 45 | 3072 | 19 | 27 | 34 |
| Springfield | Missouri | Webster | 29 | 2102 | 19 | 17 | 19 |
| St. Louis-Farmington | Illinois | Bond | 15 | 1338 | 19 | 20 | 17 |
| Missouri non-MSA | Missouri | Audrain | 16 | 1366 | 18 | 18 | 17 |
| Kansas City | Missouri | Platte | 17 | 1995 | 17 | 21 | 22 |
| Missouri non-MSA | Missouri | Adair | 3 | 1297 | 17 | 14 | 14 |
| Missouri non-MSA | Missouri | Morgan | 14 | 1296 | 16 | 15 | 12 |
| Kansas City | Missouri | Lafayette | 35 | 1782 | 16 | 16 | 18 |
| Missouri non-MSA | Missouri | Miller | 31 | 1771 | 15 | 18 | 17 |
| Springfield | Missouri | Polk | 15 | 1629 | 15 | 17 | 13 |
| Missouri non-MSA | Missouri | Crawford | 14 | 1411 | 14 | 14 | 15 |
| Kansas City | Missouri | Ray | 6 | 889 | 14 | 12 | 11 |
| Kansas City | Missouri | Clinton | 48 | 1094 | 14 | 14 | 11 |
| Missouri non-MSA | Missouri | Stone | 20 | 1414 | 13 | 15 | 15 |
| Missouri non-MSA | Missouri | Saline | 14 | 1777 | 13 | 13 | 14 |
| Missouri non-MSA | Missouri | Stoddard | 25 | 1884 | 13 | 16 | 21 |
| Missouri non-MSA | Missouri | Texas | 10 | 1148 | 13 | 12 | 10 |
| Missouri non-MSA | Missouri | Randolph | 11 | 1436 | 13 | 15 | 14 |
| Joplin | Missouri | Newton | 39 | 3162 | 12 | 12 | 19 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1259 | 12 | 12 | 14 |
| St. Louis-Farmington | Missouri | Warren | 3 | 1397 | 12 | 11 | 16 |
| Missouri non-MSA | Missouri | Pike | 11 | 1119 | 12 | 13 | 15 |
| Missouri non-MSA | Missouri | Barry | 33 | 1629 | 11 | 12 | 14 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2114 | 11 | 13 | 17 |
| Missouri non-MSA | Missouri | Harrison | 7 | 534 | 11 | 9 | 7 |
| Missouri non-MSA | Missouri | Henry | 16 | 1267 | 10 | 11 | 15 |
| Missouri non-MSA | Missouri | Oregon | 2 | 479 | 10 | 6 | 5 |
| Columbia-Jefferson City | Missouri | Cooper | 10 | 1329 | 10 | 11 | 11 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1858 | 10 | 10 | 13 |
| St. Joseph | Missouri | Andrew | 13 | 965 | 9 | 10 | 11 |
| Missouri non-MSA | Missouri | Mississippi | 8 | 1046 | 9 | 11 | 15 |
| Missouri non-MSA | Missouri | Nodaway | 17 | 2182 | 9 | 12 | 18 |
| Missouri non-MSA | Missouri | Wright | 17 | 899 | 9 | 8 | 7 |
| Missouri non-MSA | Missouri | Carroll | 8 | 560 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Madison | 10 | 1035 | 8 | 9 | 11 |
| Missouri non-MSA | Missouri | New Madrid | 26 | 1481 | 8 | 7 | 12 |
| Missouri non-MSA | Missouri | Washington | 31 | 1615 | 8 | 11 | 16 |
| Missouri non-MSA | Missouri | Perry | 15 | 1695 | 8 | 9 | 14 |
| Kansas City | Missouri | Bates | 9 | 668 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | Vernon | 13 | 818 | 8 | 9 | 9 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1375 | 7 | 9 | 12 |
| Kansas City | Kansas | Linn | 2 | 407 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 27 | 582 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | McDonald | 17 | 1507 | 7 | 7 | 6 |
| St. Joseph | Missouri | DeKalb | 16 | 698 | 7 | 7 | 8 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 341 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Douglas | 18 | 520 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 19 | 1198 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Grundy | 17 | 597 | 6 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1060 | 6 | 8 | 9 |
| Missouri non-MSA | Missouri | Wayne | 3 | 582 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Gentry | 14 | 523 | 5 | 7 | 6 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 416 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Macon | 4 | 777 | 5 | 6 | 11 |
| Missouri non-MSA | Missouri | Livingston | 18 | 877 | 5 | 6 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 10 | 907 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Iron | 1 | 297 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Ralls | 2 | 567 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Ripley | 8 | 607 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Barton | 6 | 697 | 4 | 4 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 5 | 308 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Dent | 5 | 615 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Daviess | 8 | 405 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Ozark | 4 | 343 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Monroe | 5 | 449 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Linn | 11 | 380 | 4 | 4 | 4 |
| Kansas City | Missouri | Caldwell | 3 | 464 | 4 | 4 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 565 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Carter | 6 | 345 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 3 | 397 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Shannon | 9 | 381 | 3 | 2 | 2 |
| Springfield | Missouri | Dallas | 13 | 649 | 3 | 3 | 4 |
| St. Joseph | Kansas | Doniphan | 5 | 607 | 2 | 6 | 9 |
| Missouri non-MSA | Missouri | Hickory | 6 | 403 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Holt | 5 | 309 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Atchison | 4 | 250 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dade | 8 | 323 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 262 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Mercer | 1 | 108 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 104 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Cedar | 8 | 471 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Maries | 4 | 413 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Lewis | 2 | 481 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Chariton | 0 | 280 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Sullivan | 8 | 596 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Clark | 4 | 337 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 153 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 206 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Scotland | 2 | 209 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 1 | 141 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 177 | 0 | 1 | 2 |
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
