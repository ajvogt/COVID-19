# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/18/2020  
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
| St. Louis-Farmington | 2948 | 181382 | 1883 | 1921 | 2038 |
| Kansas City | 1400 | 120361 | 1198 | 1296 | 1287 |
| Missouri non-MSA | 1169 | 83958 | 792 | 855 | 847 |
| Springfield | 336 | 26275 | 284 | 281 | 255 |
| Columbia-Jefferson City | 168 | 27090 | 192 | 217 | 250 |
| Cape Girardeau-Sikeston | 156 | 10284 | 68 | 82 | 103 |
| Joplin | 180 | 12469 | 59 | 67 | 89 |
| St. Joseph | 118 | 7950 | 56 | 73 | 85 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1215 | 62531 | 619 | 631 | 656 |
| Kansas City | Kansas | Johnson | 381 | 33964 | 401 | 420 | 399 |
| St. Louis-Farmington | Illinois | Madison | 346 | 18707 | 241 | 238 | 240 |
| St. Louis-Farmington | Missouri | St. Charles | 249 | 24477 | 238 | 243 | 273 |
| Kansas City | Missouri | Kansas City | 326 | 27447 | 209 | 238 | 260 |
| St. Louis-Farmington | Illinois | St. Clair | 319 | 17086 | 192 | 209 | 206 |
| Kansas City | Missouri | Jackson | 206 | 21082 | 185 | 214 | 223 |
| Springfield | Missouri | Greene | 238 | 16926 | 182 | 176 | 163 |
| Kansas City | Kansas | Wyandotte | 187 | 13834 | 150 | 146 | 129 |
| St. Louis-Farmington | Missouri | St. Louis City | 279 | 15471 | 142 | 141 | 150 |
| St. Louis-Farmington | Missouri | Jefferson | 121 | 13600 | 133 | 138 | 160 |
| Columbia-Jefferson City | Missouri | Boone | 36 | 12177 | 103 | 106 | 111 |
| Springfield | Missouri | Christian | 35 | 4840 | 64 | 61 | 53 |
| Missouri non-MSA | Missouri | Pettis | 50 | 3716 | 63 | 72 | 40 |
| Kansas City | Missouri | Cass | 46 | 4868 | 58 | 62 | 59 |
| Missouri non-MSA | Missouri | Howell | 35 | 2099 | 56 | 34 | 21 |
| St. Louis-Farmington | Missouri | Franklin | 102 | 5850 | 56 | 57 | 60 |
| St. Louis-Farmington | Missouri | St. Francois | 58 | 5911 | 54 | 47 | 55 |
| Kansas City | Missouri | Clay | 87 | 5615 | 51 | 55 | 59 |
| Joplin | Missouri | Jasper | 140 | 9267 | 48 | 54 | 70 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 91 | 5933 | 44 | 48 | 60 |
| St. Louis-Farmington | Missouri | Lincoln | 17 | 3147 | 41 | 40 | 40 |
| Kansas City | Kansas | Leavenworth | 36 | 4553 | 40 | 47 | 44 |
| St. Louis-Farmington | Illinois | Clinton | 77 | 4070 | 39 | 41 | 47 |
| St. Joseph | Missouri | Buchanan | 83 | 5648 | 39 | 52 | 57 |
| Columbia-Jefferson City | Missouri | Cole | 77 | 7090 | 36 | 47 | 64 |
| St. Louis-Farmington | Illinois | Monroe | 56 | 2697 | 36 | 36 | 35 |
| St. Louis-Farmington | Illinois | Macoupin | 55 | 2915 | 33 | 35 | 44 |
| Missouri non-MSA | Missouri | Taney | 47 | 3488 | 29 | 37 | 35 |
| Missouri non-MSA | Missouri | Laclede | 38 | 2279 | 25 | 26 | 24 |
| Columbia-Jefferson City | Missouri | Callaway | 17 | 3403 | 24 | 31 | 35 |
| Kansas City | Kansas | Miami | 7 | 1456 | 22 | 26 | 22 |
| Missouri non-MSA | Missouri | Pulaski | 26 | 2202 | 22 | 35 | 28 |
| Missouri non-MSA | Missouri | Johnson | 25 | 2958 | 21 | 24 | 27 |
| Missouri non-MSA | Missouri | Butler | 11 | 2618 | 21 | 26 | 28 |
| Springfield | Missouri | Webster | 33 | 2171 | 20 | 22 | 20 |
| St. Louis-Farmington | Illinois | Jersey | 32 | 1723 | 20 | 24 | 25 |
| Missouri non-MSA | Missouri | Adair | 4 | 1384 | 20 | 18 | 16 |
| Missouri non-MSA | Missouri | Miller | 39 | 1850 | 19 | 19 | 18 |
| Kansas City | Missouri | Platte | 18 | 2068 | 19 | 21 | 23 |
| Missouri non-MSA | Missouri | Dunklin | 14 | 1963 | 19 | 16 | 15 |
| Missouri non-MSA | Missouri | Phelps | 76 | 2195 | 19 | 22 | 28 |
| Missouri non-MSA | Missouri | Camden | 59 | 2859 | 18 | 22 | 24 |
| St. Louis-Farmington | Illinois | Bond | 15 | 1390 | 16 | 17 | 18 |
| Missouri non-MSA | Missouri | Benton | 13 | 1101 | 16 | 22 | 13 |
| Missouri non-MSA | Missouri | Crawford | 15 | 1459 | 15 | 15 | 15 |
| Cape Girardeau-Sikeston | Missouri | Scott | 49 | 3114 | 15 | 23 | 32 |
| St. Louis-Farmington | Missouri | Warren | 6 | 1457 | 15 | 13 | 16 |
| Missouri non-MSA | Missouri | Audrain | 22 | 1404 | 14 | 18 | 17 |
| Missouri non-MSA | Missouri | Saline | 16 | 1828 | 14 | 15 | 15 |
| Missouri non-MSA | Missouri | Morgan | 16 | 1343 | 14 | 17 | 13 |
| Missouri non-MSA | Missouri | Stone | 23 | 1457 | 14 | 15 | 14 |
| Kansas City | Missouri | Lafayette | 35 | 1821 | 14 | 15 | 18 |
| Missouri non-MSA | Missouri | Stoddard | 29 | 1928 | 14 | 16 | 20 |
| Kansas City | Missouri | Ray | 7 | 933 | 13 | 14 | 12 |
| Missouri non-MSA | Missouri | Randolph | 15 | 1469 | 13 | 15 | 15 |
| Springfield | Missouri | Polk | 16 | 1679 | 13 | 17 | 13 |
| Missouri non-MSA | Missouri | Marion | 23 | 2155 | 13 | 22 | 23 |
| Missouri non-MSA | Missouri | Perry | 15 | 1749 | 12 | 10 | 14 |
| Missouri non-MSA | Missouri | Texas | 12 | 1174 | 12 | 12 | 10 |
| Missouri non-MSA | Missouri | Lawrence | 41 | 2153 | 12 | 12 | 16 |
| Kansas City | Missouri | Clinton | 49 | 1121 | 12 | 13 | 11 |
| Missouri non-MSA | Missouri | Wright | 19 | 935 | 11 | 10 | 7 |
| Columbia-Jefferson City | Missouri | Cooper | 14 | 1369 | 11 | 11 | 11 |
| Missouri non-MSA | Missouri | Barry | 35 | 1667 | 11 | 11 | 13 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 2 | 1286 | 11 | 11 | 14 |
| Joplin | Missouri | Newton | 40 | 3202 | 10 | 12 | 18 |
| Missouri non-MSA | Missouri | Vernon | 13 | 858 | 10 | 10 | 9 |
| Missouri non-MSA | Missouri | Pike | 11 | 1148 | 10 | 12 | 15 |
| Missouri non-MSA | Missouri | Livingston | 19 | 926 | 9 | 8 | 7 |
| Missouri non-MSA | Missouri | Madison | 10 | 1073 | 9 | 10 | 11 |
| Missouri non-MSA | Missouri | Macon | 5 | 826 | 9 | 8 | 11 |
| Missouri non-MSA | Missouri | Oregon | 3 | 485 | 9 | 6 | 5 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2224 | 9 | 10 | 16 |
| Missouri non-MSA | Missouri | Douglas | 19 | 543 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | Mississippi | 9 | 1062 | 8 | 10 | 13 |
| St. Joseph | Missouri | Andrew | 13 | 986 | 8 | 9 | 11 |
| Missouri non-MSA | Missouri | Henry | 18 | 1289 | 8 | 10 | 14 |
| Missouri non-MSA | Missouri | New Madrid | 26 | 1507 | 8 | 8 | 12 |
| Missouri non-MSA | Missouri | Harrison | 7 | 551 | 8 | 9 | 7 |
| Missouri non-MSA | Missouri | Carroll | 8 | 574 | 8 | 8 | 8 |
| Missouri non-MSA | Missouri | Washington | 34 | 1640 | 7 | 8 | 15 |
| Kansas City | Missouri | Bates | 10 | 698 | 7 | 9 | 9 |
| Kansas City | Kansas | Linn | 2 | 421 | 7 | 6 | 6 |
| Missouri non-MSA | Missouri | Iron | 1 | 320 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1535 | 7 | 7 | 7 |
| Missouri non-MSA | Missouri | Gentry | 15 | 543 | 6 | 7 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 28 | 600 | 6 | 7 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 6 | 1086 | 6 | 8 | 9 |
| Columbia-Jefferson City | Missouri | Moniteau | 16 | 1390 | 6 | 8 | 10 |
| St. Joseph | Missouri | DeKalb | 17 | 709 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Montgomery | 6 | 432 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Daviess | 9 | 424 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Dent | 6 | 634 | 5 | 6 | 7 |
| Missouri non-MSA | Missouri | Ripley | 8 | 624 | 5 | 4 | 6 |
| Missouri non-MSA | Missouri | Wayne | 4 | 599 | 5 | 6 | 6 |
| Kansas City | Missouri | Caldwell | 3 | 480 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Barton | 7 | 713 | 4 | 4 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 20 | 1217 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Grundy | 18 | 610 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 176 | 4 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 11 | 919 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Ralls | 4 | 586 | 4 | 5 | 7 |
| St. Louis-Farmington | Illinois | Calhoun | 1 | 350 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Monroe | 5 | 465 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Ozark | 5 | 348 | 4 | 3 | 2 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 5 | 318 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Linn | 11 | 390 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 609 | 3 | 2 | 3 |
| Springfield | Missouri | Dallas | 14 | 659 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Shannon | 9 | 388 | 3 | 3 | 2 |
| St. Joseph | Kansas | Doniphan | 5 | 607 | 2 | 5 | 8 |
| Missouri non-MSA | Missouri | Lewis | 2 | 494 | 2 | 4 | 4 |
| Missouri non-MSA | Missouri | Mercer | 1 | 116 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 575 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Carter | 6 | 351 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 4 | 402 | 2 | 3 | 5 |
| Missouri non-MSA | Missouri | Maries | 6 | 424 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 211 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Cedar | 8 | 475 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Holt | 7 | 313 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Chariton | 2 | 287 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Dade | 8 | 330 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 1 | 268 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Hickory | 6 | 407 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Scotland | 2 | 216 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Worth | 0 | 105 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Atchison | 4 | 253 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Clark | 4 | 341 | 0 | 2 | 3 |
| Missouri non-MSA | Missouri | Putnam | 1 | 183 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 1 | 144 | 0 | 0 | 0 |
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
