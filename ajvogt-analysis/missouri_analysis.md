# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 12/28/2020  
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
| St. Louis-Farmington | 3220 | 195431 | 1263 | 1518 | 1747 |
| Kansas City | 1518 | 129913 | 910 | 1038 | 1115 |
| Missouri non-MSA | 1314 | 89702 | 553 | 614 | 726 |
| Springfield | 372 | 28293 | 194 | 224 | 238 |
| Columbia-Jefferson City | 193 | 28800 | 154 | 176 | 199 |
| Cape Girardeau-Sikeston | 172 | 10858 | 54 | 60 | 77 |
| Joplin | 197 | 13075 | 52 | 60 | 65 |
| St. Joseph | 127 | 8391 | 43 | 46 | 66 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1342 | 67120 | 392 | 503 | 569 |
| Kansas City | Kansas | Johnson | 413 | 36727 | 234 | 326 | 333 |
| Kansas City | Missouri | Kansas City | 349 | 29319 | 187 | 191 | 219 |
| Kansas City | Missouri | Jackson | 230 | 22735 | 173 | 166 | 197 |
| St. Louis-Farmington | Missouri | St. Charles | 281 | 26481 | 167 | 204 | 232 |
| St. Louis-Farmington | Illinois | Madison | 379 | 20334 | 152 | 183 | 210 |
| St. Louis-Farmington | Illinois | St. Clair | 333 | 18413 | 130 | 148 | 181 |
| Springfield | Missouri | Greene | 251 | 18206 | 128 | 142 | 151 |
| Kansas City | Kansas | Wyandotte | 193 | 14857 | 107 | 121 | 114 |
| St. Louis-Farmington | Missouri | St. Louis City | 292 | 16532 | 95 | 111 | 129 |
| St. Louis-Farmington | Missouri | Jefferson | 126 | 14611 | 93 | 106 | 129 |
| Columbia-Jefferson City | Missouri | Boone | 42 | 13037 | 77 | 90 | 95 |
| St. Louis-Farmington | Missouri | Franklin | 109 | 6343 | 50 | 50 | 53 |
| Kansas City | Missouri | Clay | 94 | 6070 | 46 | 44 | 51 |
| Kansas City | Missouri | Cass | 52 | 5371 | 44 | 51 | 57 |
| Springfield | Missouri | Christian | 44 | 5306 | 42 | 51 | 53 |
| Joplin | Missouri | Jasper | 154 | 9705 | 37 | 44 | 51 |
| St. Louis-Farmington | Missouri | St. Francois | 68 | 6324 | 36 | 42 | 44 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 95 | 6305 | 35 | 40 | 46 |
| Columbia-Jefferson City | Missouri | Cole | 85 | 7438 | 35 | 35 | 45 |
| Missouri non-MSA | Missouri | Pulaski | 27 | 2497 | 33 | 24 | 30 |
| St. Louis-Farmington | Missouri | Lincoln | 20 | 3447 | 28 | 31 | 35 |
| St. Louis-Farmington | Illinois | Clinton | 80 | 4342 | 26 | 31 | 36 |
| St. Joseph | Missouri | Buchanan | 91 | 5913 | 26 | 28 | 45 |
| St. Louis-Farmington | Illinois | Monroe | 56 | 2991 | 26 | 31 | 32 |
| Columbia-Jefferson City | Missouri | Callaway | 19 | 3648 | 21 | 25 | 28 |
| Kansas City | Missouri | Platte | 20 | 2289 | 21 | 22 | 22 |
| Missouri non-MSA | Missouri | Phelps | 82 | 2406 | 21 | 20 | 23 |
| St. Louis-Farmington | Illinois | Jersey | 36 | 1913 | 20 | 20 | 23 |
| Missouri non-MSA | Missouri | Crawford | 19 | 1637 | 20 | 17 | 15 |
| St. Louis-Farmington | Illinois | Macoupin | 69 | 3143 | 19 | 26 | 34 |
| Missouri non-MSA | Missouri | Camden | 60 | 3059 | 19 | 19 | 21 |
| Kansas City | Kansas | Miami | 10 | 1648 | 19 | 22 | 21 |
| Missouri non-MSA | Missouri | Johnson | 28 | 3172 | 19 | 21 | 23 |
| Missouri non-MSA | Missouri | Taney | 51 | 3685 | 18 | 20 | 29 |
| Missouri non-MSA | Missouri | Adair | 4 | 1555 | 18 | 19 | 16 |
| Kansas City | Kansas | Leavenworth | 38 | 4823 | 17 | 34 | 36 |
| Kansas City | Missouri | Lafayette | 38 | 2002 | 17 | 16 | 17 |
| Missouri non-MSA | Missouri | Laclede | 44 | 2439 | 15 | 16 | 22 |
| Cape Girardeau-Sikeston | Missouri | Scott | 59 | 3274 | 15 | 15 | 22 |
| Joplin | Missouri | Newton | 43 | 3370 | 14 | 15 | 13 |
| Missouri non-MSA | Missouri | Saline | 21 | 1958 | 14 | 13 | 13 |
| Missouri non-MSA | Missouri | Butler | 14 | 2745 | 14 | 14 | 21 |
| Missouri non-MSA | Missouri | Audrain | 32 | 1592 | 14 | 17 | 17 |
| St. Louis-Farmington | Missouri | Warren | 9 | 1594 | 13 | 14 | 13 |
| Missouri non-MSA | Missouri | Howell | 36 | 2241 | 13 | 12 | 22 |
| Springfield | Missouri | Webster | 38 | 2334 | 13 | 17 | 17 |
| Kansas City | Missouri | Ray | 8 | 1067 | 12 | 14 | 13 |
| Missouri non-MSA | Missouri | Pettis | 60 | 3881 | 11 | 25 | 41 |
| Missouri non-MSA | Missouri | Marion | 24 | 2275 | 11 | 12 | 17 |
| Missouri non-MSA | Missouri | Miller | 42 | 1977 | 10 | 15 | 16 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 3 | 1383 | 10 | 9 | 11 |
| Missouri non-MSA | Missouri | Randolph | 15 | 1577 | 10 | 10 | 13 |
| Missouri non-MSA | Missouri | Vernon | 16 | 948 | 10 | 10 | 9 |
| St. Louis-Farmington | Illinois | Bond | 16 | 1487 | 10 | 10 | 15 |
| Missouri non-MSA | Missouri | Pike | 14 | 1247 | 9 | 10 | 12 |
| Missouri non-MSA | Missouri | Lawrence | 47 | 2257 | 9 | 10 | 12 |
| Missouri non-MSA | Missouri | McDonald | 18 | 1624 | 9 | 8 | 7 |
| Missouri non-MSA | Missouri | Stone | 24 | 1570 | 9 | 12 | 13 |
| Missouri non-MSA | Missouri | Nodaway | 18 | 2286 | 8 | 7 | 11 |
| Missouri non-MSA | Missouri | Wright | 23 | 1013 | 8 | 8 | 8 |
| Kansas City | Missouri | Clinton | 56 | 1214 | 8 | 9 | 11 |
| Missouri non-MSA | Missouri | Barry | 35 | 1763 | 8 | 10 | 11 |
| Kansas City | Missouri | Bates | 10 | 780 | 8 | 8 | 8 |
| Springfield | Missouri | Polk | 21 | 1765 | 8 | 10 | 13 |
| Missouri non-MSA | Missouri | Iron | 1 | 384 | 7 | 6 | 5 |
| Missouri non-MSA | Missouri | Washington | 39 | 1726 | 7 | 8 | 10 |
| Missouri non-MSA | Missouri | Madison | 10 | 1150 | 7 | 8 | 9 |
| Missouri non-MSA | Missouri | Dunklin | 15 | 2037 | 7 | 13 | 12 |
| Missouri non-MSA | Missouri | Perry | 19 | 1821 | 7 | 9 | 10 |
| Missouri non-MSA | Missouri | Henry | 21 | 1398 | 7 | 9 | 11 |
| St. Joseph | Missouri | Andrew | 13 | 1059 | 6 | 7 | 9 |
| Missouri non-MSA | Missouri | Texas | 16 | 1296 | 6 | 11 | 11 |
| Columbia-Jefferson City | Missouri | Cooper | 20 | 1461 | 6 | 9 | 10 |
| Missouri non-MSA | Missouri | Carroll | 14 | 638 | 6 | 6 | 7 |
| Missouri non-MSA | Missouri | Gasconade | 29 | 656 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | Livingston | 21 | 995 | 6 | 8 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 8 | 1152 | 6 | 7 | 7 |
| St. Joseph | Kansas | Doniphan | 5 | 673 | 5 | 6 | 5 |
| Kansas City | Missouri | Caldwell | 4 | 536 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Douglas | 19 | 597 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Wayne | 6 | 653 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Stoddard | 32 | 1986 | 5 | 8 | 13 |
| Missouri non-MSA | Missouri | New Madrid | 29 | 1569 | 5 | 6 | 8 |
| Kansas City | Kansas | Linn | 3 | 475 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Macon | 8 | 888 | 5 | 8 | 7 |
| Missouri non-MSA | Missouri | Ralls | 6 | 635 | 5 | 5 | 5 |
| Missouri non-MSA | Missouri | Morgan | 21 | 1410 | 5 | 8 | 11 |
| Columbia-Jefferson City | Missouri | Moniteau | 17 | 1456 | 4 | 6 | 8 |
| Missouri non-MSA | Missouri | Dent | 7 | 680 | 4 | 5 | 6 |
| Missouri non-MSA | Missouri | Ripley | 8 | 657 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Grundy | 22 | 658 | 4 | 4 | 5 |
| Missouri non-MSA | Missouri | Sullivan | 9 | 648 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Daviess | 9 | 457 | 4 | 3 | 4 |
| Missouri non-MSA | Missouri | Harrison | 7 | 607 | 4 | 5 | 7 |
| St. Joseph | Missouri | DeKalb | 18 | 746 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Monroe | 5 | 500 | 3 | 3 | 4 |
| Missouri non-MSA | Missouri | Gentry | 16 | 590 | 3 | 5 | 6 |
| Missouri non-MSA | Missouri | Oregon | 3 | 522 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Montgomery | 8 | 478 | 3 | 5 | 4 |
| Missouri non-MSA | Missouri | Pemiscot | 20 | 1257 | 3 | 4 | 6 |
| Missouri non-MSA | Missouri | Barton | 9 | 750 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Dade | 8 | 361 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Lewis | 3 | 523 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Benton | 16 | 1156 | 3 | 8 | 13 |
| Missouri non-MSA | Missouri | Mississippi | 11 | 1109 | 3 | 5 | 8 |
| Missouri non-MSA | Missouri | Chariton | 2 | 319 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Clark | 4 | 365 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | St. Clair | 4 | 438 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Maries | 6 | 452 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Ozark | 4 | 367 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 194 | 2 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 2 | 608 | 2 | 3 | 3 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 11 | 944 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Cedar | 8 | 497 | 2 | 2 | 1 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 335 | 1 | 2 | 2 |
| Springfield | Missouri | Dallas | 18 | 682 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Linn | 11 | 404 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Shannon | 9 | 407 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Carter | 6 | 366 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Hickory | 9 | 420 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 115 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Putnam | 1 | 196 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 225 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Holt | 9 | 323 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Shelby | 3 | 285 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Mercer | 1 | 124 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 2 | 220 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Atchison | 5 | 259 | 0 | 0 | 1 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 356 | 0 | 1 | 4 |
| Missouri non-MSA | Missouri | Knox | 1 | 147 | 0 | 0 | 0 |
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
