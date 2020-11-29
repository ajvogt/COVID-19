# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 11/29/2020  
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
| St. Louis-Farmington | 2327 | 144875 | 2180 | 2220 | 2034 |
| Kansas City | 1167 | 96969 | 1269 | 1314 | 1220 |
| Missouri non-MSA | 839 | 68294 | 771 | 852 | 951 |
| Columbia-Jefferson City | 107 | 22877 | 261 | 278 | 350 |
| Springfield | 241 | 21194 | 217 | 226 | 242 |
| Cape Girardeau-Sikeston | 112 | 8677 | 110 | 126 | 129 |
| St. Joseph | 78 | 6437 | 98 | 88 | 82 |
| Joplin | 144 | 11122 | 89 | 109 | 124 |
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
| St. Louis-Farmington | Missouri | St. Louis | 976 | 50729 | 727 | 740 | 662 |
| Kansas City | Kansas | Johnson | 285 | 26731 | 405 | 413 | 363 |
| St. Louis-Farmington | Missouri | St. Charles | 213 | 19731 | 288 | 300 | 292 |
| Kansas City | Missouri | Kansas City | 281 | 22969 | 275 | 277 | 279 |
| St. Louis-Farmington | Illinois | Madison | 253 | 14210 | 222 | 245 | 225 |
| St. Louis-Farmington | Illinois | St. Clair | 259 | 13185 | 215 | 205 | 167 |
| Kansas City | Missouri | Jackson | 177 | 16937 | 208 | 227 | 226 |
| St. Louis-Farmington | Missouri | Jefferson | 103 | 10834 | 182 | 185 | 173 |
| St. Louis-Farmington | Missouri | St. Louis City | 238 | 12774 | 174 | 156 | 141 |
| Springfield | Missouri | Greene | 173 | 13711 | 144 | 146 | 153 |
| Kansas City | Kansas | Wyandotte | 178 | 11412 | 125 | 123 | 90 |
| Columbia-Jefferson City | Missouri | Boone | 23 | 10193 | 96 | 110 | 136 |
| Columbia-Jefferson City | Missouri | Cole | 49 | 6096 | 81 | 83 | 103 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 65 | 5004 | 68 | 74 | 76 |
| Joplin | Missouri | Jasper | 106 | 8155 | 65 | 82 | 94 |
| St. Louis-Farmington | Missouri | St. Francois | 44 | 5036 | 62 | 67 | 71 |
| St. Louis-Farmington | Missouri | Franklin | 72 | 4753 | 60 | 65 | 67 |
| St. Joseph | Missouri | Buchanan | 57 | 4565 | 59 | 54 | 52 |
| Kansas City | Missouri | Cass | 39 | 3721 | 54 | 57 | 54 |
| St. Louis-Farmington | Illinois | Clinton | 61 | 3279 | 52 | 54 | 47 |
| Kansas City | Missouri | Clay | 68 | 4553 | 48 | 64 | 66 |
| Kansas City | Kansas | Leavenworth | 31 | 3729 | 45 | 45 | 34 |
| St. Louis-Farmington | Illinois | Monroe | 45 | 2060 | 44 | 38 | 35 |
| St. Louis-Farmington | Illinois | Macoupin | 18 | 2184 | 44 | 51 | 44 |
| St. Louis-Farmington | Missouri | Lincoln | 9 | 2407 | 41 | 42 | 39 |
| Columbia-Jefferson City | Missouri | Callaway | 8 | 2789 | 38 | 38 | 51 |
| Springfield | Missouri | Christian | 23 | 3708 | 37 | 42 | 46 |
| Missouri non-MSA | Missouri | Taney | 40 | 2823 | 37 | 36 | 35 |
| Cape Girardeau-Sikeston | Missouri | Scott | 37 | 2623 | 34 | 41 | 39 |
| Missouri non-MSA | Missouri | Phelps | 42 | 1734 | 32 | 31 | 29 |
| Missouri non-MSA | Missouri | Butler | 9 | 2115 | 25 | 28 | 28 |
| Missouri non-MSA | Missouri | Johnson | 15 | 2477 | 25 | 28 | 32 |
| Joplin | Missouri | Newton | 38 | 2967 | 24 | 27 | 30 |
| Missouri non-MSA | Missouri | Mississippi | 7 | 859 | 23 | 19 | 13 |
| Missouri non-MSA | Missouri | Marion | 16 | 1756 | 23 | 26 | 27 |
| Missouri non-MSA | Missouri | Stoddard | 20 | 1613 | 22 | 27 | 24 |
| Kansas City | Missouri | Platte | 17 | 1636 | 21 | 22 | 20 |
| Kansas City | Kansas | Miami | 2 | 1013 | 21 | 19 | 14 |
| Kansas City | Missouri | Lafayette | 29 | 1499 | 20 | 19 | 21 |
| St. Louis-Farmington | Illinois | Jersey | 24 | 1221 | 20 | 22 | 24 |
| St. Louis-Farmington | Missouri | Warren | 2 | 1197 | 20 | 21 | 18 |
| Missouri non-MSA | Missouri | Pulaski | 18 | 1587 | 20 | 20 | 18 |
| Missouri non-MSA | Missouri | Camden | 45 | 2420 | 19 | 24 | 26 |
| Missouri non-MSA | Missouri | Audrain | 13 | 1075 | 19 | 16 | 16 |
| Missouri non-MSA | Missouri | Nodaway | 13 | 1963 | 19 | 23 | 26 |
| St. Louis-Farmington | Illinois | Bond | 10 | 1040 | 19 | 16 | 17 |
| Springfield | Missouri | Webster | 24 | 1806 | 19 | 21 | 21 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1046 | 16 | 15 | 21 |
| Missouri non-MSA | Missouri | New Madrid | 23 | 1344 | 16 | 16 | 18 |
| Missouri non-MSA | Missouri | Laclede | 30 | 1774 | 16 | 17 | 18 |
| Missouri non-MSA | Missouri | Washington | 23 | 1411 | 16 | 19 | 24 |
| Missouri non-MSA | Missouri | Lawrence | 37 | 1884 | 16 | 21 | 25 |
| St. Joseph | Kansas | Doniphan | 2 | 503 | 16 | 12 | 9 |
| Missouri non-MSA | Missouri | Madison | 7 | 881 | 15 | 13 | 12 |
| Missouri non-MSA | Missouri | Henry | 10 | 1068 | 14 | 19 | 22 |
| Missouri non-MSA | Missouri | Saline | 12 | 1565 | 14 | 16 | 20 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1679 | 14 | 15 | 17 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1219 | 14 | 14 | 19 |
| Missouri non-MSA | Missouri | Macon | 3 | 663 | 14 | 15 | 14 |
| Missouri non-MSA | Missouri | Stone | 16 | 1167 | 13 | 14 | 15 |
| Missouri non-MSA | Missouri | Perry | 12 | 1520 | 13 | 18 | 23 |
| Missouri non-MSA | Missouri | Crawford | 12 | 1174 | 13 | 15 | 17 |
| Missouri non-MSA | Missouri | Pettis | 32 | 2659 | 13 | 14 | 34 |
| Missouri non-MSA | Missouri | Pike | 8 | 889 | 13 | 16 | 17 |
| St. Joseph | Missouri | Andrew | 9 | 790 | 12 | 12 | 11 |
| Missouri non-MSA | Missouri | Miller | 24 | 1476 | 12 | 15 | 19 |
| Missouri non-MSA | Missouri | Barry | 25 | 1433 | 11 | 17 | 19 |
| Missouri non-MSA | Missouri | Randolph | 5 | 1187 | 11 | 14 | 18 |
| Kansas City | Missouri | Bates | 9 | 540 | 11 | 11 | 9 |
| Columbia-Jefferson City | Missouri | Osage | 3 | 927 | 11 | 11 | 14 |
| Springfield | Missouri | Polk | 12 | 1374 | 11 | 10 | 13 |
| St. Joseph | Missouri | DeKalb | 10 | 579 | 10 | 9 | 9 |
| Kansas City | Missouri | Ray | 4 | 679 | 10 | 9 | 13 |
| Columbia-Jefferson City | Missouri | Cooper | 7 | 1153 | 10 | 11 | 17 |
| Missouri non-MSA | Missouri | Adair | 3 | 1067 | 10 | 14 | 17 |
| Missouri non-MSA | Missouri | Howell | 28 | 1573 | 9 | 9 | 12 |
| Missouri non-MSA | Missouri | Morgan | 12 | 1056 | 9 | 10 | 12 |
| Missouri non-MSA | Missouri | Ralls | 1 | 466 | 9 | 9 | 8 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 500 | 9 | 8 | 8 |
| Missouri non-MSA | Missouri | Dent | 4 | 505 | 9 | 9 | 8 |
| Missouri non-MSA | Missouri | Vernon | 7 | 665 | 8 | 9 | 10 |
| Missouri non-MSA | Missouri | Pemiscot | 16 | 1074 | 8 | 9 | 11 |
| Missouri non-MSA | Missouri | Gasconade | 24 | 465 | 8 | 6 | 6 |
| Missouri non-MSA | Missouri | Texas | 8 | 946 | 7 | 8 | 11 |
| Kansas City | Missouri | Clinton | 44 | 868 | 7 | 9 | 11 |
| Missouri non-MSA | Missouri | Ripley | 8 | 505 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Carroll | 6 | 419 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Montgomery | 5 | 343 | 7 | 5 | 6 |
| Missouri non-MSA | Missouri | Livingston | 14 | 777 | 6 | 7 | 7 |
| Kansas City | Kansas | Linn | 1 | 295 | 6 | 6 | 5 |
| Missouri non-MSA | Missouri | McDonald | 16 | 1398 | 6 | 5 | 5 |
| Missouri non-MSA | Missouri | Douglas | 15 | 425 | 6 | 4 | 4 |
| Kansas City | Missouri | Caldwell | 2 | 387 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Monroe | 3 | 381 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Putnam | 1 | 148 | 5 | 3 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 1 | 328 | 5 | 6 | 6 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 8 | 797 | 5 | 7 | 9 |
| Springfield | Missouri | Dallas | 9 | 595 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Gentry | 11 | 405 | 5 | 5 | 7 |
| Missouri non-MSA | Missouri | Harrison | 2 | 393 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Wayne | 3 | 486 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Wright | 14 | 758 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Benton | 8 | 756 | 4 | 5 | 9 |
| Missouri non-MSA | Missouri | Linn | 9 | 316 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Grundy | 14 | 500 | 4 | 6 | 7 |
| Missouri non-MSA | Missouri | Barton | 4 | 626 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Holt | 3 | 262 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Maries | 3 | 359 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Clark | 3 | 297 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Iron | 0 | 232 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Daviess | 8 | 332 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Atchison | 3 | 209 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 175 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Shelby | 1 | 200 | 3 | 3 | 3 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 235 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Sullivan | 6 | 559 | 3 | 5 | 8 |
| Missouri non-MSA | Missouri | Cedar | 6 | 440 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Hickory | 6 | 366 | 3 | 2 | 5 |
| Missouri non-MSA | Missouri | Carter | 5 | 293 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Chariton | 0 | 238 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Oregon | 0 | 366 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Lewis | 2 | 429 | 2 | 5 | 7 |
| Missouri non-MSA | Missouri | Ozark | 2 | 291 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Dade | 6 | 285 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 338 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Scotland | 1 | 183 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 131 | 1 | 1 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 2 | 253 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Worth | 0 | 70 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Knox | 1 | 133 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 83 | 1 | 1 | 1 |
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
