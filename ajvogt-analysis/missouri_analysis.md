# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/17/2020  
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
| St. Louis-Farmington | 2912 | 179496 | 1910 | 1940 | 2065 |
| Kansas City | 1369 | 119717 | 1218 | 1310 | 1299 |
| Missouri non-MSA | 1154 | 82959 | 818 | 849 | 857 |
| Springfield | 335 | 25834 | 253 | 266 | 250 |
| Columbia-Jefferson City | 167 | 26822 | 191 | 218 | 252 |
| Cape Girardeau-Sikeston | 156 | 10180 | 70 | 84 | 106 |
| St. Joseph | 116 | 7908 | 61 | 77 | 88 |
| Joplin | 178 | 12384 | 55 | 67 | 89 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1199 | 61978 | 634 | 641 | 664 |
| Kansas City | Kansas | Johnson | 357 | 33964 | 401 | 420 | 399 |
| St. Louis-Farmington | Missouri | St. Charles | 245 | 24270 | 245 | 252 | 281 |
| St. Louis-Farmington | Illinois | Madison | 344 | 18388 | 232 | 232 | 237 |
| Kansas City | Missouri | Kansas City | 325 | 27215 | 212 | 244 | 261 |
| Kansas City | Missouri | Jackson | 205 | 20918 | 199 | 221 | 231 |
| St. Louis-Farmington | Illinois | St. Clair | 317 | 16875 | 196 | 203 | 206 |
| Springfield | Missouri | Greene | 238 | 16658 | 162 | 167 | 161 |
| Kansas City | Kansas | Wyandotte | 187 | 13834 | 150 | 146 | 129 |
| St. Louis-Farmington | Missouri | Jefferson | 121 | 13469 | 138 | 143 | 167 |
| St. Louis-Farmington | Missouri | St. Louis City | 276 | 15331 | 138 | 146 | 151 |
| Columbia-Jefferson City | Missouri | Boone | 36 | 12059 | 101 | 105 | 110 |
| Missouri non-MSA | Missouri | Pettis | 47 | 3588 | 62 | 63 | 37 |
| Kansas City | Missouri | Cass | 44 | 4801 | 60 | 62 | 61 |
| Missouri non-MSA | Missouri | Howell | 35 | 2093 | 57 | 34 | 21 |
| St. Louis-Farmington | Missouri | Franklin | 102 | 5775 | 56 | 57 | 61 |
| Springfield | Missouri | Christian | 34 | 4729 | 55 | 58 | 51 |
| St. Louis-Farmington | Missouri | St. Francois | 58 | 5859 | 54 | 47 | 56 |
| Kansas City | Missouri | Clay | 86 | 5548 | 53 | 56 | 60 |
| Joplin | Missouri | Jasper | 138 | 9198 | 45 | 54 | 70 |
| St. Joseph | Missouri | Buchanan | 81 | 5618 | 43 | 55 | 59 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 91 | 5858 | 43 | 48 | 61 |
| St. Louis-Farmington | Missouri | Lincoln | 17 | 3102 | 41 | 40 | 41 |
| St. Louis-Farmington | Illinois | Clinton | 74 | 4040 | 41 | 41 | 48 |
| Kansas City | Kansas | Leavenworth | 36 | 4553 | 40 | 47 | 44 |
| Columbia-Jefferson City | Missouri | Cole | 77 | 7042 | 39 | 50 | 67 |
| St. Louis-Farmington | Illinois | Monroe | 56 | 2651 | 35 | 34 | 35 |
| St. Louis-Farmington | Illinois | Macoupin | 50 | 2877 | 33 | 35 | 45 |
| Missouri non-MSA | Missouri | Taney | 47 | 3454 | 29 | 36 | 36 |
| Missouri non-MSA | Missouri | Butler | 11 | 2608 | 25 | 26 | 28 |
| Missouri non-MSA | Missouri | Johnson | 25 | 2939 | 25 | 25 | 28 |
| Missouri non-MSA | Missouri | Laclede | 38 | 2248 | 24 | 27 | 23 |
| Missouri non-MSA | Missouri | Pulaski | 26 | 2171 | 24 | 35 | 28 |
| Missouri non-MSA | Missouri | Adair | 4 | 1371 | 23 | 18 | 16 |
| Kansas City | Kansas | Miami | 7 | 1456 | 22 | 26 | 22 |
| Columbia-Jefferson City | Missouri | Callaway | 17 | 3349 | 22 | 30 | 35 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1956 | 22 | 16 | 15 |
| St. Louis-Farmington | Illinois | Jersey | 31 | 1701 | 20 | 24 | 25 |
| Springfield | Missouri | Webster | 33 | 2144 | 19 | 21 | 20 |
| Missouri non-MSA | Missouri | Camden | 59 | 2834 | 19 | 22 | 24 |
| St. Louis-Farmington | Illinois | Bond | 15 | 1384 | 18 | 19 | 18 |
| Missouri non-MSA | Missouri | Phelps | 74 | 2152 | 18 | 22 | 28 |
| Kansas City | Missouri | Platte | 18 | 2039 | 18 | 21 | 23 |
| Missouri non-MSA | Missouri | Marion | 23 | 2145 | 18 | 22 | 24 |
| Cape Girardeau-Sikeston | Missouri | Scott | 49 | 3092 | 17 | 25 | 33 |
| Missouri non-MSA | Missouri | Benton | 12 | 1065 | 17 | 20 | 12 |
| Missouri non-MSA | Missouri | Audrain | 21 | 1389 | 16 | 18 | 17 |
| Missouri non-MSA | Missouri | Miller | 38 | 1807 | 16 | 18 | 17 |
| St. Louis-Farmington | Missouri | Warren | 6 | 1448 | 16 | 13 | 17 |
| Missouri non-MSA | Missouri | Crawford | 15 | 1433 | 14 | 14 | 15 |
| Missouri non-MSA | Missouri | Saline | 15 | 1800 | 14 | 13 | 15 |
| Kansas City | Missouri | Lafayette | 35 | 1805 | 14 | 16 | 19 |
| Missouri non-MSA | Missouri | Stoddard | 28 | 1919 | 14 | 17 | 22 |
| Missouri non-MSA | Missouri | Texas | 12 | 1168 | 14 | 13 | 10 |
| Missouri non-MSA | Missouri | Randolph | 14 | 1458 | 13 | 15 | 15 |
| Missouri non-MSA | Missouri | Morgan | 15 | 1314 | 13 | 16 | 13 |
| Kansas City | Missouri | Ray | 6 | 907 | 13 | 12 | 11 |
| Missouri non-MSA | Missouri | Stone | 23 | 1432 | 12 | 14 | 14 |
| Springfield | Missouri | Polk | 16 | 1650 | 12 | 16 | 13 |
| Kansas City | Missouri | Clinton | 49 | 1102 | 12 | 13 | 11 |
| Missouri non-MSA | Missouri | Pike | 11 | 1138 | 12 | 12 | 15 |
| Missouri non-MSA | Missouri | Perry | 15 | 1729 | 12 | 11 | 15 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1269 | 11 | 11 | 14 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2133 | 11 | 12 | 17 |
| Missouri non-MSA | Missouri | Barry | 35 | 1647 | 11 | 11 | 14 |
| Missouri non-MSA | Missouri | Oregon | 3 | 485 | 10 | 7 | 5 |
| Columbia-Jefferson City | Missouri | Cooper | 13 | 1345 | 10 | 11 | 11 |
| Joplin | Missouri | Newton | 40 | 3186 | 10 | 12 | 19 |
| Missouri non-MSA | Missouri | Wright | 19 | 922 | 10 | 9 | 7 |
| Missouri non-MSA | Missouri | Henry | 18 | 1282 | 9 | 11 | 15 |
| Missouri non-MSA | Missouri | Washington | 34 | 1632 | 9 | 10 | 15 |
| Missouri non-MSA | Missouri | Macon | 5 | 815 | 9 | 8 | 12 |
| Missouri non-MSA | Missouri | Mississippi | 9 | 1058 | 9 | 11 | 14 |
| Missouri non-MSA | Missouri | Madison | 10 | 1058 | 9 | 10 | 11 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2197 | 9 | 11 | 15 |
| Missouri non-MSA | Missouri | New Madrid | 26 | 1498 | 9 | 8 | 12 |
| St. Joseph | Missouri | Andrew | 13 | 981 | 8 | 10 | 11 |
| Missouri non-MSA | Missouri | Harrison | 7 | 539 | 8 | 9 | 7 |
| Missouri non-MSA | Missouri | Douglas | 19 | 536 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Carroll | 8 | 566 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Vernon | 13 | 833 | 8 | 10 | 9 |
| Kansas City | Missouri | Bates | 9 | 682 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | Gasconade | 27 | 591 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Livingston | 19 | 905 | 7 | 8 | 7 |
| Columbia-Jefferson City | Missouri | Moniteau | 16 | 1384 | 7 | 8 | 11 |
| Kansas City | Kansas | Linn | 2 | 421 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1530 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Gentry | 15 | 536 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Pemiscot | 20 | 1215 | 6 | 7 | 8 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 429 | 6 | 5 | 5 |
| St. Joseph | Missouri | DeKalb | 17 | 702 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | Wayne | 4 | 598 | 6 | 6 | 6 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1072 | 6 | 8 | 9 |
| Missouri non-MSA | Missouri | Iron | 1 | 309 | 5 | 4 | 4 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 11 | 917 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Ralls | 4 | 582 | 5 | 6 | 8 |
| Missouri non-MSA | Missouri | Ripley | 8 | 619 | 5 | 4 | 6 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 348 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Dent | 6 | 620 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Grundy | 18 | 600 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Ozark | 4 | 347 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Monroe | 5 | 462 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Barton | 7 | 706 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 174 | 4 | 2 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 5 | 313 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Daviess | 9 | 411 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Linn | 11 | 385 | 3 | 4 | 4 |
| Kansas City | Missouri | Caldwell | 3 | 472 | 3 | 4 | 5 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 571 | 3 | 3 | 6 |
| Missouri non-MSA | Missouri | Carter | 6 | 349 | 3 | 3 | 3 |
| Springfield | Missouri | Dallas | 14 | 653 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 384 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 607 | 2 | 2 | 4 |
| St. Joseph | Kansas | Doniphan | 5 | 607 | 2 | 5 | 8 |
| Missouri non-MSA | Missouri | Maries | 6 | 421 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Holt | 7 | 311 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 4 | 398 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Dade | 8 | 327 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Atchison | 4 | 251 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Hickory | 6 | 404 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Cedar | 8 | 473 | 2 | 1 | 3 |
| Missouri non-MSA | Missouri | Chariton | 1 | 283 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Mercer | 1 | 109 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 1 | 268 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Scotland | 2 | 214 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Lewis | 2 | 486 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Worth | 0 | 105 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 207 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 4 | 337 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Putnam | 1 | 183 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 1 | 142 | 0 | 0 | 1 |
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
