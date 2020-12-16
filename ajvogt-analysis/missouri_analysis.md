# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/16/2020  
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
| St. Louis-Farmington | 2868 | 177872 | 1894 | 1964 | 2096 |
| Kansas City | 1363 | 118014 | 1271 | 1288 | 1314 |
| Missouri non-MSA | 1127 | 82223 | 804 | 835 | 860 |
| Springfield | 335 | 25592 | 252 | 263 | 252 |
| Columbia-Jefferson City | 166 | 26568 | 192 | 224 | 252 |
| Cape Girardeau-Sikeston | 155 | 10142 | 70 | 86 | 107 |
| St. Joseph | 114 | 7866 | 62 | 79 | 88 |
| Joplin | 175 | 12303 | 60 | 71 | 90 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1175 | 61500 | 629 | 648 | 683 |
| Kansas City | Kansas | Johnson | 357 | 33144 | 420 | 408 | 406 |
| St. Louis-Farmington | Missouri | St. Charles | 245 | 24057 | 240 | 253 | 284 |
| St. Louis-Farmington | Illinois | Madison | 337 | 18164 | 232 | 238 | 239 |
| Kansas City | Missouri | Kansas City | 324 | 27067 | 217 | 239 | 266 |
| Kansas City | Missouri | Jackson | 205 | 20779 | 206 | 222 | 234 |
| St. Louis-Farmington | Illinois | St. Clair | 312 | 16706 | 197 | 210 | 208 |
| Kansas City | Kansas | Wyandotte | 184 | 13568 | 165 | 145 | 129 |
| Springfield | Missouri | Greene | 238 | 16507 | 162 | 167 | 161 |
| St. Louis-Farmington | Missouri | Jefferson | 121 | 13354 | 135 | 145 | 170 |
| St. Louis-Farmington | Missouri | St. Louis City | 275 | 15199 | 134 | 143 | 149 |
| Columbia-Jefferson City | Missouri | Boone | 36 | 11879 | 98 | 106 | 107 |
| Missouri non-MSA | Missouri | Pettis | 47 | 3565 | 72 | 62 | 37 |
| Kansas City | Missouri | Cass | 44 | 4739 | 60 | 62 | 60 |
| Kansas City | Missouri | Clay | 86 | 5520 | 57 | 57 | 62 |
| Missouri non-MSA | Missouri | Howell | 34 | 2081 | 57 | 34 | 21 |
| St. Louis-Farmington | Missouri | Franklin | 101 | 5730 | 55 | 57 | 63 |
| Springfield | Missouri | Christian | 34 | 4680 | 55 | 57 | 52 |
| St. Louis-Farmington | Missouri | St. Francois | 58 | 5831 | 54 | 48 | 58 |
| Joplin | Missouri | Jasper | 135 | 9137 | 50 | 59 | 71 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 91 | 5836 | 43 | 48 | 62 |
| St. Joseph | Missouri | Buchanan | 79 | 5582 | 43 | 55 | 59 |
| Kansas City | Kansas | Leavenworth | 35 | 4435 | 42 | 44 | 44 |
| St. Louis-Farmington | Missouri | Lincoln | 16 | 3080 | 42 | 40 | 42 |
| St. Louis-Farmington | Illinois | Clinton | 74 | 3979 | 42 | 42 | 47 |
| Columbia-Jefferson City | Missouri | Cole | 77 | 7009 | 40 | 52 | 69 |
| St. Louis-Farmington | Illinois | Macoupin | 48 | 2840 | 35 | 37 | 45 |
| St. Louis-Farmington | Illinois | Monroe | 55 | 2622 | 34 | 35 | 35 |
| Missouri non-MSA | Missouri | Taney | 47 | 3439 | 32 | 36 | 37 |
| Missouri non-MSA | Missouri | Johnson | 25 | 2928 | 26 | 25 | 28 |
| Missouri non-MSA | Missouri | Laclede | 38 | 2238 | 26 | 28 | 23 |
| Missouri non-MSA | Missouri | Butler | 10 | 2588 | 25 | 27 | 28 |
| Columbia-Jefferson City | Missouri | Callaway | 17 | 3330 | 25 | 32 | 35 |
| Kansas City | Kansas | Miami | 7 | 1404 | 25 | 23 | 21 |
| Missouri non-MSA | Missouri | Pulaski | 26 | 2165 | 24 | 36 | 29 |
| St. Louis-Farmington | Illinois | Jersey | 29 | 1675 | 20 | 25 | 25 |
| Missouri non-MSA | Missouri | Benton | 12 | 1057 | 20 | 19 | 12 |
| Missouri non-MSA | Missouri | Camden | 58 | 2814 | 20 | 23 | 24 |
| Missouri non-MSA | Missouri | Marion | 23 | 2131 | 19 | 22 | 24 |
| Springfield | Missouri | Webster | 33 | 2118 | 18 | 19 | 20 |
| St. Louis-Farmington | Illinois | Bond | 15 | 1353 | 17 | 19 | 18 |
| Kansas City | Missouri | Platte | 17 | 2015 | 17 | 20 | 22 |
| Cape Girardeau-Sikeston | Missouri | Scott | 48 | 3083 | 17 | 26 | 34 |
| Missouri non-MSA | Missouri | Audrain | 21 | 1372 | 17 | 18 | 17 |
| Missouri non-MSA | Missouri | Phelps | 64 | 2140 | 16 | 22 | 28 |
| Missouri non-MSA | Missouri | Adair | 4 | 1308 | 16 | 15 | 14 |
| St. Louis-Farmington | Missouri | Warren | 6 | 1438 | 15 | 14 | 17 |
| Missouri non-MSA | Missouri | Crawford | 15 | 1424 | 15 | 14 | 15 |
| Kansas City | Missouri | Lafayette | 35 | 1797 | 15 | 16 | 19 |
| Missouri non-MSA | Missouri | Morgan | 15 | 1306 | 14 | 15 | 13 |
| Missouri non-MSA | Missouri | Miller | 33 | 1781 | 14 | 18 | 17 |
| Missouri non-MSA | Missouri | Saline | 15 | 1789 | 14 | 13 | 15 |
| Missouri non-MSA | Missouri | Stoddard | 27 | 1905 | 13 | 17 | 22 |
| Springfield | Missouri | Polk | 16 | 1638 | 13 | 17 | 13 |
| Missouri non-MSA | Missouri | Randolph | 14 | 1444 | 13 | 15 | 15 |
| Missouri non-MSA | Missouri | Texas | 11 | 1152 | 13 | 13 | 10 |
| Missouri non-MSA | Missouri | Stone | 20 | 1417 | 13 | 15 | 15 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1268 | 12 | 12 | 14 |
| Kansas City | Missouri | Ray | 6 | 897 | 12 | 12 | 11 |
| Missouri non-MSA | Missouri | Pike | 11 | 1127 | 12 | 13 | 15 |
| Kansas City | Missouri | Clinton | 49 | 1096 | 11 | 13 | 12 |
| Missouri non-MSA | Missouri | Barry | 34 | 1641 | 11 | 12 | 15 |
| Columbia-Jefferson City | Missouri | Cooper | 13 | 1337 | 11 | 11 | 11 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2121 | 11 | 11 | 17 |
| Missouri non-MSA | Missouri | Oregon | 3 | 482 | 10 | 6 | 5 |
| Missouri non-MSA | Missouri | Henry | 18 | 1274 | 10 | 11 | 16 |
| Missouri non-MSA | Missouri | Mississippi | 9 | 1055 | 10 | 11 | 15 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1869 | 10 | 10 | 13 |
| Joplin | Missouri | Newton | 40 | 3166 | 10 | 12 | 19 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2188 | 10 | 12 | 17 |
| Missouri non-MSA | Missouri | Perry | 15 | 1714 | 10 | 10 | 15 |
| St. Joseph | Missouri | Andrew | 13 | 976 | 9 | 10 | 11 |
| Missouri non-MSA | Missouri | Madison | 10 | 1049 | 8 | 10 | 11 |
| Missouri non-MSA | Missouri | Washington | 32 | 1625 | 8 | 10 | 16 |
| Missouri non-MSA | Missouri | Wright | 19 | 904 | 8 | 8 | 7 |
| Missouri non-MSA | Missouri | Harrison | 7 | 537 | 8 | 9 | 7 |
| Missouri non-MSA | Missouri | Carroll | 8 | 565 | 8 | 8 | 8 |
| Kansas City | Missouri | Bates | 9 | 679 | 8 | 8 | 9 |
| Missouri non-MSA | Missouri | New Madrid | 26 | 1487 | 8 | 7 | 12 |
| Missouri non-MSA | Missouri | Douglas | 19 | 530 | 7 | 5 | 5 |
| Kansas City | Kansas | Linn | 2 | 407 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Gasconade | 27 | 587 | 7 | 6 | 7 |
| Missouri non-MSA | Missouri | Vernon | 13 | 826 | 7 | 10 | 9 |
| Missouri non-MSA | Missouri | Livingston | 19 | 893 | 7 | 7 | 7 |
| St. Joseph | Missouri | DeKalb | 17 | 701 | 6 | 6 | 8 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1524 | 6 | 8 | 6 |
| Columbia-Jefferson City | Missouri | Moniteau | 15 | 1378 | 6 | 9 | 12 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1069 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Macon | 5 | 781 | 6 | 6 | 11 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 344 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 421 | 5 | 4 | 5 |
| Missouri non-MSA | Missouri | Pemiscot | 20 | 1203 | 5 | 7 | 8 |
| Missouri non-MSA | Missouri | Grundy | 18 | 597 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Gentry | 15 | 526 | 5 | 7 | 6 |
| Missouri non-MSA | Missouri | Wayne | 4 | 594 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Ripley | 8 | 614 | 5 | 5 | 6 |
| Missouri non-MSA | Missouri | Iron | 1 | 306 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Barton | 7 | 703 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Ralls | 4 | 578 | 5 | 6 | 8 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 11 | 913 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Dent | 6 | 620 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Ozark | 4 | 346 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Daviess | 8 | 410 | 4 | 4 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 5 | 310 | 4 | 3 | 3 |
| Missouri non-MSA | Missouri | Monroe | 5 | 452 | 4 | 3 | 5 |
| Missouri non-MSA | Missouri | Linn | 11 | 379 | 3 | 3 | 4 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 566 | 3 | 3 | 5 |
| Kansas City | Missouri | Caldwell | 3 | 467 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Carter | 6 | 348 | 3 | 3 | 3 |
| Springfield | Missouri | Dallas | 14 | 649 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 382 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 4 | 398 | 2 | 4 | 5 |
| St. Joseph | Kansas | Doniphan | 5 | 607 | 2 | 6 | 9 |
| Missouri non-MSA | Missouri | Holt | 7 | 311 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Dade | 8 | 326 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Worth | 0 | 106 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Maries | 6 | 417 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Atchison | 4 | 250 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Mercer | 1 | 109 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 601 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Shelby | 1 | 265 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Hickory | 6 | 403 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Chariton | 1 | 282 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Cedar | 8 | 472 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 155 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 207 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Lewis | 2 | 484 | 1 | 3 | 4 |
| Missouri non-MSA | Missouri | Clark | 4 | 337 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Scotland | 2 | 212 | 1 | 1 | 2 |
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
